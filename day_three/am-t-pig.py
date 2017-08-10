print ("Pig Latin")
englishword = input ("Enter your word: ")


def piglatin(englishword):
	vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
	if englishword[0] in vowels:
		pigword = englishword + 'yay'
		print (pigword)

	else:
		for letter in englishword:
			if letter in vowels:
				i = englishword.find(letter)
				break

		pigword = englishword[i:] + englishword[:i] + 'ay'
		print (pigword)

piglatin(englishword)

