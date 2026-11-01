with open("names.csv") as fil:
    for line in fil:
        first_name, last_name, email = line.strip().split(",")
        print(f" Your first names is {first_name} and your mail is :  {email}")