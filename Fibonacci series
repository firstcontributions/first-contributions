# Program to print Fibonacci series
# Contributed by Sai Karthik

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series


print("First 10 Fibonacci numbers:", fibonacci(10))
