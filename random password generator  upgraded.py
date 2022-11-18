import random

a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "0123456789"
d = ".;'[!@#$%^&*()]-=`\>"

all = a + b + c + d

length = int(input("length : "))

password = "".join(random.sample(all,length))

print(password)