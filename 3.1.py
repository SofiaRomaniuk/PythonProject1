
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
 if num1 == 0 or num2 == 0 :
    print("неможливо поділити на 0")
 else:
  result = num1 / num2
  print("результат", result)


