#!/usr/bin/env python3
"""
tools/image_search.py

Fetches one image per slide from free sources (Openverse → Wikimedia Commons → Pexels).
Reads a JSON manifest, downloads images, writes a results JSON.

Usage:
    python3 tools/image_search.py --manifest <path>/image_manifest.json \
                                   --output-dir <path>/svg_output/images/

Manifest format (written by the slide-generator agent):
    [
      {"slide_id": "slide01", "query": "SQL database tables joining", "style_hint": "diagram"},
      {"slide_id": "slide03", "query": "data analyst at computer", "style_hint": "photo"}
    ]

Results JSON (written next to the manifest as image_results.json):
    {
      "slide01": {
        "local_path": "svg_output/images/slide01.jpg",
        "source": "openverse",
        "license": "CC BY",
        "attribution": "Photo by Jane Doe on Flickr",
        "status": "sourced"
      },
      "slide03": { ..., "status": "needs-manual" }
    }

Statuses:
    sourced      — image downloaded, ready to embed
    needs-manual — all providers failed; leave placeholder

Providers (tried in order):
    1. Openverse  — public API, no key, CC-licensed
    2. Wikimedia Commons — public API, no key, mixed CC
    3. Pexels     — free API key, set PEXELS_API_KEY in env or .env file

Requires:
    pip3 install requests Pillow
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests not installed. Run: pip3 install requests")
    sys.exit(1)

try:
    from PIL import Image as PILImage
    _PIL_AVAILABLE = True
except ImportError:
    _PIL_AVAILABLE = False

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

TIMEOUT = 10          # seconds per HTTP request
MAX_IMAGE_BYTES = 5 * 1024 * 1024   # skip images larger than 5 MB
TARGET_WIDTH = 1280   # resize downloaded images to this width if Pillow available

# Load optional .env file from repo root for PEXELS_API_KEY
def _load_dotenv() -> None:
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

_load_dotenv()


# ---------------------------------------------------------------------------
# Provider: Openverse
# ---------------------------------------------------------------------------

def _search_openverse(query: str) -> list[dict]:
    """Return up to 5 usable candidates from Openverse (commercial CC or any CC)."""
    url = "https://api.openverse.org/v1/images/"
    candidates: list[dict] = []
    for params in [
        {"q": query, "license_type": "commercial", "page_size": 10, "mature": "false"},
        {"q": _shorten_query(query), "page_size": 10, "mature": "false"},
    ]:
        if len(candidates) >= 5:
            break
        try:
            resp = requests.get(url, params=params, timeout=TIMEOUT)
            resp.raise_for_status()
            data = resp.json()
            for result in data.get("results", []):
                img_url = result.get("url") or result.get("thumbnail")
                if not img_url:
                    continue
                license_tag = result.get("license", "").upper()
                if any(t in license_tag for t in ["NC", "ND"]):
                    continue
                creator = result.get("creator", "")
                title = result.get("title", "image")
                candidates.append({
                    "url": img_url,
                    "source": "openverse",
                    "license": license_tag,
                    "attribution": f'"{title}" by {creator} (Openverse, {license_tag})',
                })
                if len(candidates) >= 5:
                    break
        except Exception:
            pass
    return candidates


# ---------------------------------------------------------------------------
# Provider: Wikimedia Commons
# ---------------------------------------------------------------------------

def _shorten_query(query: str, words: int = 3) -> str:
    """Return the first `words` words of a query for broader matching."""
    return " ".join(query.split()[:words])


def _search_wikimedia(query: str) -> list[dict]:
    """Return up to 5 usable candidates from Wikimedia Commons."""
    import re as _re
    api_url = "https://commons.wikimedia.org/w/api.php"
    candidates: list[dict] = []
    for search_term in [query, _shorten_query(query, 3), _shorten_query(query, 2)]:
        if len(candidates) >= 5:
            break
        params = {
            "action": "query",
            "generator": "search",
            "gsrsearch": f"filetype:bitmap {search_term}",
            "gsrnamespace": "6",
            "gsrlimit": "10",
            "prop": "imageinfo",
            "iiprop": "url|extmetadata|size",
            "iiurlwidth": str(TARGET_WIDTH),
            "format": "json",
        }
        try:
            resp = requests.get(api_url, params=params, timeout=TIMEOUT,
                                headers={"User-Agent": "TeachingAssistant/1.0"})
            resp.raise_for_status()
            pages = resp.json().get("query", {}).get("pages", {})
            for page in pages.values():
                info_list = page.get("imageinfo", [])
                if not info_list:
                    continue
                info = info_list[0]
                img_url = info.get("thumburl") or info.get("url")
                if not img_url:
                    continue
                # Skip URLs without a recognisable image extension (often broken)
                ext = Path(urllib.parse.urlparse(img_url).path).suffix.lower()
                if ext not in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}:
                    continue
                meta = info.get("extmetadata", {})
                license_tag = meta.get("LicenseShortName", {}).get("value", "CC")
                if any(tag in license_tag.upper() for tag in ["NC", "ND"]):
                    continue
                artist = meta.get("Artist", {}).get("value", "Unknown")
                artist = _re.sub(r"<[^>]+>", "", artist)
                candidates.append({
                    "url": img_url,
                    "source": "wikimedia",
                    "license": license_tag,
                    "attribution": f'"{page.get("title", "image")}" by {artist} (Wikimedia Commons, {license_tag})',
                })
                if len(candidates) >= 5:
                    break
        except Exception:
            pass
    return candidates


# ---------------------------------------------------------------------------
# Provider: Pexels (optional — requires PEXELS_API_KEY in env)
# ---------------------------------------------------------------------------

def _search_pexels(query: str) -> list[dict]:
    """Return up to 5 candidates from Pexels. Empty list if no API key."""
    api_key = os.environ.get("PEXELS_API_KEY", "")
    if not api_key:
        return []
    url = "https://api.pexels.com/v1/search"
    params = {"query": query, "per_page": 5, "orientation": "landscape"}
    candidates: list[dict] = []
    try:
        resp = requests.get(url, params=params,
                            headers={"Authorization": api_key}, timeout=TIMEOUT)
        resp.raise_for_status()
        for photo in resp.json().get("photos", []):
            img_url = photo.get("src", {}).get("large") or photo.get("src", {}).get("original")
            if not img_url:
                continue
            photographer = photo.get("photographer", "Unknown")
            candidates.append({
                "url": img_url,
                "source": "pexels",
                "license": "Pexels License",
                "attribution": f"Photo by {photographer} on Pexels (Pexels License)",
            })
    except Exception:
        pass
    return candidates


# ---------------------------------------------------------------------------
# Download & resize
# ---------------------------------------------------------------------------

def _download_image(img_url: str, dest_path: Path) -> bool:
    """Download image to dest_path. Returns True on success."""
    try:
        resp = requests.get(img_url, timeout=30, stream=True)
        resp.raise_for_status()
        content_length = int(resp.headers.get("content-length", 0))
        if content_length and content_length > MAX_IMAGE_BYTES:
            return False
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dest_path, "wb") as f:
            downloaded = 0
            for chunk in resp.iter_content(chunk_size=8192):
                downloaded += len(chunk)
                if downloaded > MAX_IMAGE_BYTES:
                    return False
                f.write(chunk)
        # Resize if Pillow is available
        if _PIL_AVAILABLE:
            try:
                img = PILImage.open(dest_path)
                if img.width > TARGET_WIDTH:
                    ratio = TARGET_WIDTH / img.width
                    new_h = int(img.height * ratio)
                    img = img.resize((TARGET_WIDTH, new_h), PILImage.LANCZOS)
                    img.save(dest_path, optimize=True, quality=85)
            except Exception:
                pass  # keep original if resize fails
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Main acquisition loop
# ---------------------------------------------------------------------------

PROVIDERS = [_search_openverse, _search_wikimedia, _search_pexels]


def acquire_images(manifest: list[dict], output_dir: Path) -> dict:
    """Process manifest, download images, return results dict."""
    results: dict[str, dict] = {}
    output_dir.mkdir(parents=True, exist_ok=True)

    for entry in manifest:
        slide_id = entry["slide_id"]
        query = entry.get("query", "")
        style_hint = entry.get("style_hint", "photo")

        print(f"  [{slide_id}] searching: {query!r} ({style_hint})")

        effective_query = f"{query} {style_hint}" if style_hint not in query else query

        # Collect candidates from all providers, then try each until one downloads
        all_candidates: list[dict] = []
        for provider_fn in PROVIDERS:
            all_candidates.extend(provider_fn(effective_query))

        if not all_candidates:
            print(f"    → no image found — marked needs-manual")
            results[slide_id] = {"status": "needs-manual", "query": query}
            continue

        # Try each candidate in order until one downloads successfully
        sourced = False
        for candidate in all_candidates:
            url_path = urllib.parse.urlparse(candidate["url"]).path
            ext = Path(url_path).suffix.lower()
            if ext not in {".jpg", ".jpeg", ".png", ".webp", ".gif"}:
                ext = ".jpg"
            dest = output_dir / f"{slide_id}{ext}"
            if _download_image(candidate["url"], dest):
                print(f"    → {candidate['source']}: {dest.name} ({candidate['license']})")
                results[slide_id] = {
                    "local_path": str(dest),
                    "source": candidate["source"],
                    "license": candidate["license"],
                    "attribution": candidate["attribution"],
                    "status": "sourced",
                    "query": query,
                }
                sourced = True
                break

        if not sourced:
            print(f"    → all candidates failed download — marked needs-manual")
            results[slide_id] = {"status": "needs-manual", "query": query}

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch slide images from free sources.")
    parser.add_argument("--manifest", required=True,
                        help="Path to image_manifest.json")
    parser.add_argument("--output-dir", required=True,
                        help="Directory to save downloaded images")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        print(f"ERROR: manifest not found: {manifest_path}")
        sys.exit(1)

    manifest = json.loads(manifest_path.read_text())
    output_dir = Path(args.output_dir)

    print(f"Image search: {len(manifest)} slides → {output_dir}")
    results = acquire_images(manifest, output_dir)

    sourced = sum(1 for r in results.values() if r["status"] == "sourced")
    manual = sum(1 for r in results.values() if r["status"] == "needs-manual")
    print(f"\nDone: {sourced} sourced, {manual} needs-manual")

    results_path = manifest_path.parent / "image_results.json"
    results_path.write_text(json.dumps(results, indent=2))
    print(f"Results written to: {results_path}")


if __name__ == "__main__":
    main()
