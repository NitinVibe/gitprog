for i in range(2, 50):
    is_prime = True  # Assume the number is prime initially
    for j in range(2, int(i**0.5) + 1):  # Optimized loop up to the square root of i
        if i % j == 0:
            is_prime = False  # Found a divisor, so it's not prime
            break  # No need to check further divisors for this number
    if is_prime:
        print(i, "is a prime number")

print("byy byy !")