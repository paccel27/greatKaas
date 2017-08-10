print ("Board exercises.")
list1 = [1,8,9,2,3,-4,1,3,1,3,3,1]
fact1 = 5
fact1 = int(fact1)
import math


def maxinalist(list1):
	print ('Maximum value of the list is ', max(list1))
maxinalist(list1)

def sumalist(list1):
	print ('Sum of a list is ', sum(list1))
sumalist(list1)

def multalist(list1):
	listmulti = 1
	for number in list1:
		listmulti*= number 
	print ('Total multiplication of list is ', listmulti)
multalist(list1)

def factfunc(fact1):
	print (fact1,"factorial is", math.factorial(fact1) )
factfunc(fact1)


def uniquelist(list1):
		print ('Unique of list is: ', set(list1))
uniquelist(list1)


def evenlist(list1):
	evenlist = []
	for number in list1:
		if number % 2 == 0:
			evenlist.append(number)
	print ('Even numbers are: ', evenlist)
evenlist(list1)

def letsadd4():
	list4 = []
	for number in range(0,420,4):
		if (number < 25 or number > 399) and number >0 and number < 420:
			list4.append(number)
	print("Multiples of four, skipping 25 to 399", list4)
letsadd4()

def letsadd5():
	list5 = []
	for number in range(0,310,5):
		if number < 25 or number > 279 and number >0 and number < 310:
			if number % 10 != 0:
				list5.append(number)
	print("Multiples of five but not of 10, skipping 25 to 279", list5)
letsadd5()

def oddlist2():
	list2 = []
	for number in range(0,1000):
		list2.append(number*2+1)

	for number in range (len(list2)-11,len(list2)-1):
		print(list2[number])
oddlist2()


def evenlist2():
	list2 = []
	for number in range(1,1000):
		list2.append(number*2)
	for number in range (0,10):
		print(list2[number])
evenlist2()

def fizzbuzz():
	listfizbuzz = []
	for number in range(1,200):
		if number % 15 == 0:
			listfizbuzz.append("fizzbuzz")
		elif number % 5 == 0:
			listfizbuzz.append("buzz")
		elif number % 3 == 0:
			listfizbuzz.append("fizz")
		else:
			listfizbuzz.append(number)
	print (listfizbuzz)

fizzbuzz()

def isaprime(testprime):
	for number in range (2,testprime):
		if testprime % number == 0:
			#print ('not a prime')
			return
		elif number == testprime-1:
			#print ('is a prime')
			return True

	
testprime = int(input("Enter a number to test:"))

isaprime(testprime)

def makeprimeslist():
		primelist = []
		i = 1
		while len(primelist) < 100:
			if isaprime(i):
				primelist.append(i)
				i+=1
			else:
				i+=1

		print(primelist)

makeprimeslist()







