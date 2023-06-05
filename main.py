import random
a=random.randint(1,100)
i=0
userguess=None
while (userguess!=a):
    try:
        userguess=int(input("enter your guess\n"))
    except Exception as e :
        print("that is not a valid number")
    else:
        i+=1
    
        if userguess<a:
            print("enter a higher number")
        elif userguess>a:
            print("enter a lower number")
        else:
            print(f"you guessed it right , it took you {i} tries")
    
    
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(i<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(i))
    