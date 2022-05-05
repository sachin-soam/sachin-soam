from random import randrange


def rockPaperScissors(you, comp):
    if you==comp:
        return 0
    
    if (you=='r' and comp == 's'):
        return 1
    elif (you=='s' and comp == 'r'):
        return -1
    
    if (you=='s' and comp == 'p'):
        return 1
    elif (you=='p' and comp == 's'):
        return -1
    
    if (you=='p' and comp == 'r'):
        return 1
    elif (you=='r' and comp == 'p'):
        return -1

comp = randrange(0, 100)
you = input("Enter 'r' for rock 'p' for paper and 's' for scissor: ") 

number = randrange(0, 100) % 100 + 1
if (number < 33):
    comp = 'r'
elif (number > 33 and number < 66):
    comp = 'p'
else:
    comp = 's'
    
result = rockPaperScissors(you, comp)
if (you==comp):
    print("Drawn")
elif(result == 1):
    print("You Win")
else:
    print("You lose")
