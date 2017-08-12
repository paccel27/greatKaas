class CreditCard:
    
    def __init__(self, card_number):
    	#pass
        self.card_number = card_number
        # attributes assigned from other methods will call those methods in the order listed here in __init__
        self.check_length = self.check_length()
        #if self.check_length():
        self.card_type = self.card_type()
            #if self.card_type != None:
        self.card_valid = self.validate()
        
    	# write your code here
    def check_length(self):
        if len(self.card_number) != 15 and len(self.card_number) != 16:
            print("Invalid # of credit card digits!")
            #prompt user to try again, maybe use generator to stop after 3 tries?
            return False
        else: 
            return True
     
    def card_type(self):
        if self.check_length:
            if self.card_number[0] == '4': 
                return 'Visa'
            elif self.card_number[0] == '5':
                if int(self.card_number[1]) in range(1,6):
                    return 'Mastercard'
            elif self.card_number[0:2] == '34' or self.card_number[0:2] == '37':
                return 'AMEX'
            elif self.card_number[0:4] == '6011' or self.card_number[0:2] == '65':
                return 'Discover'
            else:
                print("Invalid credit card type!")
                return 
    
    def validate(self):
        #loop over each element in string and convert to integer. Place them in a list
        if self.card_type:
            card_int = []
            for i in self.card_number:
                card_int.append(int(i))
        # Step 1 of Luhn's algorithm: Start from the end and double each digit.
            for digit in range(len(card_int)-2,-1,-2):
                card_int[digit] *= 2
                # Step 2: If the doubling gives a 2-digit no., then add the digits.  
                # Shortcut: This is equivalent to subtracting 9
                if card_int[digit] >= 10:
                    card_int[digit] -= 9
            # Step 3: Add add the numbers in the card_int list
            j = sum(card_int)
            if j%10 == 0:
                print("Valid ", self.card_type, "card")
                return True
            else:
                print("Invlaid credit card number!")
                return False





# #do not modify assert statements

# cc = CreditCard('9999999999999999')

# assert cc.valid == False, "Credit Card number cannot start with 9"
# assert cc.card_type == "INVALID", "99... card type is INVALID"

# cc = CreditCard('4440')

# assert cc.valid == False, "4440 is too short to be valid"
# assert cc.card_type == "INVALID", "4440 card type is INVALID"

# cc = CreditCard('5515460934365316')

# assert cc.valid == True, "Mastercard is Valid"
# assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

# cc = CreditCard('6011053711075799')

# assert cc.valid == True, "Discover Card is Valid"
# assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

# cc = CreditCard('379179199857686')

# assert cc.valid == True, "AMEX is Valid"
# assert cc.card_type == "AMEX", "card_type is AMEX"

# cc = CreditCard('4929896355493470')

# assert cc.valid == True, "Visa Card is Valid"
# assert cc.card_type == "VISA", "card_type is VISA"

# cc = CreditCard('4329876355493470')

# assert cc.valid == False, "This card does not meet mod10"
# assert cc.card_type == "INVALID", "card_type is INVALID"

# cc = CreditCard('339179199857685')

# assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
# assert cc.card_type == "INVALID", "card_type is INVALID"
