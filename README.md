# Python BlackJack Simulation

In this project, I implement a Python simulation of a Blackjack game using object-oriented programming techniques.
Blackjack is a card game typically played at casinos where each player competes against the dealer to get a score closest to 21, without going over 21. At the start of the game, each player and the dealer are given 2 cards. A person's set of cards is referred to as their hand. The player's own cards (their hand) are visible to themselves and only one of the dealer's cards is visible to everyone. After everyone receives their cards, the dealer asks each player whether they would like to hit (take another card) or stand (keep their current cards). Each player can hit (take a card) as many times as they would like to get their score as close to 21 as possible, without going over. Afterwards, the dealer reveals their card and decides to hit or stand. Lastly, the final scores are calculated and the winner is announced.

This project implements 5 major classes: Card, Deck, PlayerHand, Shuffle, and Blackjack. 

## 1) CARDS CLASS:

This implements a class of object that represent an individual card of a standard 52-Playing Card deck. This class has 3 instance attributes:
  - RANK : The possible values range from 2-10 (inclusive both ends) and include "A" (for Ace), "J" (for Jack), "Q" (for Queen), and "K" (for King).
  - SUIT : The possible values are "hearts", "spades", "clubs", and "diamonds".
  - HIDDEN : Indicates if a card is Visible or Hidden. 


Examples of printed out cards:

  Visible Card:
        ____
        |A  |
        | ♠ |
        |__A|
        
  Hidden Card:
        ____
        |?  |
        | ? |
        |__?|
        
 This class also implements the 'COMPARE()' method that allows us to compare the ranks (and/or suits) of 2 different cards.
        
## 2) PLAYERHAND & DEALERHAND CLASSES:

This implements the Playerhand Class which is later inherited by the Dealerhand class. In Blackjack, the difference between Dealer and Player is that all the cards in a player's hand are visible to the player whereas only the first card in a dealer's hand is visible
These class implement methods like:
  - GET_CARDS(): Returning a list of cards in a plyer's hand
  - SORT_HAND(): Arranges hand in Ascending Order
  - ADD_CARD(): Adds a single card to a player's hand
  - REVEAL_CARD(): Reveals the cards in a hand in ascending order. 
  
  Dealer Hand has a few of these methods implemented differently to accomodate the special role of the dealer in BlackJack
  
## 3) SHUFFLE CLASS:
This class shuffles the cards in a given hand. It implements 2 kinds of Shuffle methods:
 
   -MODIFIED_OVERHAND() Shuffling: In this method, a number 'N' cards are taken from the middle of the deck and put on the top of the deck. Then, (N- 1) cards from the middle of the deck are put on the top of the deck. This process is repreated N times
   -MONGEAN() Shuffling: In this method, the deck is split into 2 'hands' and alternating cards from the top and bottom of each hand are switched repeatedly untill all cards have been split.The 2 are then joined This function is implemented using recursion. 

## 4) DECK CLASS:
This class implements the previous 3 classes by incorporating CARDS, PLAYER & DEALER HANDS with SHUFFLE to create a complte deck of 52 cards, ranked in ascending order of rank and suit
It implements the following methods:

  - DEAL_HAND(): Takes the first card from the deck and adds it to the given hand. If it is dealt to a Player hand, the card is dealt in ascending order of rank
  - SHUFFLE(): This shuffles a deck of 52 cards. This takes in 2 parameters of (1)Type of Shuffle, i.e- Mongean or Overhand , as well (2) N: the number of cards/times the shuffle takes place

## 5) PLAY_BLACKJACK:
This class combines the methods and implementation discussed in the previous classes while also introducing some new methods like (1) Betting ,(2) Scoring to determine the winner of a given round as per the ruules of Blackjack.
It also writes a 'Summary' .txt file of every hand played in a given round so as to calculate the scores and bets of each player. This class implements numerous methods.
Some of which are:

  - RESET() : Resets the hands and Starts a new round/game of Blackjack
  - CALCULATE_SCORE() : Calculates the score of a dealt hand based on the rules of Blackjack using the ranks of the cards (Card objects) in a Hand object
  - HIT_OR_STAND() : Deals cards to a hand untill the stnad threshold has been reached (For more info view: [Rules of Blackjack](https://bicyclecards.com/how-to-play/blackjack/))
  - DETERMINE_WINNER() : Determines who won the Blackjack round given the player and dealer scores. Return 0 if the Blackjack round ended with a tie, -1 if the dealer won, or 1 if the player won. It also updates the log book 
  - PLAY_ROUND(): Implements previous methods to run a simulation of a game of Blakcjack. Is the final method run in this simulations

