'''
Dice Roll Generator
-------------------------------------------------------------
'''


import random
import os


def num_die():
  while True:
      try:
          num_dice = input('Number of dice: ')
          valid_responses = ['1', 'one', 'two', '2']
          if num_dice not in valid_responses:
              raise ValueError('1 or 2 only')
          else:
              return num_dice
      except ValueError as err:
          print(err)


def roll_dice():
   min_val = 1
   max_val = 6
   roll_again = 'y'

   while roll_again.lower() == 'yes' or roll_again.lower() == 'y':
       os.system('cls' if os.name == 'nt' else 'clear')
       amount = num_die()

       if amount == '2' or amount == 'two':
           print('Rolling the dice...')
           dice_1 = random.randint(min_val, max_val)
           dice_2 = random.randint(min_val, max_val)

           print('The values are:')
           print('Dice One: ', dice_1)
           print('Dice Two: ', dice_2)
           print('Total: ', dice_1 + dice_2)

           roll_again = input('Roll Again? ')
       else:
           print('Rolling the die...')
           dice_1 = random.randint(min_val, max_val)
           print(f'The value is: {dice_1}')

           roll_again = input('Roll Again? ')


if __name__ == '__main__':
   roll_dice()
