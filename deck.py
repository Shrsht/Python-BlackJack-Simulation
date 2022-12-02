from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)
    """

    # Class Attribute(s)
    suits = ['diamonds','hearts','clubs','spades']
    
    ranks= [2,3,5,6,7,8,9,10,'J','Q','K',"A"]
    
    
    

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        self.cards = [Card(r,'hearts',visible=True) for r in Deck.ranks] + \
         [Card(r,'diamonds',visible=True) for r in Deck.ranks] + \
         [Card(r,'clubs',visible=True) for r in Deck.ranks] + \
         [Card(r,'spades',visible=True) for r in Deck.ranks]
         
        cards = self.cards 
        cards.sort()
        

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
    #    CHECK　FOR　ORDER of operations shuffle_and_count
        
    
        new =[]
        for type in shuffle_and_count.keys():
            new.append(type)
            new.sort()
        for type in new:
            if type == 'modified_overhand':
                self.cards = Shuffle.modified_overhand(self.cards,shuffle_and_count[type])
            else:
                for i in range(shuffle_and_count[type]):
                    self.cards = Shuffle.mongean(self.cards)
            

    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand,PlayerHand) or isinstance(hand,DealerHand)
        hand.add_card(self.cards.pop(0))
        

    def get_cards(self):
        return self.cards
