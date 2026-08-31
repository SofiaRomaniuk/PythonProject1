import random

lenght = random.randint(1,10)

numbers = [random.randint(1,10) for i in range(lenght)]

new_numbers = [ numbers[0],numbers[2],numbers[-2] ]
print(numbers)
print(new_numbers)