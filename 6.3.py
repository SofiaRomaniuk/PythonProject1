number  = int(input("Enter a number: "))

while number >9:
    result = 1

    while number > 0:
         digit = number % 10
         result = result * digit
         number = number // 10

    number = result

print(result)
