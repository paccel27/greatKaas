def multitable():
	print ("Here's a multiplication table")

	print ("  ",end="")
	for i in range(1,11):
		l = str(i)
		l = l.rjust(5)
		print (l, end="")
	print()

	for i in range(1,11):
		l = str(i)
		l = l.rjust(4)
		print (l, end="")
		for j in range (1,11):
			k = str(i*j)
			k = k.rjust(3)
			print (k," ", end="")
		print ()

multitable()