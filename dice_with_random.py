# this dice game is not the greatest, but it runs and 
# can be used a basis for a better dice game 

from random import randint

score = 0
again = "y"

print # blank line

def dice(score, again):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    roll = d1 + d2
    if roll == 7:
        print "Rolled %d and %d. You lose." % (d1, d2)
        again = "n"
    else:
        score += roll
        print "Rolled %d." % roll,
        again = raw_input("Roll again? y/n ")
    return score, again

while again != "n":
    score, again = dice(score, again)

print "Game over! Final score:", score
print
