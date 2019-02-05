from math import sqrt
from pprint import pprint as pp


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


pp([(i, is_prime(i)) for i in range(100)])

only_primes = [i for i in range(100) if is_prime(i)]
print ('Prime only')
pp(only_primes)

print("Prime Square Divisors")
prime_square_divisors = {x*x: (1, x, x*x) for x in range(101) if is_prime(x)}
pp(prime_square_divisors)
