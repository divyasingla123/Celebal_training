
units = int(input())

if units <= 100:
    bill = units * 3
elif units <= 200:
    bill = 300 + (units - 100) * 5
else:
    bill = 800 + (units - 200) * 8

if units > 300:
    bill += bill * 0.10

print(int(bill))
