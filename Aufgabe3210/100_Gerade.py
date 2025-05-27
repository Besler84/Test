sum = 0

for number in range(1, 101):
    if number % 2 == 0:
        sum += number

print("Summe der geraden Zahlen von 1 bis 100:", sum)