user_input = "not a number"

try:
    n = int(user_input)
    print(f"You entered {n}")
except ValueError:
    print("That wasn't a valid number. Please try again")