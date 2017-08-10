# x = ['Colonel Mustard','Mrs. Scarlet','Professor Plum','Dr. Watson']
# y = ['library','drawing room','kitchen']


# l1 = list(zip(x,y))

# print (l1)

# addresses = [['New York','NY'],['Boston','MA'],['Los Angeles','CA']]

# city,state = list(zip(*addresses))

# print (city)
# print (state)

# grid = []

# for i in range(0,len(x)):
# 	for j in range(0,len(y)):
# 		grid.append([x[i],y[j]])

# print (grid)


# testlist = [1,3,5,7,9,2,4,6,8,0]
# print (testlist)
# print (sorted(testlist))
# print (testlist)
# print (testlist.sort())
# print (testlist)

# print (slice(testlist[2:4]))


import datetime

# print(dir(datetime))

# print (date.today)
# print (date.dayofweek)
# print (date.day)
# print (date.month)

### Cycle

class sales():

	salesmen = 0
	bob = "bob"
	rutabaga = [1,2,3,4]
	def __init__ (self,name,address,phone):
		self.name = name
		self.address = address
		self.phone = phone
		sales.salesmen += 1

		def name(self):
			return self.name

		def address(self):
			return self.address

		def __str__(self):
			return "Eat my shorts"

customer = sales('Andrew','NYC','12345')

vendor = sales('Microsoft','NYC','12345')
	
# print (customer.bob)
print (customer.name)
print (customer.bob)
print (customer.rutabaga)
print (customer.salesmen)
print (sales)


