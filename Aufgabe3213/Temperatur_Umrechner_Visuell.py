import pyfiglet

def headline():
    titel = pyfiglet.figlet_format("Temperatur Umrechner")
    print(titel)

def show_menu():
    print("\n     ╔══════════════════════════════════╗")
    print("     ║        Temperatur-Optionen       ║")
    print("     ╠════╦═════════════════════════════╣")
    print("     ║ 1  ║ Celsius zu Fahrenheit       ║")
    print("     ║ 2  ║ Fahrenheit zu Celsius       ║")
    print("     ║ 3  ║ Beenden                     ║")
    print("     ╚════╩═════════════════════════════╝")

def print_result(text):
    frame_width = 36
    content = f"Ergebnis: {text}"
    centered = content.center(frame_width - 2)
    print("\n     ╔" + "═" * (frame_width - 2) + "╗")
    print("     ║" + centered + "║")
    print("     ╚" + "═" * (frame_width - 2) + "╝")

def print_input_box(prompt_text):
    frame_width = 36
    centered = prompt_text.center(frame_width - 2)
    print("\n     ╔" + "═" * (frame_width - 2) + "╗")
    print("     ║" + centered + "║")
    print("     ╚" + "═" * (frame_width - 2) + "╝")
    return input("     ➤ Eingabe: ")

def celsius_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_celsius(f):
    return (f - 32) * 5 / 9

def temp_calculator():
    while True:
        show_menu()
        choice = input("      ➤ Bitte Auswahl eingeben: ")

        if choice == "1":
            try:
                feed = print_input_box("Temperatur in Celsius eingeben")
                celsius = float(feed)
                fahrenheit = celsius_fahrenheit(celsius)
                print_result(f"{celsius:.2f}°C → {fahrenheit:.2f}°F")
            except ValueError:
                print("     ❌ Ungültige Eingabe! Bitte eine Zahl angeben.")

        elif choice == "2":
            try:
                feed = print_input_box("Temperatur in Fahrenheit angeben")
                fahrenheit = float(feed)
                celsius = fahrenheit_celsius(fahrenheit)
                print_result(f"{fahrenheit:.2f}°F → {celsius:.2f}°C")
            except ValueError:
                print("     ❌ Ungültige Eingabe! Bitte eine Zahl eingeben.")

        elif choice == "3":
            print("\n     👋 Programm beendet. Bis zum nächsten Mal!")
            break

        else:
            print("     ⚠️ Ungültige Auswahl! Bitte 1, 2 oder 3 eingeben.")

headline()
temp_calculator()