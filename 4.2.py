numbers = [0,2,0,3,4,6]
if len(numbers) == 0:
    result = 0
else:
    total = 0

    for i in range (0,len(numbers),2):
        total += numbers[i]

    result = total * numbers [-1]

print(result)