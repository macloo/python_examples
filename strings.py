# example of manipulating strings -- slices
# find parts of a string using variable[0:n]
# http://stackoverflow.com/questions/509211/explain-pythons-slice-notation

book = "The Fault in Our Stars"
movie = "The Theory of Everything"

word1 = book[0:4]
word2 = movie[0:4]
word3 = book[-5:]
word4 = movie[-10:]
word5 = book[17:22]
word6 = movie[14:24]

print word1
print word2
print word3
print word4
print word5
print word6

# -----------------------------------------------------------------------------
# practical application 1

# delete a dollar sign and use the numbers only
# maybe we extracted this total from a text document
total = "$123.56"

# chop off the dollar sign
new_total = total[1:]
with_tax = float(new_total) + float(new_total) * .06
print with_tax

# -----------------------------------------------------------------------------
# practical application 2

# delete punctuation at end of word
last_word = "cheese?"
new_last_word = last_word[0:-1]
print new_last_word

