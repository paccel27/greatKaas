print (ord('a'))
print (ord('A'))
print (ord('$'))
print()
for i in range (7,100,12):
	print(i)
am1 = 112341234123
print(am1)
print (type(am1))
am2 = str(am1)
print (type(am2))
print (am2)
print ()
print ('Lists are Mutable')
print ('Tuples are immutable')
tup1 = 1,2
print (type(tup1))
tup2 = 3,4
tuptotal = tup1 + tup2
print (tuptotal)
for i in tuptotal:
	print (i)
d = {}
print (type(d))

def shopping():
	shopping_list = {"Milk","Apples","Potatos"}
	len_of_list = len(shopping_list)
	cart = []

	while len_of_list >0:
		print(len_of_list)
		len_of_list -= 1 
		for item in shopping_list:
			print(item)
			if item not in cart:
				cart.append(item)
	print ("Cart",cart)

shopping()

def functionOne(a,b):
	total = a + b
	return total

def functiontwo(a,b):
	total = a - b
	return total

def main():
	sum_num = functionOne(5,7)
	sub_num = functiontwo(5,7)
	print (sub_num)
	print (sum_num)

if __name__ == "__main__":
	main()

# for check in range (2,number+1):
# 	if number % check == 0 and number != check:
# 		return False

x = 'string'
x.isalpha()
x.isdigit()


