#import the necessary modules!
import random 
import string

print('hello, Welcome to password generator!')

#input the length of password
length = int(input('\nEnter the length of the password: '))

#define data 
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#string.ascii_letter

#combine the data 
all = lower + upper + num + symbols

#use random
temp = random.sample(all,length)

#create the password
password = "".join(temp)

#print the password
print(password)

