def fib(n):

    """Function that creates Fibonacci sequence n times

    Args: n - an integer inputted by user


    Returns: Verbose return of sequence progress
    """

    a, b = 1, 1
    for i in range(n-1):
        print(a)
        a, b = b, a + b
    return a

def fibonacci(n):

    """Function that creates Fibonacci sequence until reaches n

    Args: n - an integer inputted by user

    Returns: Verbose return of sequence progress
    """

    a, b = 1, 1
    while (a < n - 1):
        print(a)
        a, b = b, a + b
    return a

integer = int(input("Enter number: "))

print(fib(integer))
print("\n")
print(fibonacci(integer))
