from pathlib import Path
abs = Path("example.txt")

msg = "I love my girl \nI love my family"

abs.write_text(msg)