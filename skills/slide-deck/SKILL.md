/---
name: slide-deck
description: Generate a complete slide-by-slide PowerPoint blueprint following the project design system; supports pitch, training, and report styles.
arguments: '"<topic>" [--slides N] [--audience <audience>] [--style <style>] [--subject <subject>] [--level <level>] [--save]'
outputs:
  - slide_deck_template/decks/[subject]/[topic-slug].md
  - slide_deck_template/decks/[subject]/[topic-slug]/[topic-slug].pptx
---

# Skill: slide-deck

## Usage

```
/slide-deck "<topic>" [--slides N] [--audience <audience>] [--style <style>] [--subject <subject>] [--level <level>] [--save]
```

## Arguments

| Argument | Required | Values | Default |
|----------|----------|--------|---------|
| `topic` | yes | e.g. `"SQL Joins for Beginners"` | — |
| `--slides` | no | minimum slide count; agent generates more if the topic requires it | topic-driven (no ceiling) |
| `--audience` | no | `students` / `investors` / `executives` / `clients` / `general` | `students` |
| `--style` | no | `training` / `pitch` / `report` | `training` |
| `--subject` | no | `sql` / `excel` / `powerbi` | inferred from topic |
| `--level` | no | `beginner` / `intermediate` / `advanced` | inferred from topic |
| `--save` | no | flag | off (print only) |

## Examples

```
/slide-deck "SQL Joins for Beginners" --style training --save
/slide-deck "Excel PivotTables" --level intermediate --slides 12 --save
/slide-deck "Power BI for Executives" --audience executives --style pitch --save
```

---

## Execution Steps

### Step 1 — Parse arguments

Extract `topic`, `slides`, `audience`, `style`, `subject`, `level`, and `--save` flag. Infer `subject` and `level` from topic if not stated. Normalize `topic` to a slug for file naming.

---

### Step 2 — Check for knowledge doc

Look for an existing knowledge doc at `skills/[subject]-[level]-[topic-slug].md`. Note the path if found — pass it to the agent as `knowledge_doc`.

---

### Step 3 — Spawn Slide Generator agent

Use the Agent tool to spawn the `slide-generator` subagent with these inputs:

```
topic: [topic]
audience: [audience]
style: [style]
slides: [slides]
knowledge_doc: [path if found, omit if not]
--save: [true if --save flag was set]
```

Wait for the agent to complete. It will write the blueprint to (if --save):
`slide_deck_template/decks/[subject]/[topic-slug].md`

---

### Step 3.5 — Fetch slide images

After the blueprint is saved, extract the Image Manifest block from the blueprint file and
write it to:
```
slide_deck_template/decks/[subject]/[topic-slug]/image_manifest.json
```

Then run:
```bash
python3 tools/image_search.py \
  --manifest "slide_deck_template/decks/[subject]/[topic-slug]/image_manifest.json" \
  --output-dir "slide_deck_template/decks/[subject]/[topic-slug]/svg_output/images/"
```

This produces:
- Downloaded images in `svg_output/images/slide01.jpg`, `slide03.jpg`, etc.
- `image_results.json` alongside the manifest — maps each `slide_id` to `local_path` (or `needs-manual`)

Slides marked `needs-manual` keep their placeholder icon. Continue to Step 4 regardless of how
many images were sourced — a partial result is fine.

Skip this step if `--save` was not used (no manifest exists to process).

---

### Step 4 — Write SVGs directly (PPT Master approach)

Create the SVG output directory:

```bash
mkdir -p "slide_deck_template/decks/[subject]/[topic-slug]/svg_output"
```

Then, for each slide in the blueprint (slide 1 through N), write one complete SVG file
directly to:

```
slide_deck_template/decks/[subject]/[topic-slug]/svg_output/slide01.svg
slide_deck_template/decks/[subject]/[topic-slug]/svg_output/slide02.svg
...
```

**Do not batch-generate or script-generate SVGs. Write each one individually using the
Write tool, sequentially, in a single continuous pass.** Re-read the blueprint spec for
each slide before writing it.

Before writing each SVG, check `image_results.json` for that slide's `local_path`. If
`status == "sourced"`, use the local path as the `href` in the SVG `<image>` element.
If `status == "needs-manual"` or the slide has no image, use the `<use data-icon="...">` placeholder.

---

#### Design System (apply to every SVG)

Read the full design system before writing any SVG:
`slide_deck_template/examples/svg-design-system.md`

---

After all SVGs are written, convert to PPTX:

```bash
python3 tools/svgs_to_pptx.py "slide_deck_template/decks/[subject]/[topic-slug]/svg_output"
```

Writes `slide_deck_template/decks/[subject]/[topic-slug]/[topic-slug].pptx`.

**Fallback (offline, text-only):** `python3 tools/md_to_pptx.py slide_deck_template/decks/[subject]/[topic-slug].md`

---

### Step 5 — Run Slide QC

Spawn the `slide-qc` subagent to reconcile the generated deck against the project design system.

Pass it:
```
deck_path: slide_deck_template/decks/[subject]/[topic-slug].md
svg_dir:   slide_deck_template/decks/[subject]/[topic-slug]/svg_output/
design_references:
  - slide_deck_template/examples/deck-analysis.md
  - slide_deck_template/examples/svg-design-system.md
```

The agent will:
1. Read both design reference files
2. Review every slide in the blueprint and each exported SVG for compliance
3. Score across all five quality dimensions
4. Output an issue log with severity ratings and the top 3 priority fixes
5. Append its review to `log/slide-qc.log`

If `--save` was not used (blueprint was printed inline only), skip Step 4 and Step 5 — QC only applies to saved, exportable decks.

---

### Step 7 — Report result

Confirm files written:
- Blueprint:      `slide_deck_template/decks/[subject]/[topic-slug].md`
- Images:         `slide_deck_template/decks/[subject]/[topic-slug]/svg_output/images/` (N sourced, M needs-manual)
- SVG slides:     `slide_deck_template/decks/[subject]/[topic-slug]/svg_output/slide01.svg` … `slideN.svg`
- PPTX (native):  `slide_deck_template/decks/[subject]/[topic-slug]/[topic-slug].pptx`
- QC report:      logged to `log/slide-qc.log`; inline review delivered above

For any slides marked `needs-manual`, list the slide number and the query that failed so the instructor can source an image manually.
