def celsius_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_celsius(f):
    return (f - 32) * 5 / 9

def temp_calculator():
    print("Temperatur-Umrechner")

    while True:
        print("\nWählen Sie eine Option:")
        print("1 - Celsius zu Fahrenheit")
        print("2 - Fahrenheit zu Celsius")
        print("3 - Beenden")

        choice = input("Bitte Auswahl eingeben: ")

        if choice == "1":
            try:
                celsius = float(input("Geben Sie die Temperatur in Celsius ein: "))
                fahrenheit = celsius_fahrenheit(celsius)
                print(f"{celsius:.2f}°C entsprechen {fahrenheit:.2f}°F")
            except ValueError:
                print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
        
        elif choice == "2":
            try:
                fahrenheit = float(input("Geben Sie die Temperatur in Fahrenheit ein: "))
                celsius = fahrenheit_celsius(fahrenheit)
                print(f"{fahrenheit:.2f}°F entsprechen {celsius:.2f}°C")
            except ValueError:
                print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
        
        elif choice == "3":
            print("Programm beendet. Bis zum nächsten mal!")
            break

        else:
            print("Ungültige Auswahl! Bitte 1, 2 oder 3 eingeben.")

temp_calculator()