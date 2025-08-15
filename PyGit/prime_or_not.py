#check if a number is prime or not
def prime_or_not(n):
    if n <= 1:
        return False
    for i in range(2, n+1):
        if n % i == 0:
            return True
    return False

num = int(input("Enter a number: "))    
print(num,"is a prime number" if prime_or_not(num) else "is not a prime number")