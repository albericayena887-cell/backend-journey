from datetime import date

today = date.today().isoformat()

with open("journal.txt", "a", encoding="utf-8") as file:
    file.write(f"{today}: Practiced writing files in Python.\n")