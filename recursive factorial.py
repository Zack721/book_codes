
def Factorial(n):
    result = n
    if n <= 1:
        return result
    return result * Factorial(n-1)

    



print(Factorial())