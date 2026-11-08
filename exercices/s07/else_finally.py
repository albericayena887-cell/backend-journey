try:
    n = int("42")
except ValueError:
    print("Conversion failed")
else:
    # runs ONLY if no exception was raised
    print(f"Got {n}")
finally:
    # ALWAYS runs, success or failure
    print("Cleaning up")