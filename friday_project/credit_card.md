Write a Python class to validate credit cards.

Using the Luhn Algorithm , also known as "modulus 10", we will be determining the validity of a given credit card number.
```
http://en.wikipedia.org/wiki/Luhn_algorithm
```


Use the skeleton of the `CreditCard` class:
```
class CreditCard:
    
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = 
        self.valid = 
```

We want our class to have its three main properties set on  - card_number, card_type, and valid.

If the card number given passes the Luhn algorithm, valid should be true and cardType should be set to 'VISA', 'AMEX', etc. If it does not pass, valid should be false and cardType should be set to "INVALID"

This way, we can do this:
```python
    myCard = CreditCard('347650202246884')

    myCard.valid ## true
    myCard.card_type ## 'AMEX'
    myCard.card_number ## '347650202246884'
```

There are three instance methods. You may perform these methods in the order you see fit.

`determine_card_type` should check whether or not the credit card has valid starting numbers and return the card type.

Visa must start with 4  
Mastercard must start with 51, 52, 53, 54 or 55  
AMEX must start with 34 or 37  
Discover must start with   

`check_length` should check whether or not a credit card number is a valid length.

Visa, MC and Discover have 16 digits  
AMEX has 15  

`validate` should run the Luhn Algorithm and return true or false.

The Algorithm

From the right most digit, double the value of every second digit. For example:

`4 4 8 5 0 4 0 9 9 3 2 8 7 6 1 6`

becomes

`8 4 16 5 0 4 0 9 18 3 4 8 14 6 2 6`

Now, sum all the individual digits together. That is to say, split any numbers with two digits into their individual digits and add them. Like so:

`8 + 4 + 1 + 6 + 5 + 0 + 4 + 0 + 9 + 1 + 8 + 3 + 4 + 8 + 1 + 4 + 6 + 2 + 6`

Now take the sum of those numbers and modulo 10.

80 % 10

If the result is 0, the credit card number is valid.

Keep your code super clean and DRY.

If you are repeating yourself, stop and think about how to better approach the problem.

