with open("names.csv") as file:
    contents = file.readlines()
    chap = contents[1:]
    for line in chap:
        print(line.strip().replace(",", "__"))