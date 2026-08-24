#перший випадок
numbers = [1,2,3,4,5,6,]

if len(numbers) == 0:
    result = [[],[]]
else:
    middle = (len(numbers) + 1) //2
    result = [numbers[:middle],numbers[middle:]]

print(result)

#другий випадок
numbers = [1,2,3]

if len(numbers) == 0:
    result = [[],[]]
else:
    middle = (len(numbers) + 1) //2
    result = [numbers[:middle],numbers[middle:]]
print(result)

#третій випадок
numbers = [1,2,3,4,5]
if len(numbers) == 0:
    result = [[],[]]
else:
    middle = (len(numbers) + 1) //2
    result = [numbers[:middle],numbers[middle:]]
print(result)

#четвертий випадок
numbers = [1]
if len(numbers) == 0:
    result = [[],[]]
else:
    middle = (len(numbers) + 1) //2
    result = [numbers[:middle],numbers[middle:]]
print(result)

#п'ятий випадок
numbers = [0]
if len(numbers) == 0:
    result = [[],[]]
else:
    middle = (len(numbers) + 1) //2
    result = [numbers[:middle],numbers[middle:]]
print(result)
