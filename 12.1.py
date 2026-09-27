from inspect import isgenerator

def prime_generator(end):
        for n in range(2, end + 1):
            is_prime = True

            for divisor in range(2,n):
                if n % divisor == 0:
                    is_prime = False

            if is_prime:
                yield n


gen = prime_generator(1)
assert isgenerator(gen)
print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))

print('Ok')