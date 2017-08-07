def fizzbuzz():
	print ("Here's a range of numbers!")

	
	for num in range(1,100):
		if num%3 == 0 and num%5 ==0:
			print (num,"FizzBuzz")
		elif num%5 == 0:
			print (num,"Buzz")
		elif num%3 == 0:
			print (num,"Fizz")

fizzbuzz()