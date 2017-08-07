def drawatriangle():
	uprange = range(1,5)
	dnrange = range(5,0,-1)
	stars = "*"
	for num in uprange:
		print ("*"* num)
	for num in dnrange:
		print ("*"* num)

drawatriangle()

def nicetriangle(number,character):
	character = str(character)
	for i in range(1,number+1):
		print (i*character)
	for i in range (number,1,-1):
		print (i*character)
	

nicetriangle(10,"%")