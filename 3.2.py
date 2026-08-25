numbers = [1,2,3,4,5,6,]
if len(numbers) >1:
    numbers = numbers[-1:] + numbers[:-1]
print(numbers)

