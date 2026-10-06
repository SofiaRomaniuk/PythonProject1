from inspect import isgenerator

def generate_cube_numbers(end):
        number = 2

        while number **3 <= end:
            yield number ** 3
            number += 1



gen = generate_cube_numbers(1)
assert (gen)
print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(1000)))
