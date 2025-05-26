a = float(input("Bitte die erste Zahl eingeben: "))
b = float(input("Bitte die zweite Zahl eingeben: "))
c = float(input("Bitte die dritte Zahl eingeben: "))

if (a < b < c) or (c < b < a):
    print("Die zweite Zahl liegt zwischen der ersten und der dritten.")
else:
    print("Die zweite Zahl liegt nicht zwischen der ersten und der dritten.")
