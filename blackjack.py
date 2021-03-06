import random
import sys

version = "0.0.1"

deck=[]
for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
	for suit in ["H", "D", "C", "S"]:
		deck.append("%s of %s" % (rank, suit))

print """Hello and Welcome to version %s of PyJack, by Micah Weitzman. 
Feel free to fork this project on GitHub!
Enjoy!""" % (version)


def handVal(hand):
	value=0
	aces=0
	for card in hand:
		for x in range(2,11):
			if card.startswith(str(x)):
				value+=x
		for x in ["J", "Q", "K"]:
			if card.startswith(x):
				value+=10
		if card.startswith("A"):
			aces=1
			value+=1
	other = value + 10 * aces
	if (other > 21):
		return value
	else:
		return other

player_card_first = random.choice(deck) 
deck.remove(player_card_first)

player_card_second = random.choice(deck)
deck.remove(player_card_second)

hand = [player_card_first, player_card_second]

hValue = handVal(hand)

print "Dealer gives you a " + player_card_first + " and " + player_card_second
print "Your hand is now equal to " + str(hValue)

dealer_card_first = random.choice(deck)
deck.remove(dealer_card_first)

dealer_card_second = random.choice(deck)
deck.remove(dealer_card_second)

dhand = [dealer_card_first, dealer_card_second]

dValue = handVal(dhand)

print "Dealer get",  dealer_card_first, "and another card"


while hValue < 21:
	print "You now have 2 options"

	decide_one = raw_input ("Hit or stay? ")

	if decide_one == "hit":	
		player_card_hit = random.choice(deck)
		deck.remove(player_card_hit)
		print "Dealer gives you a " + player_card_hit
		hand.append(player_card_hit) 
		print "You now have "
		for card in hand:
			print card
		hValue = handVal(hand)
		print "Your hand is equal to " + str(hValue)
	elif decide_one == "stay":
		print "You chose to stay with " + str(hValue)
		break

if hValue > 21:
	print "You went bust. Dealer wins :("
	sys.exit()

while dValue < 17:
	dealer_card_hit = random.choice(deck)
	deck.remove(dealer_card_hit)
	print "Deal gets", dealer_card_hit
	dhand.append(dealer_card_hit)
	dValue = handVal(dhand)

print "Dealer has", str(dValue)

if dValue > 21:
	print "Dealer went bust, now you win!"
	sys.exit()

elif dValue == hValue:
	print "You tied with the dealer"
elif dValue > hValue:
	print "Dealer won. :("
elif dValue < hValue:
	print "You won!!! :)"




