#!/usr/bin/env python

from random import randint

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
				key = randint(1,len(self.contents))
				hit_card = self.contents[key][0]
				return hit_card, key
				self.contents.pop(key)
				
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
				print self.contents

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
				hit_card, key = deck.deal_card()
				deck.contents.pop(key)
				if x % 2 == 1:
						player_hand.add_card(hit_card)
						print "You've been dealt a %s!" % hit_card
				else:
						dealer_hand.add_card(hit_card)

def hit(deck, hand):
		hit_card, key = deck.deal_card()
		deck.contents.pop(key)
		hand.add_card(hit_card)
		print "You hit a %s!" % hit_card

nick = Player()
nick.add_bankroll(1000)
nick.get_bankroll()
nick.bankroll

deck = Deck()
player_hand = PlayerHand()
dealer_hand = DealerHand()

deal_cards(deck, player_hand, dealer_hand)
print deck.contents
player_hand.get_hand()

hit(deck, player_hand)
print len(deck.contents)