import random

options = ['rock', 'papper','scissors']

cpuValue = random.choice(options)
#print(cpuValue)

on_off=True

while on_off:
    usrValue = input ("Enter with the item : ").lower()
    print ("Cpu:" +str(cpuValue))
    print ("Player:" +str(usrValue))
    if (usrValue in options):
        if usrValue == cpuValue:
            print("Tie!")
        else:
            if usrValue == "rock":
                if cpuValue =="scissors":
                    print("you win")
                else:
                    print("you lose")
            elif usrValue =="papper":
                if cpuValue=="rock":
                    print("you win")
                else:
                    print("you lose")
            elif usrValue =="scissors":
                if cpuValue=="papper":
                    print("you win")
                else:
                    print("you lose")             
        control = input("do you want continue the game (y/n)") .lower() 
        while control != 'n' and control!='y':
            control = input("Incorrect enterie. Do you want continue the game (y/n)")
        if control=="n":
            on_off = False
    else:
        print ("enter with correct items")
print("Bye!")




