for item in 'Ahasun':
    print(item)


for item in ['md','Ahasun','haBib']:
    print(item)

for item in [10,12,3,6,7,8,12]:
    print(item)

for item in range(9):
    print(item)

for item in range(2, 10):
    print(item)

for item in range(2, 12, 3):
    print(item)

price = [10,30,5]
total = 0
for price in price:
    total += price
print(f"Total price is = ${total}")

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

number = [5,2,5,2,3]

for x_count in number:
    print('*' * x_count)
