import random
num = input("select the range : ")
if num.isdigit():
    num = int(num)
    if num <= 0:
        print ("enter higher number than 0 ")
        exit()
else :
    print ("enter a number next time fuck off")
    exit()
ai = random.randint(0,num)
count = 1
while True:
    user = input (f"guess a number between (0-{num}) ")
    if user.isdigit():
        user = int(user)
    else :
        print("enter a number")
        continue
    if user == ai :
        print ("you have won against ai\nyou are great")
        if count > 1:
            print (f"you took {count} times")
        else :
            print (f"you took in one shot")
        break
    elif not int(user) > ai :
        print ("you are lower")
        count+=1
    else :
        print("you are higher")
        count+=1