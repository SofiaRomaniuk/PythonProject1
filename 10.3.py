def is_even(digit):
    """ Перевірка чи є парним число """
    if digit % 2 == 0:
        return True
    else:
        return False


print((is_even(2)))
print((is_even(5)))
print((is_even(0)))

print('OK')