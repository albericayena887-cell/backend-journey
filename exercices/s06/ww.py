with open("example.txt", "a") as fil:
    fil.write("\nI'm Roussel")

with open("example.txt", "r") as fil:
    contents = fil.read()
print(contents)