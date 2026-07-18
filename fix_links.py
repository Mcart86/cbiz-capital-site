import re, glob

pages = ["index","about","contact","dscr-rental-loans","fix-and-flip","bridge-loans",
         "multifamily-loans","recent-loan-closings","blogs","faqs","404",
         "builders-risk-insurance","asset-based-lending"]

total_changes = 0
for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    original = content

    for page in pages:
        clean = "/" if page == "index" else f"/{page}"
        # href="page.html" or href="page.html#anchor"
        pattern = re.compile(r'href="' + re.escape(page) + r'\.html(#[^"]*)?"')
        def repl(m, clean=clean):
            anchor = m.group(1) or ""
            return f'href="{clean}{anchor}"'
        content = pattern.sub(repl, content)

    if content != original:
        changes = sum(1 for a,b in zip(original.split('href='), content.split('href=')) if a!=b)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{filepath}: updated")
        total_changes += 1

print(f"\nTotal files updated: {total_changes}")
