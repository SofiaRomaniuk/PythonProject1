number = int(input("Enter a number: "))

while number >=9:
     digit = str(number)
     number = 1

     for digit in digit:
         number*=10 + int(digit)


print(number)
