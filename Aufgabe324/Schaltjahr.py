year = int(input("Bitte ein Jahr eingeben: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "ist ein Schaltjahr.")
else:
    print(year, "ist kein Schaltjahr.")
