color = input("Bitte eine Ampelfarbe eingeben (rot, gelb, grün): ").lower()

if color == "rot":
    print("Stehen bleiben.")
elif color == "gelb":
    print("Bereit machen.")
elif color == "grün":
    print("Gehen.")
else:
    print("Ungültige Eingabe! Bitte rot, gelb oder grün eingeben.")
