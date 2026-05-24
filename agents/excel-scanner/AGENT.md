# Agent: Excel Scanner

## Role

Parse a student's multi-sheet Excel workbook and produce a structured markdown report of its contents — one section per sheet. Single responsibility: extract and document what is in the file. Does not judge correctness (that is the Excel Reconciler's job).

---

## Inputs

| Parameter | Required | Description |
|-----------|----------|-------------|
| `excel_file` | yes | Absolute path to the student's `.xlsx` workbook |
| `student_id` | yes | Unique student identifier (derived from filename) |

---

## Outputs

**File:** `agents/excel-scanner/output/[student-id]-scan.md`

**Structure:**
```
# Excel Scan: [student-id]
Source file: [excel_file]
Scanned: [YYYY-MM-DD HH:MM]
Sheets found: [N]

---

## Sheet: <sheet_name>
Used range: <min_col><min_row>:<max_col><max_row>

| Cell | Value | Formula |
|------|-------|---------|
| A1   | Name  |         |
| B2   | 1500  | =SUM(B3:B10) |

Charts detected: yes | no
Pivot tables detected: yes | no

---

## Sheet: <next_sheet_name>
...
```

- `Value` column shows the cell's display value (as stored, not formatted)
- `Formula` column is populated only when the cell contains a formula; the raw formula string is shown (e.g. `=VLOOKUP(A2,Sheet2!A:C,3,0)`)
- Empty cells are omitted
- Sheet order matches workbook tab order

---

## Tools

- **Bash** — run a Python extraction script using `openpyxl`
- **Write** — write the scan output file

---

## Execution Steps

### Step 1 — Install dependency check

Run via Bash:
```bash
python3 -c "import openpyxl; print('ok')" 2>&1
```

If output is not `ok`, log failure and abort with status: failed. Note: `openpyxl` is a standard data-science dependency; install with `pip3 install openpyxl` if missing.

### Step 2 — Extract workbook content

Run via Bash (substitute `{excel_file}` and `{student_id}` with actual values):
```bash
python3 - <<'PYEOF'
import openpyxl, sys, re
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook("{excel_file}", data_only=False)
lines = []
lines.append(f"# Excel Scan: {student_id}")
lines.append(f"Source file: {excel_file}")
lines.append(f"Sheets found: {len(wb.sheetnames)}")
lines.append("")

for name in wb.sheetnames:
    ws = wb[name]
    lines.append("---")
    lines.append(f"## Sheet: {name}")

    if ws.min_row is None or ws.max_row is None:
        lines.append("(empty sheet)")
        lines.append("")
        continue

    min_col_ltr = get_column_letter(ws.min_column)
    max_col_ltr = get_column_letter(ws.max_column)
    lines.append(f"Used range: {min_col_ltr}{ws.min_row}:{max_col_ltr}{ws.max_row}")
    lines.append("")
    lines.append("| Cell | Value | Formula |")
    lines.append("|------|-------|---------|")

    for row in ws.iter_rows():
        for cell in row:
            if cell.value is None:
                continue
            addr = cell.coordinate
            val = str(cell.value) if not str(cell.value).startswith("=") else ""
            formula = str(cell.value) if str(cell.value).startswith("=") else ""
            if not val and not formula:
                continue
            lines.append(f"| {addr} | {val} | {formula} |")

    has_charts = len(ws._charts) > 0 if hasattr(ws, "_charts") else False
    has_pivots = len(ws._pivots) > 0 if hasattr(ws, "_pivots") else False
    lines.append("")
    lines.append(f"Charts detected: {'yes' if has_charts else 'no'}")
    lines.append(f"Pivot tables detected: {'yes' if has_pivots else 'no'}")
    lines.append("")

print("\n".join(lines))
PYEOF
```

Capture the output; it becomes the body of the scan file.

### Step 3 — Write scan file

Write captured output to `agents/excel-scanner/output/{student_id}-scan.md`.

Create the `agents/excel-scanner/output/` directory if it does not exist.

### Step 4 — Log and hand off

Append to `log/excel-scanner.log`:
```
[YYYY-MM-DD HH:MM] excel-scanner
  Input:   excel_file=[excel_file] student=[student_id]
  Output:  agents/excel-scanner/output/[student-id]-scan.md
  Status:  success | partial | failed
  Notes:   [number of sheets scanned, any sheets skipped]
```

Output the path on the final line:
```
output_path: agents/excel-scanner/output/[student-id]-scan.md
```

---

## Error Handling

| Condition | Action |
|-----------|--------|
| `openpyxl` not installed | Log status: failed. Print install instruction. Abort. |
| File not found | Log status: failed. Abort. |
| Password-protected file | Log status: failed. Note in log. Abort. |
| Empty sheet | Include sheet header with "(empty sheet)" note. Continue. |
| Sheet extraction error | Log sheet name, note error, skip sheet. Status: partial. |
