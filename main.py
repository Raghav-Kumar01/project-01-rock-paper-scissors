import random
# Encoding choices
'''
1 for rock 
-1 for paper
0 for scissors  
'''
computer = random.choice([1,-1,0])
user = input("Enter your choice-->")

# Mapping string to value
Gamedict  = {
    "rock":1,
    "paper":-1,
    "scissors":0
}

# Reverse map value to string (for display)
reversedict = {1:"rock", -1:"paper", 0:"scissors"}

yourchoice = Gamedict[user]

print(f"You enter:{reversedict[yourchoice]} \n computer enter:{reversedict[computer]}")

def ladder():
    if(yourchoice == computer):
        print("It's a tie!")
    else:
        if(computer == 1 and yourchoice == -1):
            print("You Win!)")
        elif(computer == 1 and yourchoice == 0):
            print("You lose!")
        elif(computer == -1 and yourchoice == 1):
            print("You lose!")
        elif(computer == -1 and yourchoice == 0):
            print("You Win!")
        elif(computer == 0 and yourchoice == 1):
            print("You Win!")
        elif(computer == 0 and yourchoice == -1):
            print("You lose!")
        else:
         print("Something Went wrong!!!!")
ladder()