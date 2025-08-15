#Fibonacci series upto n terms
def fib_series(n):
    a,b = 0,1
    for _ in range(n):
        print(a, end=" ")
        a,b = b, a+b

num = int(input("Enter the number of terms: "))
print(f"Fibonacci series upto {num} terms:")
fib_series(num)
