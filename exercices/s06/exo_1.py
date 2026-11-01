with open("example.txt", "r") as ffile:
    content = ffile.readlines()
    chapter = content[:15]

with open("chapter_2.txt", "w") as ffile:
    ffile.writelines(chapter)    