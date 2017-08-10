print ("Roman Numberals")
arabicnumber = int(input ("Give me an arabic number: "))
romannumber = ''
factorlist = [1000,500,100,50,10,5,1]
letterlist = ['M',"D","C","L","X","V","I"]
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






	

