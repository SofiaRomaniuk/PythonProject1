while True:
    num1 = float(input("Введіть перше число:"))
    operations = input("введіть дію (+,-,*,/): ")
    num2 = float(input("введіть друге число: "))

    if operations == "+":
         print(num1 + num2)
    elif operations == "-":
        print(num1 - num2)
    elif operations == "*":
        print(num1 * num2)
    elif operations == "/":
        print(num1 / num2)
    answer = input("Продовжити?")

    if answer != "yes":
        break
