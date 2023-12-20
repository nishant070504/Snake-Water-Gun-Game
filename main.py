import random
#Snake Water Gun or Rock Paper Scissors
def game(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None
    
    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False
#Computer chooses 
print("Comp Turn: Snake(s) Water(w) Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
#You choose
you = input("Your Turn: Snake(s) Water(w) Gun(g)?")
a = game(comp, you)
#Displaying what the computer and you chose 
print("computer chose", comp)
print("You chose", you)
#Displays the result
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You lose!")