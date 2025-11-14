import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

charlen = int(input("Enter the length of the password: "))
numlen =  int(input("Enter the number of numbers: "))
symlen =  int(input("Enter the number of symbols: "))
#password using easy method
password = ""
password2Temp=[]
#password using complex method
password2final=""

for i in range(0, charlen):
    password += random.choice(letters)
    password2Temp.append(random.choice(letters))

for i in range(0, numlen ):
    password += random.choice(numbers)
    password2Temp.append(random.choice(numbers))

for i in range(0, symlen):
    password += random.choice(symbols)
    password2Temp.append(random.choice(symbols))

print(password2Temp)
random.shuffle(password2Temp)
print(password2Temp)
for char in password2Temp:
    password2final+=char

print(f"Your random Password is : {password2final}")