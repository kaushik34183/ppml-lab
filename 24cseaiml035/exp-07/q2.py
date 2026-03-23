def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

m = int(input("Enter m: "))
n = int(input("Enter n: "))
primes = [num for num in range(m, n + 1) if is_prime(num)]
print("Prime numbers from", m, "to", n, ":", primes)
