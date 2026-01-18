#!/usr/bin/env python3
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 3:
        print("Usage: gen_index.py <output_dir> <CLASS1> [CLASS2 ...]", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(sys.argv[1])
    classes = sys.argv[2:]

    out_dir.mkdir(parents=True, exist_ok=True)
    index_path = out_dir / "index.html"

    items = []
    for cls in classes:
        pdf_name = "main.pdf"
        pdf_path = out_dir / pdf_name
        if pdf_path.exists():
            items.append((cls, pdf_name))
        else:
            # Skip classes without PDFs; Make already warned
            continue

    html = build_html(items)
    index_path.write_text(html, encoding="utf-8")
    print(f"Wrote {index_path}")


def prettify_class_name(cls: str) -> str:
    """
    Turn something like 'EENG4312' into 'EENG 4312'.
    Super dumb but good enough for course codes.
    """
    prefix = "".join(ch for ch in cls if not ch.isdigit())
    suffix = "".join(ch for ch in cls if ch.isdigit())
    if prefix and suffix:
        return f"{prefix} {suffix}"
    return cls


def build_html(items):
    # Build the list items
    if items:
        lis = []
        for cls, pdf in items:
            display = prettify_class_name(cls)
            lis.append(
                f'''      <li class="class-item">
        <div class="class-code">{display}</div>
        <div class="class-actions">
          <a href="{pdf}" class="primary-link">Open notes (PDF)</a>
        </div>
      </li>'''
            )
        list_html = "\n".join(lis)
    else:
        list_html = (
            '      <li class="class-item empty">No PDFs found. Did the build fail?</li>'
        )

    # Main HTML template
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Course Notes</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <style>
    :root {{
      color-scheme: dark light;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      background: radial-gradient(circle at top, #1e293b, #020617 55%);
      color: #e5e7eb;
    }}

    .shell {{
      max-width: 720px;
      width: 100%;
      background: rgba(15, 23, 42, 0.9);
      border-radius: 18px;
      border: 1px solid rgba(148, 163, 184, 0.35);
      box-shadow:
        0 24px 60px rgba(15, 23, 42, 0.85),
        0 0 0 1px rgba(15, 23, 42, 0.9);
      padding: 24px 22px 20px;
      backdrop-filter: blur(12px);
    }}

    header {{
      text-align: center;
      margin-bottom: 18px;
    }}

    h1 {{
      font-size: 1.6rem;
      margin: 0 0 4px;
      letter-spacing: 0.03em;
    }}

    .subtitle {{
      font-size: 0.9rem;
      color: #9ca3af;
    }}

    .class-list {{
      list-style: none;
      padding-left: 0;
      margin: 16px 0 0;
    }}

    .class-item {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      padding: 12px 14px;
      margin-bottom: 10px;
      border-radius: 12px;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(75, 85, 99, 0.7);
      transition: transform 0.12s ease-out, box-shadow 0.12s ease-out, border-color 0.12s;
    }}

    .class-item:hover {{
      transform: translateY(-1px);
      box-shadow: 0 10px 25px rgba(15, 23, 42, 0.9);
      border-color: rgba(129, 140, 248, 0.9);
    }}

    .class-item.empty {{
      justify-content: center;
      text-align: center;
      color: #9ca3af;
      border-style: dashed;
    }}

    .class-code {{
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      font-size: 0.95rem;
    }}

    .class-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}

    .primary-link {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 6px 12px;
      border-radius: 999px;
      background: linear-gradient(135deg, #4f46e5, #22c55e);
      color: #f9fafb;
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      border: 1px solid rgba(15, 23, 42, 0.75);
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.45);
      transition: filter 0.12s ease-out, transform 0.12s ease-out, box-shadow 0.12s ease-out;
      white-space: nowrap;
    }}

    .primary-link:hover {{
      filter: brightness(1.07);
      transform: translateY(-0.5px);
      box-shadow: 0 6px 18px rgba(37, 99, 235, 0.7);
    }}

    footer {{
      margin-top: 16px;
      font-size: 0.8rem;
      color: #6b7280;
      text-align: center;
    }}

    @media (max-width: 600px) {{
      .shell {{
        padding: 18px 16px 16px;
      }}
      .class-item {{
        align-items: flex-start;
      }}
      .class-code {{
        font-size: 0.9rem;
      }}
      .primary-link {{
        width: 100%;
        justify-content: center;
      }}
    }}

    /* Light mode fallback */
    @media (prefers-color-scheme: light) {{
      body {{
        background: radial-gradient(circle at top, #e5e7eb, #d1d5db 60%);
        color: #111827;
      }}
      .shell {{
        background: rgba(248, 250, 252, 0.96);
        border-color: rgba(148, 163, 184, 0.6);
        box-shadow:
          0 18px 40px rgba(15, 23, 42, 0.25),
          0 0 0 1px rgba(148, 163, 184, 0.5);
      }}
      .class-item {{
        background: #f9fafb;
        border-color: rgba(209, 213, 219, 0.9);
      }}
      .class-item.empty {{
        color: #6b7280;
      }}
      .subtitle {{
        color: #4b5563;
      }}
      footer {{
        color: #6b7280;
      }}
    }}
  </style>
</head>
<body>
  <div class="shell">
    <header>
      <h1>Course Notes</h1>
      <div class="subtitle">Latest PDFs, built from LaTeX via CI.</div>
    </header>

    <ul class="class-list">
{list_html}
    </ul>

    <footer>
      Notes compiled by <strong>Dylan Parks</strong>.<br />
      These notes are for study purposes only — no guarantees of correctness are made.<br /><br />

      <a href="https://github.com/BouwerMan/uni-notes"
        style="color:#93c5fd; text-decoration:none; font-weight:500;">
        View source on GitHub →
      </a><br /><br />
    </footer>
  </div>
</body>
</html>
"""


if __name__ == "__main__":
    main()
