def sodarefund():
	print ("You drink a lot of soda!")
	while True:
		try:
			bigbottles = int(input ("How many bottles larger than a litre have you bought?"))
			break
		except:
			print("That is not a valid input! Try using whole numbers. You cannot buy parts of a bottle")
	while True:
		try:
			littlebottles = int(input ("How many bottles one litre or smaller have you bought?"))
			break
		except:
			print("That is not a valid input! We already told you to use whole numbers!")

	bigbottles = float(bigbottles)
	littlebottles = float(littlebottles)
	returndeposit = (bigbottles * .25) + (littlebottles * .10)
	print ("Great news! you get $%.2f" % returndeposit)
	print ("Here are the variable types:")
	print (type(bigbottles))
	print (type(littlebottles))
	print ("Thanks!")

sodarefund()