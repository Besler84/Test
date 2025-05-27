import random

number = random.randint(1, 100)
tries = 0
guess = False

print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Finde herraus welche es ist.")

while not guess:
    try:
        hint = int(input("Dein Tipp: "))
        tries += 1

        if hint < 1 or hint > 100:
            print("Bitte gib eine Zahl zwischen 1 und 100 ein.")
        elif hint < number:
            print("Zu niedrig!")
        elif hint > number:
            print("Zu hoch!")
        else:
            print(f"Richtig! Du hast die Zahl nach {tries} Versuchen erraten.")
            guess = True
    except ValueError:
        print("Bitte gib eine gültige ganze Zahl ein.")