print ('Prime Numbers')

def testprime(testnumber):
	primeremainder = 1
	i = 1
	isaprime = 0
	
	while primeremainder != 0:
			i += 1
			primeremainder = testnumber % i
			print (i,primeremainder)
			if i == testnumber:
				print ("This is a prime Number")
				isaprime = 1
				return isaprime
			if primeremainder == 0 and i != testnumber:
				print ("Not a prime Number.")
				isaprime = 0 
				return isaprime


testnumber = input ("Enter a number for testing: ")
testnumber = int(testnumber)

if __name__ == "__main__":
	print ("Inside the main loop")

	if testprime(testnumber):
		print ("testprime tested true")
	else:
		print ("testprime tested false")
else:
	print ("Not the main program")
