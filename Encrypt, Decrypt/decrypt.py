#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files=[]
user = input("file name to decrypt : ")
for file in os.listdir():
	if file == user:
		pass
	else :
		continue
	files.append(file)
with open("thekey.key","rb") as key:
	s_key = key.read()

for file in files:
	with open(file,"rb") as thefile:
		co = thefile.read()
	en=Fernet(s_key).decrypt(co)
	with open(file,"wb") as thefile:
		thefile.write(en)
if files==[]:
	print("Enter a valid file to encrypt")
else:
	print(f"{file}\nThe file have be decrypted successfully")
