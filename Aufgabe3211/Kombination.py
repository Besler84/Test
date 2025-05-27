numbers = []

while True:
    feed = input("Gib eine Zahl ein (oder 'stop' zum Beenden): ")

    if feed.lower() == "stop":
        break

    try:
        number = int(feed)
        numbers.append(number)
    except ValueError:
        print("Ungültige Eingabe! Bitte eine ganze Zahl eingeben oder 'stop' schreiben.")

if numbers:
    smallest = numbers[0]
    largest = numbers[0]
    sum = 0

    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        sum += number

    average = round(sum / len(numbers), 2)

    print("\n--- Ergebnisse ---")
    print("Eingegebene Zahlen:", numbers)
    print("Kleinste Zahl:", smallest)
    print("Größte Zahl:", largest)
    print("Durchschnitt:", average)
    print("Liste sortiert (aufsteigend):", sorted(numbers))
else:
    print("Kein ganzzahliger Wert eingegeben.")