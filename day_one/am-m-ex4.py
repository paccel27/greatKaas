def isavowel1():
	print ("Let's talk about letters!")
	myletter = str(input("Enter a letter of the alphabet. "))
	myletter = myletter.lower()
	if myletter not in "abcdefghijklmnopqrstuvwxyz":
		print ("Liar! that's not a letter.")
	if myletter in 'aeiou':
		print ("That's a vowel!")
	elif myletter == 'y':
		print ("That's the letter y")
	elif myletter in "bcdfghjklmnpqrstvwxyz":
		print ("It's a consonant.")

isavowel1()