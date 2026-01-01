def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_three_primes(num):
    """Check if a number can be expressed as sum of 3 prime numbers."""
    for p1 in range(2, num):
        if not is_prime(p1):
            continue
        for p2 in range(2, num - p1):
            if not is_prime(p2):
                continue
            p3 = num - p1 - p2
            if p3 >= 2 and is_prime(p3):
                return True, (p1, p2, p3)
    return False, None

# Example usage
number = 10
result, primes = sum_of_three_primes(number)
if result:
    print(f"{number} = {primes[0]} + {primes[1]} + {primes[2]}")
else:
    print(f"{number} cannot be expressed as sum of 3 primes")