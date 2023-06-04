def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = power(x, n // 2)
        return half_power * half_power
    else:
        half_power = power(x, n // 2)
        return x * half_power * half_power


base = 2
exponent = 5
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")
