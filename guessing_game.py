import random 

#Function to set the no. of turns according to diffiulty level
def set_difficulty() :
    choice = input("Choose difficulty\nType hard or easy  : ")
    choice = choice.lower()
    if choice == 'hard' :
        print("You have 5 attempts to guess the number")
        return  5
    elif choice == 'easy':
        print("You have 10 attempts to guess the number")

        return 10
    else :
        print("Invalid entry please enter a right option")
        
        
#Function to check user guess against actual answer
def check_answer(choice,random_choice,chance):
    
    if choice > random_choice :
        print("Too high guess")
        chance = chance - 1
        print(f"You have {chance} attempt remaning to guess the number")
        return chance

        
    elif choice < random_choice :
        print("Too low guess")
        chance = chance - 1 
        print(f"You have {chance} attempt remaning to guess the number")
        return chance

    else :
        print("Right guess")
        print(f"You won .The answer was {random_choice}")
       
def game() :
    #chossing a random number
    print("Welcome to the number guessing game !")
    print("I am thinking a number between  1 and  100 ") 
    random_choice = random.randint(1,100)
    chance = set_difficulty()
    choice=-1
   
    while  random_choice !=choice :
        #Let the user guess a number      
        
        choice = int(input("Make guess : "))
        
        #track the no. of turns left 
        chance = check_answer(choice,random_choice,chance)

        if chance ==0 :
            print("You have run out the chances ,You lose")
            print(f"The right guess is  {random_choice}")
            break 
              
game()
#Asking from user to  play again  
will=True
while will :        
    x=input("You want to play again ? Type yes/no :")
    x.lower()
    if x=='yes' :
        game()
    else :
        will = False
    
        




 
