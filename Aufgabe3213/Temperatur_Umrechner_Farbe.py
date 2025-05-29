import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

TABLE_COLOR = Fore.GREEN
HEADLINE_COLOR = Fore.YELLOW
WARNING_COLOR = Fore.RED
FEED_COLOR = Fore.YELLOW
END_COLOR = Fore.BLUE

def headline():
    titel = pyfiglet.figlet_format("Temperatur Umrechner")
    print(HEADLINE_COLOR + titel)

def show_menu():
    print(TABLE_COLOR + "\n     ╔══════════════════════════════════╗")
    print(TABLE_COLOR + "     ║        Temperatur-Optionen       ║")
    print(TABLE_COLOR + "     ╠════╦═════════════════════════════╣")
    print(TABLE_COLOR + "     ║ 1  ║ Celsius zu Fahrenheit       ║")
    print(TABLE_COLOR + "     ║ 2  ║ Fahrenheit zu Celsius       ║")
    print(TABLE_COLOR + "     ║ 3  ║ Beenden                     ║")
    print(TABLE_COLOR + "     ╚════╩═════════════════════════════╝")

def print_result(text):
    frame_width = 36
    content = f"Ergebnis: {text}"
    centered = content.center(frame_width - 2)
    print(TABLE_COLOR + "\n     ╔" + "═" * (frame_width - 2) + "╗")
    print(TABLE_COLOR + "     ║" + FEED_COLOR + centered + TABLE_COLOR + "║")
    print(TABLE_COLOR + "     ╚" + "═" * (frame_width - 2) + "╝")

def print_input_box(prompt_text):
    frame_width = 36
    centered = prompt_text.center(frame_width - 2)
    print(TABLE_COLOR + "\n     ╔" + "═" * (frame_width - 2) + "╗")
    print(TABLE_COLOR + "     ║" + centered + "║")
    print(TABLE_COLOR + "     ╚" + "═" * (frame_width - 2) + "╝")
    return input(FEED_COLOR + "     ➤ Eingabe: ")

def celsius_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_celsius(f):
    return (f - 32) * 5 / 9

def temp_calculator():
    while True:
        show_menu()
        choice = input(FEED_COLOR + "      ➤ Bitte Auswahl eingeben: ")

        if choice == "1":
            try:
                feed = print_input_box("Temperatur in Celsius eingeben")
                celsius = float(feed)
                fahrenheit = celsius_fahrenheit(celsius)
                print_result(f"{celsius:.2f}°C → {fahrenheit:.2f}°F")
            except ValueError:
                
                print()
                print(WARNING_COLOR + "     ❌ Ungültige Eingabe! Bitte eine Zahl angeben.")

        elif choice == "2":
            try:
                feed = print_input_box("Temperatur in Fahrenheit angeben")
                fahrenheit = float(feed)
                celsius = fahrenheit_celsius(fahrenheit)
                print_result(f"{fahrenheit:.2f}°F → {celsius:.2f}°C")
            except ValueError:
                
                print()
                print(WARNING_COLOR + "     ❌ Ungültige Eingabe! Bitte eine Zahl eingeben.")

        elif choice == "3":
            print(END_COLOR + "\n     👋 Programm beendet. Bis zum nächsten Mal!")
            break

        else:
            print()
            print(WARNING_COLOR + "      ⚠️  Ungültige Auswahl! Bitte 1, 2 oder 3 eingeben.")

headline()
temp_calculator()