# print ("Anagrams are fun!")
# word1 = sorted(list(input("Enter your first word: ")))
# word2 = sorted(list(input("Enter your second word: ")))

# print (word1)
# print (word2)

# if word1 == word2:
# 	print ("These words are anagrams")
# else:
# 	print ("Not anagrams. No such luck")

# # do as a dictonary.

print ("Anagrams are fun - especially as a dictionary.")
word1 = input("Enter your first word: ")
word2 = input("Enter your second word: ")

dict1 = {}
dict2 = {}

for letter in word1:
	if letter not in dict1:
		# letter not in dict1.keys():
		dict1[letter]=1
		print (dict1)
		
	else:
		dict1[letter] += 1

print(dict1)

for letter in word2:
	if letter not in dict2:
		dict2[letter]=1
		print (dict1)
		
	else:
		dict2[letter] += 1

print(dict2)

if dict1 == dict2:
	print ("Anagrams")
else:
	print ("Not anagrams")