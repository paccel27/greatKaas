# dictionary and extracting multiple variables
roman = {1000:'M',900:"CM"}

for i in roman:
	x,y = divmod(number,i)
	if x> 0:
		r += roman(i) * x
		number -= (i *x)

# dictionaries have two {key,values}
# for i, the first one, says go through the keys one at a time
# for the roman(i) that returns the values corresponding to that keys.

# note the x,y = divmod
# Divmod is very useful - gives both quotient and remainder

