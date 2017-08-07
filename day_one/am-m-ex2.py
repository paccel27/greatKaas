def roomarea():
	print ("Congratulations on the purchase of your new house!")
	while True:
		try:
			roomwidth = float(input ("What is the width of your biggest room in meters? "))
			break
		except:
			print("That is not a valid input!")
	while True:
		try:
			roomlength = float(input ("What is the length of your biggest room in meters? "))
			break
		except:
			print("That is not a valid input!")

	area = roomwidth * roomlength
	print ("Wow! Your room is",area, "square meters!")
	print ("Here are the variable types:")
	print (type(roomlength))
	print (type(roomwidth))
	print ("Thanks!")

roomarea()

