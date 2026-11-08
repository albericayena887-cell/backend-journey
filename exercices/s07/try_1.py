data = {"name": "Alice"}

# Style A: several types in one tuple
try:
    print(data["age"])              # KeyError
except (KeyError, IndexError):
    print("Couldn't find that")

# Style B: different actions for different errors
try:
    age = int(data["age"])
except KeyError:
    print("No age field")
except ValueError:
    print("Age wasn't a valid number")