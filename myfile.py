#This is a Guess the Number game.
import random

guessesTaken = 0

print( 'Hello! what is your name? ' )
myName = input()

number = random.randint(1, 20)
print('well, ' + myName + ', I am thinking of a number between 1 and 20. ')

for guessesTaken in range(6):
