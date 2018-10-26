#import random
import secrets
#min = 1
#max = 6
foo = ['1','2','3','4','5','6']
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
#    print (random.randint(min, max))
#    print (random.randint(min, max))
    print (secrets.choice(foo))
    roll_again = input("Roll the dices again?")