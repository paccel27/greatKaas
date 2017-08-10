print ("Roman Numberals")
arabicnumber = int(input ("Give me an arabic number: "))
romannumber = ''
factorlist = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
letterlist = ['M',"CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
arabroman = [arabicnumber,romannumber]

def roman1(arabroman,factor,letter):
	arabicnumber = arabroman [0]
	if arabroman[0] >= factor:
		arabroman[0] = arabroman[0] - ((arabicnumber//factor) * factor)
		arabroman[1] = arabroman[1] + (letter * int(arabicnumber//factor))
		return arabroman
	return arabroman

for i in range(0,len(factorlist)):
	arabroman = (roman1(arabroman,factorlist[i],letterlist[i]))

print (arabroman[1])






	

