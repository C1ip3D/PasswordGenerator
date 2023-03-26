import random
import string
from passlib.hash import pbkdf2_sha256

length=int(input("How many characters do you want your password to be? "))

def generate_password(length=length):
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols
    
    password = ""
    for i in range(length):
        password += random.choice(all_chars)
    
    hashed_password = pbkdf2_sha256.hash(password, rounds=1, salt_size=2)
    
    return hashed_password

password = generate_password()
print(password)
again=input("Need another password? ")
again=again.replace(" ", "")
if again.lower()=='yes' or again.lower()=='y':
    password=generate_password()
    print(password)
else: 
    print("1 - Horrible")
    print("2 - Bad")
    print("3 - Ok")
    print("4 - Good")
    print("5 - Amazing")
    rate=input("Please rate this on a scale of 1-5")
    
    if rate==1:
        fb=input("Why was your experience horrible? ")
    elif rate==2:
        fb=input("Why was your experience bad? ")
    else:
    	fb=input("Is there anything else you would like to tell us? ")

                

