#!/usr/bin/env python

from random import choice

class Deck(object):

		# Class object variables
		size = 52
		contents = {
				1: ["Ace of Clubs", [1,11]],
				2: ["Two of Clubs", 2],
				3: ["Three of Clubs", 3],
				4: ["Four of Clubs", 4],
				5: ["Five of Clubs", 5],
				6: ["Six of Clubs", 6],
				7: ["Seven of Clubs", 7],
				8: ["Eight of Clubs", 8],
				9: ["Nine of Clubs", 9],
				10: ["Ten of Clubs", 10],
				11: ["Jack of Clubs", 10],
				12: ["Queen of Clubs", 10],
				13: ["King of Clubs", 10],
				14: ["Ace of Diamonds", [1,11]],
				15: ["Two of Diamonds", 2],
				16: ["Three of Diamonds", 3],
				17: ["Four of Diamonds", 4],
				18: ["Five of Diamonds", 5],
				19: ["Six of Diamonds", 6],
				20: ["Seven of Diamonds", 7],
				21: ["Eight of Diamonds", 8],
				22: ["Nine of Diamonds", 9],
				23: ["Ten of Diamonds", 10],
				24: ["Jack of Diamonds", 10],
				25: ["Queen of Diamonds", 10],
				26: ["King of Diamonds", 10],
				27: ["Ace of Hearts", [1,11]],
				28: ["Two of Hearts", 2],
				29: ["Three of Hearts", 3],
				30: ["Four of Hearts", 4],
				31: ["Five of Hearts", 5],
				32: ["Six of Hearts", 6],
				33: ["Seven of Hearts", 7],
				34: ["Eight of Hearts", 8],
				35: ["Nine of Hearts", 9],
				36: ["Ten of Hearts", 10],
				37: ["Jack of Hearts", 10],
				38: ["Queen of Hearts", 10],
				39: ["King of Hearts", 10],
				40: ["Ace of Spades", [1,11]],
				41: ["Two of Spades", 2],
				42: ["Three of Spades", 3],
				43: ["Four of Spades", 4],
				44: ["Five of Spades", 5],
				45: ["Six of Spades", 6],
				46: ["Seven of Spades", 7],
				47: ["Eight of Spades", 8],
				48: ["Nine of Spades", 9],
				49: ["Ten of Spades", 10],
				50: ["Jack of Spades", 10],
				51: ["Queen of Spades", 10],
				52: ["King of Spades", 10]
		}

		# Initialization method		
		def __init__(self, contents={
				1: ["Ace of Clubs", [1,11]],
				2: ["Two of Clubs", 2],
				3: ["Three of Clubs", 3],
				4: ["Four of Clubs", 4],
				5: ["Five of Clubs", 5],
				6: ["Six of Clubs", 6],
				7: ["Seven of Clubs", 7],
				8: ["Eight of Clubs", 8],
				9: ["Nine of Clubs", 9],
				10: ["Ten of Clubs", 10],
				11: ["Jack of Clubs", 10],
				12: ["Queen of Clubs", 10],
				13: ["King of Clubs", 10],
				14: ["Ace of Diamonds", [1,11]],
				15: ["Two of Diamonds", 2],
				16: ["Three of Diamonds", 3],
				17: ["Four of Diamonds", 4],
				18: ["Five of Diamonds", 5],
				19: ["Six of Diamonds", 6],
				20: ["Seven of Diamonds", 7],
				21: ["Eight of Diamonds", 8],
				22: ["Nine of Diamonds", 9],
				23: ["Ten of Diamonds", 10],
				24: ["Jack of Diamonds", 10],
				25: ["Queen of Diamonds", 10],
				26: ["King of Diamonds", 10],
				27: ["Ace of Hearts", [1,11]],
				28: ["Two of Hearts", 2],
				29: ["Three of Hearts", 3],
				30: ["Four of Hearts", 4],
				31: ["Five of Hearts", 5],
				32: ["Six of Hearts", 6],
				33: ["Seven of Hearts", 7],
				34: ["Eight of Hearts", 8],
				35: ["Nine of Hearts", 9],
				36: ["Ten of Hearts", 10],
				37: ["Jack of Hearts", 10],
				38: ["Queen of Hearts", 10],
				39: ["King of Hearts", 10],
				40: ["Ace of Spades", [1,11]],
				41: ["Two of Spades", 2],
				42: ["Three of Spades", 3],
				43: ["Four of Spades", 4],
				44: ["Five of Spades", 5],
				45: ["Six of Spades", 6],
				46: ["Seven of Spades", 7],
				47: ["Eight of Spades", 8],
				48: ["Nine of Spades", 9],
				49: ["Ten of Spades", 10],
				50: ["Jack of Spades", 10],
				51: ["Queen of Spades", 10],
				52: ["King of Spades", 10]
			}):
				self.contents = contents

		def deal_card(self):
				key = choice(self.contents.keys())
				card_and_value = self.contents.pop(key)
				return key, card_and_value
				
# Player class for creating players for the Blackjack game
class Player(object):

		# Initialization method
		def __init__(self, bankroll=100):
				self.bankroll = bankroll

		def add_bankroll(self, amount):
				self.bankroll += amount
				print 'Your bankroll is now %s' % self.bankroll
				return self.bankroll

		def withdraw_bankroll(self, amount):
				self.bankroll -= amount
				print 'Your bankroll is now %s' % self.bankroll
				return self.bankroll

		def get_bankroll(self):
				print 'Your bankroll is now %s' % self.bankroll
				return self.bankroll

# Hand class to create methods for Blackjack hands
class Hand(object):

		def __init__(self, contents=[]):
				self.contents = contents

		def add_card(self, card):
				self.contents.append(card)

		def get_hand(self):
				return self.contents
		
		def get_score(self):
				score = [0,0]
				ace_counter = False
				for count in self.contents:
				
				# NEED TO FIGURE OUT HOW TO ACCOUNT FOR TWO ACES...

						if count[0].startswith('Ace'):
								score[0]+=1
								score[1]+=11
								ace_counter = True
						else:
								score[0]+=int(count[1])
								score[1]+=int(count[1])
				
				return score
			
'''				
				if ace_counter:
						print "Your hand is currently a %s or a %s." % score[0], score[1]
				else:
						print "Your hand is currently a %s." % score[0]
'''

# PlayerHand class for creating hands for players
class PlayerHand(Hand):
		
		def __init__(self, contents=[]):
				self.contents = contents
				pass
'''
		def add_card(self, card):
				self.contents.append(card)

		def get_hand(self):
				print self.contents
'''

# DealerHand class for creating hand for the dealer
class DealerHand(Hand):
		
		def __init__(self, contents=[]):
				self.contents = contents
				
def deal_cards(deck, player_hand, dealer_hand, players=1):
		for x in range(1, players * 2 + 3):
				key, hit_card_and_value = deck.deal_card()
				hit_card = hit_card_and_value[0]
		#		deck.contents.pop(key)
				if x % 2 == 1:
						player_hand.add_card(hit_card_and_value)
				else:
						dealer_hand.add_card(hit_card_and_value)

def hit(deck, hand, player):
		key, hit_card_and_value = deck.deal_card()
		hit_card = hit_card_and_value[0]
#		deck.contents.pop(key)
		hand.add_card(hit_card_and_value)
		print "%s hit a %s!" % (player, hit_card)

def check_blackjack(hand):
		card1 = hand[0][0]
		card2 = hand[1][0]
		
		if card1.startswith('Ace') and ((card2.startswith('Ten') or\
				card2.startswith('Jack') or card2.startswith('Queen') or\
				card2.startswith('King'))):
				return True
		elif card2.startswith('Ace') and ((card1.startswith('Ten') or\
				card1.startswith('Jack') or card1.startswith('Queen') or\
				card1.startswith('King'))):
				return True
		else:
				return False

def get_cards(hand):
		new_hand = hand.get_hand()
		new_list = []
		for list in new_hand:
				new_list.append(list[0])
		return new_list

def check_bust(hand):
		score = hand.get_score()
		if score[0] < 22:
				return False
		else:
				return True

nick = Player()
nick.add_bankroll(1000)
nick.get_bankroll()
nick.bankroll

print 
print "Let's start our game of Blackjack!"

game_on = True

while game_on:
		
		deck = Deck()
		player_hand = PlayerHand()
		dealer_hand = DealerHand()
		
		print
		print "==================================="
		print "Dealing out the cards!!!!!!!!!!!!!!"
		print "==================================="

		deal_cards(deck, player_hand, dealer_hand)

		print
		print "Your current hand is: %s" % get_cards(player_hand)	
		print
		
		print "Checking for blackjacks..."

		if check_blackjack(player_hand.get_hand()) and \
				check_blackjack(dealer_hand.get_hand()):
					print "Both you and the dealer had a Blackjack!"
					print "The dealer flips over his hand: %s." % get_cards(dealer_hand)	
					break
		elif check_blackjack(player_hand.get_hand()):
					print "You got a blackjack, congratulations!"
					break
		elif check_blackjack(dealer_hand.get_hand()):
					print "The dealer got blackjack, sorry you have lost!"
					break
		else:
					print "No blackjacks!"
		print

		print "Your current hand is: %s" % get_cards(player_hand)	
		
		if player_hand.get_score()[0] == player_hand.get_score()[1]:
				print "Your current score is %s." % player_hand.get_score()[0]
		else:
				print "Your current score is either %s or %s." % (player_hand.get_score()[0], \
						player_hand.get_score()[1])
		print "The dealer is showing a %s" % get_cards(dealer_hand)[1]
		
		hit_count = True
		while hit_count:
				print
				answer = raw_input("Would you like to hit or stay? 'H' or 'S'")
				if answer.upper() == 'H':
						hit(deck, player_hand, 'You')						
						print "Your current hand is: %s" % get_cards(player_hand)	
						
						if player_hand.get_score()[0] == player_hand.get_score()[1]:
								print "Your current score is %s." % player_hand.get_score()[0]
						else:
								if player_hand.get_score()[1] < 22:
										print "Your current score is either %s or %s." % \
												(player_hand.get_score()[0], player_hand.get_score()[1])
								else:
										print "Your current score is %s." % player_hand.get_score()[0]
						
						if check_bust(player_hand):
								print
								print "You have busted! You lose!"
								break
									
				elif answer.upper() == 'S':
						print "You have chosen to stay..."
						if player_hand.get_score()[1] < 22:
								player_score = player_hand.get_score()[1]
						else:
								player_score = player_hand.get_score()[0]

						print "The dealer's hand is: %s" % get_cards(dealer_hand)
						if dealer_hand.get_score()[0] == dealer_hand.get_score()[1]:
								print "Dealer's current score is %s." % dealer_hand.get_score()[0]
								dealer_score = dealer_hand.get_score()[0]
						else:
								print "Dealer's current score is either %s or %s." % \
										(dealer_hand.get_score()[0], dealer_hand.get_score()[1])
								dealer_score = [dealer_hand.get_score()[0], dealer_hand.get_score()[1]]
						if type(dealer_score) == int:
								while dealer_score < 17:
										hit(deck, dealer_hand, 'Dealer')
										print "Dealer's current score is %s." % dealer_hand.get_score()[0]
										dealer_score = dealer_hand.get_score()[0]
								if check_bust(dealer_hand):
										print
										print "The dealer has busted! You win!"
								else:
										if player_score > dealer_score:
													print
													print "You have won! %s to %s" % (player_score, dealer_score)
										elif player_score == dealer_score:			
													print	
													print "You and the dealer have tied! %s to %s" % \
															(dealer_score, player_score)
										else:			
													print
													print "The dealer has beaten you! %s to %s" % \
															(dealer_score, player_hand.get_score()[0])
						else:
								pass			 
						hit_count = False
				else:
						print "Please enter a valid option..."
				
		game_on = False
