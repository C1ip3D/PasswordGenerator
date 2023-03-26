import random
import string

length=int(input("How many characters do you want your password to be? "))

def generate_password(length=length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols
    
    password = ""
    for i in range(length):
        password += random.choice(all_chars)
    
    return password

password = generate_password()
print(password)
again=input("Need another password? ")
again=again.replace(" ", "")
if again.lower()=='yes' or again.lower()=='y':
    password=generate_password()
    print(password)
else: 
    rate=input("Please rate this on a scale of 1-5")
    print("1 - Horrible")
    print("2 - Bad")
    print("3 - Ok")
    print("4 - Good")
    print("5 - Amazing")
    if rate==1:
        fb=input("Why was your experience horrible")
    elif rate==2:
        fb=input("Why was your experience bad")
    else:
    	fb=input("Is there anything else you would like to tell us")

                
