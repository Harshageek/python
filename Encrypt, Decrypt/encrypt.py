#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet


files=[]
user = input("File name to encrypt: ")
for file in os.listdir():
	if file == user:
		pass
	else :
		continue
	files.append(file)
key = Fernet.generate_key()
with open("thekey.key","wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file,"rb") as thefile:
		co = thefile.read()
	en=Fernet(key).encrypt(co)
	with open(file,"wb") as thefile:
		thefile.write(en)
print(f"{files}\nThe file have be encrypted successfully")
