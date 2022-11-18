#Final boss game (hardcore)

import random

name = input ("what is your name : ")
#            round - 0 
#             prologue
game_start = f"Enter the beast game {name} you have to defeat 001"
print (game_start)
boss = "001"
rang = 4
ai = random.randint(0,rang)
user = int(input(f"boss : {boss}\nenter number between(0-{rang}) : "))
def boss_chosen():
    print (f"{boss} chosen : {ai}")
boss_chosen()
if user == ai:
    pass
else :
    print (f"you can't win on me\niam the great {boss} among all!!")
    quit()
print ("you have defeated 001 but you have send him to upside down now 001 has become vecna and he has opened all gates to overworld now vecna is sending monster kill all the monster and save the world")
#           round - 1
r = 1
rang = 1
ai = random.randint(0,rang)
boss = "demobats"
user = int(input(f"round-{r}\n{boss}\nenter number between(0-{rang}) : "))
boss_chosen()
if user == ai:
    print (f"Congratulations,you have defeted your first boss {boss}")
else :
    print ("you lose!!")
    exit()
#          round - 2
r = 2
boss = "demodogs"
rang = 10
ai = random.randint(0,rang)
user = int(input(f"round-{r}\n{boss}\nenter number between(0-{rang}) : "))
boss_chosen()
if user == ai:
    print (f"you won!! on {boss}")
else :
    print ("you lose!!")
    quit() 
    
#           round - 3
r = 3
boss = "demogorgen"
rang = 20
ai = random.randint(0,rang)
user = int(input(f"round-{r}\n{boss}\nenter number between(0-{rang}) : "))
boss_chosen()
if user == ai:
    print (f"you won!! on {boss}")
else :
    print ("you lose!!")
    quit()
    
#          round - 4 
r = 4
boss = "mindflare"
rang = 30
ai = random.randint(0,rang)
user = int(input(f"round-{r}\n{boss}\nenter number between(0-{rang}) : "))
boss_chosen()
if user == ai:
    print (f"you won!! on {boss}")
else :
    print ("you lose!!")
    quit()
#          round - 5 
r = 5
rang = 50
boss = "vecna"
ai = random.randint(0,rang)
user = int(input(f"round - {r}\nhello, {name} welcome to upside down do you miss me \n enter number between(0-{rang}) : "))
boss_chosen()
if user == ai:
    print (f"no I can loss you are great {name} iam giving you my powers go save your world")
else :
    print ("no one can defeat me\niam vecna now iam more powerful than to think!!")
    quit()
