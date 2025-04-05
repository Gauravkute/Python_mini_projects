import random
import string

lenght = int(input("Input lenght of password you want: "))

letters = string.ascii_letters  # a-zA-Z
digits = string.digits          # 0-9
symbols = string.punctuation    # !@#$%^&*()...

a = int(input("Enter the number of alphabets: "))
b = int(input("Enter the number of numbers: "))
c = int(input("Enter the number of special charater: "))
if(a+b+c!=lenght):
    print("Error!! number of lenght and number of letter , numbers and special character does not add up correctly")
else:
    password = []
    
password += random.choices(letters, k=a)
password += random.choices(digits, k=b)
password += random.choices(symbols, k=c)

random.shuffle(password)

final_Password = ''.join(password)

print("Password: ",final_Password)