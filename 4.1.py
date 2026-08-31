numbers = [1,0,3,7,0]
new_numbers = []
for number in numbers:
    if number != 0:
        new_numbers.append(number)
zore_count = numbers.count(0)

for i in range(zore_count):
    new_numbers.append(0)

print(new_numbers)
