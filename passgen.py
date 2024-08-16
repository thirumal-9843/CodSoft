import random
import string

def password_generator(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters +=special

    pwd=""
    meets_requirements = False
    has_special = False
    has_number =  False

    while not meets_requirements or len(pwd) < min_length:
        new_characters =  random.choice (characters)
        pwd +=  new_characters

        if new_characters in digits:
            has_number = True
        elif new_characters in special:
            has_special = True

        meets_requirements =  True
        
        if numbers:
            meets_requirements = has_number
        if  special_characters:
            meets_requirements = meets_requirements and has_special

    return pwd

min_length = int(input("Enter the  Minimum length of the password: "))
has_number = input("Do you want to have numbers (y/n)?:").lower() == "y"
has_special = input("Do you  want to have special characters (y/n):").lower() == "y"
pwd  = password_generator(min_length,has_number,has_special)
                          
print("The generated password",pwd)
