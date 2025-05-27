weight = float(input("Bitte das Gewicht in kg eingeben: "))
height = float(input("Bitte die Größe in Metern eingeben (z. B. 1.75): "))

bmi = weight / (height ** 2)

print(f"Ihr BMI beträgt: {bmi:.2f}")

if bmi < 18.5:
    print("Sie sind untergewichtig.")
elif 18.5 <= bmi < 25:
    print("Sie haben Normalgewicht.")
else:
    print("Sie sind übergewichtig.")