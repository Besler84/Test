def say_hello(first_name, last_name):
    message_lines = [
        f"Hallo {first_name} {last_name}",
        "Willkommen zurück"
    ]

    # Breite des Rahmens ermitteln
    max_length = max(len(line) for line in message_lines)
    border = "+" + "-" * (max_length + 2) + "+"

    # Ausgabe mit Rahmen
    print(border)
    for line in message_lines:
        print(f"| {line.ljust(max_length)} |")
    print(border)

say_hello("großer", "Meister")