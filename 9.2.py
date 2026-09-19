def difference(*args):
    if not args:
        return 0

    max_args = max(args)
    min_args = min(args)

    return round(max_args - min_args,2)

print(difference(1, 2, 3))
print(difference(5, -5))
print(difference(10.2, -2.2, 0, 1.1, 0.5))
print(difference())

print('OK')