# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
suits = ["H", "S", "C", "D"]

def highCard(hand):
  handcards = list(i[0] for i in hand)
  indexes = list(cards.index(cardValue) for cardValue in handcards)
  indexes.sort(reverse=True)
  return indexes

def pair(hand):
  handcards = list(i[0] for i in hand)
  pairNumber = str()
  for card in handcards:
    if (handcards.count(card) == 2):
      pairNumber = card

  if pairNumber:
    handcards.remove(pairNumber)
    handcards.remove(pairNumber)
    handcards = list(cards.index(card) for card in handcards)
    handcards.sort(reverse=True)
    handcards.insert(0, cards.index(pairNumber))
  return {
    "status": len(set(handcards)) == 4,
    "cards": handcards
  } 

def twoPairs(hand):
  handcards = list(i[0] for i in hand)
  return {
    "status": len(set(handcards)) == 3 and all(handcards.count(card) != 3 for card in handcards),
    "cards": []
  }

def threeOfKind(hand):
  handcards = list(i[0] for i in hand)
  return {
    "status": len(set(handcards)) == 3 and any(handcards.count(card) == 3 for card in handcards),
    "cards": []
  } 

def straight(hand):
  handcards = list(i[0] for i in hand)
  indexes = list(cards.index(cardValue) for cardValue in handcards)
  indexes.sort()
  return {
    "status": (all(index - indexes[0] in range(5) for index in indexes) or indexes == [0, 1, 2, 3, 12]) and len(set(indexes)) == 5,
    "cards": []
  }

def flush(hand):
  firstSuit = hand[0][1]
  return {
    "status": all(suit[1] == firstSuit for suit in hand),
    "cards": []
  }
  
def fullHouse(hand):
  handcards = list(i[0] for i in hand)
  return {
    "status": len(set(handcards)) == 2 and any(handcards.count(card) == 3 for card in handcards),
    "cards": []
  } 

def fourOfKind(hand):
  handcards = list(i[0] for i in hand)
  cards_set = set()
  for card in handcards:
    if (handcards.count(card)) == 4: cards_set.add(cards.index(card))
  cards_set = cards_set.union(set(cards.index(n) for n in handcards))
  return {
    "status": len(set(handcards)) == 2 and any(handcards.count(card) == 4 for card in handcards),
    "cards": cards_set
  }

def straightFlush(hand):
  return {
    "status": straight(hand) and flush(hand),
  } 

def royalFlush(hand):
  handcards = list(i[0] for i in hand)
  return {
    "status": all(card in cards[-5:] for card in handcards) and flush(hand)
  } 

allChecks = [
  royalFlush,
  straightFlush,
  fourOfKind,
  fullHouse,
  flush,
  straight,
  threeOfKind,
  twoPairs,
  pair
]

def getScore(player):
  for callback in allChecks:
    a = callback(player)
    if (a["status"] == True):
      return allChecks.index(callback)
  return 100

def getWinner(player1, player2):
  score_p1 = getScore(player1)
  score_p2 = getScore(player2)
  if (score_p1 < score_p2):
    return 1
  elif (score_p1 > score_p2):
    return 0
  elif (score_p1 == score_p2 != 100):
    for index, card in enumerate(allChecks[score_p1](player1)["cards"]):
      if (card > allChecks[score_p2](player2)["cards"][index]):
        return 1
      if (card < allChecks[score_p2](player2)["cards"][index]):
        return 0
  else:
    max1 = highCard(player1)
    max2 = highCard(player2)
    for index, card in enumerate(max1):
      if (card > max2[index]): return 1
      if (card < max2[index]): return 0

import os

os.chdir('./54-Poker-hands/')

def getAllHands():
  hands = open("./p054_poker.txt", "r").read()
  hands = hands.split("\n")
  player1Score = 0
  for hand in hands:
    newHand = hand.split(" ")
    player1 = newHand[:5]
    player2 = newHand[5:]
    player1Score += getWinner(player1, player2)
  return player1Score

print(getAllHands()) # 376

#Correct