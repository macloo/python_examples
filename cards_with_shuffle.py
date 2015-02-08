# build a deck of cards, copy it, shuffle it
# draw two cards off the top of the deck, compare them
# update scores for two players

# shuffle can randomly re-order all items in a list
from random import shuffle

# -----------------------------------------------------------------------------
# Step 1 to build a full deck of cards

suits = ["C", "D", "H", "S"] # Clubs, Diamonds, Hearts, Spades
ranks = []

# here 1 represents an Ace, 11 - Jack, 12 - Queen, 13 - King 
for r in range(1, 14):
    ranks.append(r)

print "Ranks:", ranks
print "Suits:", suits

# -----------------------------------------------------------------------------
# Step 2 to build the deck uses TWO for-loops, one inside the other
# the second loop runs through all the numbers in ranks
# it does that 4 times, once for each item in suits

# create a new empty list
cards = []

for suit in suits:
    for rank in ranks:
        card_value = str(rank) + suit  # str() changes int to string
        cards.append(card_value)

# number of cards in the deck
print "Number of cards:", len(cards)

# -----------------------------------------------------------------------------
# now we have 52 different cards, in cards
# we cannot do 'deck = cards' -- that does NOT create a NEW deck
#           instead, it would make deck and cards the same
#           changes to deck would affect cards also
# copy the list, cards, so we do not destroy it
deck = []
for card in cards:
    deck.append(card)

# put all the cards in random order - shuffle was imported at top
shuffle(deck)

# prove that deck and cards are NOT the same now
print
print "Deck is now shuffled:"
print deck
print
print "Cards remains unchanged:" 
print cards
print

# -----------------------------------------------------------------------------
def draw_card():
    # remove the first card
    user_card = deck.pop(0)
    # remove the (new) first card
    opponent_card = deck.pop(0)
    
    print "Your card:", user_card
    print "Opponent's card:", opponent_card
    
    # chop off the suit letter at end
    # NOTE: variable[0:n] gets letters from any string
    # :-1  means "the next-to-last character"
    user_number = user_card[0:-1]
    # chop off the suit letter at end
    opp_number = opponent_card[0:-1]
    
    # returns two strings that contain only numeric characters
    return user_number, opp_number

def compare_two():
    # get the two values from the draw_card() function
    u, o = draw_card()
    
    # change them both to ints and find the larger one
    if int(u) > int(o):
        print "User wins."
    elif int(o) > int(u):
        print "Opponent wins."
    else:
        print "It's a tie!"
    
    # returns two True or False values
    return int(u) > int(o), int(o) > int(u)


# call the function and update the two scores
# NOTE: we did not declare these scores before now
user_score, opponent_score = compare_two()


# number of cards in the deck
print "Number of cards left:", len(deck)
print "You: %d  Opponent: %d" % (user_score, opponent_score)
print


