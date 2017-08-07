print("Hello World")
print("!")
a = "apple"
print (a)
ba = "big Apple"
print(ba)
bodacious_confuscious = 'ba'
print(bodacious_confuscious)
c = a[0:3]
d = "AaBbCcDdEeFf"
e = d[0::2]
print(e)
f=d[1::2]
print(f)
g=d[-1::-2]
print(g)
h = 7
i = 7.0
j = "7"
print (type (h))
print (type (i))
print (type (j))
total = str(h) + j
print (total)
total2 = int(j) + h
print (total2)
total3 = h + i
print (total3)
bugs = []
print (type(bugs))
bugs.append(h)
bugs.append(i)
bugs.append(j)
print (bugs)
bugs[2] = 77
print (bugs)
for number in bugs:
    print(number)
for bananna in bugs:
    print(bananna)
def shopping():
	shopping_list = ["Milk","Apples","Potatos"]
	newitem = input("What do you want to add? ")
	shopping_list.append(newitem)
	for item in shopping_list:
		print("do not forget"+item)
	for item in shopping_list:
		print("but forget",item)
shopping()
print("More examples")

def greetings():
	list_of_friends = ["Alvin","Bob","Chuck"]
	time = int(input("What time is it now? "))
	for name in list_of_friends:
		if time <7:
			print ("Hello", name, "Party starts at 7PM")
		elif time == 7:
			print ("Hello", name, "Party is starting right now")
		else:
			print ("Hello", name, "You are late.")

greetings()
def test1():
	nums = [1,2,3,4,5,6]
	sumNums = 0

	for num in nums:
		sumNums += num
	print (sumNums)
test1()

def test2():
	x = range(1,9)
	print (x)

test2()







