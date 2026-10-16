def bisextille(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        return f"{year} est bisextille"
    else:
        return f" Pas une année bisextille"


print(bisextille(2026))    