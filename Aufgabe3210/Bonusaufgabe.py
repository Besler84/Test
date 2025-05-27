limit = int(input("Bis zu welcher Zahl sollen die geraden Zahlen summiert werden? "))

sum = 0

for number in range(1, limit + 1):
    if number % 2 == 0:
        sum += number

print(f"Summe der geraden Zahlen von 1 bis {limit}: {sum}")