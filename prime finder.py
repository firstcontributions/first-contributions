def prime():
	n = eval(input("Please enter a number for testing primescy: "))
	count = 2
	while count <= sqrt(n):
		if n % count == 0:
			print("This number isn't a prime number")
			break
		count = count +1
	if n % count !=0:
		print('This number is a prime number')
