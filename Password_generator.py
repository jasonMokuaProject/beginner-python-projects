# Password generator
import random
import string

arry_pass = []

# Function that generates password
def Generate_password(minimal_limit):
            x=0
            while x <minimal_limit:
                chosenChar =""
                random_string = random.randint(0,len(string.ascii_letters) -1)
                random_digit = random.randint(0, len(string.digits) - 1)
                random_punctuation = random.randint(0,len(string.punctuation)-1)
                random_char = random.randint(0,2)
                match random_char:
                    case 0:
                        chosenChar =string.ascii_letters[random_string]
                    case 1:
                        chosenChar = string.digits[random_digit]
                    case 2:
                        chosenChar = string.punctuation[random_punctuation]




                x +=1
                arry_pass.append(chosenChar)
Generate_password(23)
print("".join(arry_pass))