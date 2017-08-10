print ("Roman Numberals")
arabicnumber = int(input ("Give me an arabic number: "))

def romannumerals(arabicnumber):

	romannumber = ""

	romannumber = 'M' * int(arabicnumber//1000)
	arabicnumber = arabicnumber - ((arabicnumber//1000) * 1000)
	print (romannumber)
	print (arabicnumber)

	romannumber = romannumber + ('D' * int(arabicnumber//500))
	arabicnumber = arabicnumber - ((arabicnumber//500) * 500)

	print (romannumber)
	print (arabicnumber)

	romannumber = romannumber + ('C' * int(arabicnumber//100))
	arabicnumber = arabicnumber - ((arabicnumber//100) * 100)

	print (romannumber)
	print (arabicnumber)

	romannumber = romannumber + ('L' * int(arabicnumber//50))
	arabicnumber = arabicnumber - ((arabicnumber//50) * 50)

	print (romannumber)
	print (arabicnumber)

	romannumber = romannumber + ('X' * int(arabicnumber//10))
	arabicnumber = arabicnumber - ((arabicnumber//10) * 10)

	print (romannumber)
	print (arabicnumber)
	romannumber = romannumber + ('V' * int(arabicnumber//5))
	arabicnumber = arabicnumber - ((arabicnumber//5) * 5)

	print (romannumber)
	print (arabicnumber)

	romannumber = romannumber + ('I' * int(arabicnumber//1))
	arabicnumber = arabicnumber - ((arabicnumber//1) * 1)

	print (romannumber)
	print (arabicnumber)




romannumerals(1234)







