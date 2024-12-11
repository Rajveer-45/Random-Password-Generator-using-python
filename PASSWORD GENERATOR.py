import random
char = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
length=int(input("enter length: "))
password=""

for a in range(length):
    password+=random.choice(char)
print(password)