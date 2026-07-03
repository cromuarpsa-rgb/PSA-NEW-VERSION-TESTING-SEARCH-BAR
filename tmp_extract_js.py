from pathlib import Path
p = Path(r'c:/Users/PHNID/Desktop/PSA Search system/app.py')
text = p.read_text(encoding='utf-8')
start = text.index("JS = r'''") + len("JS = r'''")
end = text.index("'''\n\n\ndef page_login")
print(text[start:end])
