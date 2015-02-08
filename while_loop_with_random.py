# while-loop for a game
# uses randint to generate a random number
# the random number is use to represent the force of your enemy's punch
# when you have been punched enough, you die

from random import randint

lives = 3
hits = 0

print "\nThis represents a fighting game:\n"

while lives > 0:
    punch = randint(1, 10)
    hits += punch
    if hits < 20:
        print "Force of enemy's punch:", punch
    else:
        lives -= 1
        hits = 0
        print "You died! You have %d lives left.\n" % lives

print "The game is over."
