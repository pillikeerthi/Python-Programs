# sum of digits of a number
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n%10
        n //= 10        
    return sum

num = int(input("Enter a number: "))
print(f"Sum of digits of {num}:{sum_of_digits(num)}")