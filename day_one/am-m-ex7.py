def evenorodd():
	print ("Let's try some numbers.")
	guess = int(input ("Enter a number, my friend: "))

	if guess%2 == 0:
		print ("It's even!")
	elif guess%2 == 1:
		print ("It's an odd number.")


evenorodd()