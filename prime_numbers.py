import time
Num = int(input("Enter a number:"))

if Num <= 1:
    print(f"{Num} is not a prime number")
elif Num == 2:
    print(f"{Num} is a prime number")
else:
    is_prime = True
    for i in range(2, Num):
        if Num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{Num} is a prime number")
    else:
        print(f"{Num} is not a prime number")