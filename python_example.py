def greet_user(name):
    print(f"Hello, {name}! Welcome to First Contributions.")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def print_factorials_up_to(n):
    print(f"Factorials from 0 to {n}:")
    for i in range(n+1):
        print(f"{i}! = {factorial(i)}")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet_user(user_name)

    max_num = int(input("Enter a number to calculate factorials up to: "))
    print_factorials_up_to(max_num)
