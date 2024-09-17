def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def primes_in_range(start, end):
    return [num for num in range(start, end) if is_prime(num)]
start, end = 10, 100
print(f"Prime numbers between {start} and {end}:")
print(primes_in_range(start, end))