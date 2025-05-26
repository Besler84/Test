e = float(input("Bitte den Einkaufswert in Euro eingeben: "))

if e > 100:
    discount = e * 0.10
    price = e - discount
    print(f"Es gibt 10 % Rabatt ({discount:.2f} €).")
else:
    end = e
    print("Kein Rabatt.")

print(f"Der zu zahlende Betrag beträgt: {price:.2f} €")