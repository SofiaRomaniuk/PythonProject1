
num1 = float(input("введіть перше число: "))
operations = input("введіть дію (+,-,*,/): ")
num2 = float(input("введіть друге число: "))

if operations == "+":
    result = num1 + num2
elif operations == "-":
    result = num1 - num2
elif operations == "*":
    result = num1 * num2
elif operations == "/":
    result = num1 / num2
else:
    result = "невідома дія"

print("результат:", result)


