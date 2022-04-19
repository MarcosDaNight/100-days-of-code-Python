def prime_check(num):
    if num <= 1:
        return "It's not a prime number."
    is_prime = True
    for i in range (2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        return("It's a prime number.")
    else:
        return("It's not a prime number.")

while True:
    num = int(input())
    print(prime_check(num))
