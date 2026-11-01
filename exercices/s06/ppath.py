from pathlib import Path

abs = Path('example.txt')
contents = abs.read_text()


#lines = contents.splitlines()
#for line in lines:
#    print(line)