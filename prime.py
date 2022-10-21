# Prime determination method
def Prime_series(number):
    for iter in range(2,number):
        if is_prime(iter) == True:
            print(iter,end = " ")
        else:
            pass

number = int(input("Enter the input Range : "))
is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )
Prime_series(number)
