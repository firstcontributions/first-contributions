def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == "__main__":
    n = int(input("Enter the length of the Fibonacci sequence: "))
    print(f"Fibonacci sequence of length {n}: {fibonacci(n)}")
#github.com/adityzkrmishra
