def whattypeoftriangle():
	print ("Triangles are fun.")
	sidea = int(input("How long is side A? "))
	sideb = int(input("How long is side A? "))
	sidec = int(input("How long is side A? "))

	
	if (sidea==sideb) and (sideb==sidec):
		print ("Equilateral Triangle!")
	elif (sidea==sideb) or (sideb==sidec) or (sidea==sidec):
		print ("Neat - Isosceles.")
	elif (sidea!=sideb) and (sideb!=sidec):
		print ("Must be a scalene")

whattypeoftriangle()