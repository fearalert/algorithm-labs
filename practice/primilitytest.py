import random

def is_prime(n, k):
    # Check for small prime numbers
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Repeat the primality test k times
    for _ in range(k):
        a = random.randint(2, n - 2)

        # Compute (a ^ (n-1)) % n using modular exponentiation
        x = pow(a, n - 1, n)

        # If the result is not 1, n is composite
        if x != 1:
            return False

    # If the number passes all tests, it is likely prime
    return True

number = 563
confidence = 5

if is_prime(number, confidence):
    print(number, "is probably prime.")
else:
    print(number, "is composite.")
