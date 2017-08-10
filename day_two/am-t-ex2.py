print ("Let's check for palindromes")
wordasalist = list(input("Enter a word or phrase: "))
maxlist = len(wordasalist)

print (wordasalist)
print (maxlist)

letter = 0
letter = int(letter)
print (type(letter))

while maxlist>0 and (wordasalist[letter] == wordasalist[maxlist-1]):
	print (wordasalist[letter],wordasalist[maxlist-1])
	maxlist -= 1
	letter += 1

if maxlist == 0:
	print("Must be a palindrome")
else:
	print ("Nope, sorry. Not a palindrome")
