numbers = [1,2,3,4]         #перший випадок
if len(numbers) >1:
    numbers = numbers[-1:] + numbers[:-1]
print(numbers)

#другий випадок
numbers = [1]
if len(numbers) >1:
    numbers = numbers[-1:] + numbers[:-1]
print(numbers)

#третій випадок
numbers = []
if len(numbers) >1:
    numbers = numbers[-1:] + numbers[:-1]
print(numbers)

#четвертий випадок
numbers = [1,2,3,4,5]
if len(numbers) >1:
    print(numbers)