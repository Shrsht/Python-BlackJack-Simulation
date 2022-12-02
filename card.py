class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)
    suits = {'diamonds':'♦','hearts':'♥','clubs':'♣','spades':'♠'}
    
    ranks= {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':11,'Q':12,'K':13,"A":14}

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        self.rank = rank
        self.suit = suit
        self.visible = visible
        

    def __lt__(self, other_card):
        if Card.ranks[self.rank] != Card.ranks[other_card.rank]:
            if Card.ranks[self.rank] < Card.ranks[other_card.rank]:
                return True 
            else:
                return False
        if Card.ranks[self.rank] == Card.ranks[other_card.rank]:
            if self.suit <other_card.suit:
                return True 
            else:
                return False
            
            


    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        if self.visible == True:
            
            if self.suit == 'spades':
                s=  "____"+"\n"
                s+= "|"+str(self.rank)+"  |" +"\n"       
                s+= "| ♠ |"+"\n"
                s+= "|__"+str(self.rank)+"|" 
                return s
            elif self.suit == 'hearts' :
                s=  "____"+"\n"
                s+= "|"+str(self.rank)+"  |"  +"\n"      
                s+= "| ♥ |"+"\n"
                s+= "|__"+str(self.rank)+"|" 
                return s
            elif self.suit == 'diamonds':
                s=  "____"+"\n"
                s+= "|"+str(self.rank)+"  |"   +"\n"     
                s+= "| ♦ |"+"\n"
                s+= "|__"+str(self.rank)+"|" 
                return s
            elif self.suit == 'clubs':
                s=  "____"+"\n"
                s+= "|"+str(self.rank)+"  |" +"\n"       
                s+= "| ♣ |"+"\n"
                s+= "|__"+str(self.rank)+"|" 
                return s
                
        elif self.visible == False :
            
            s=  "____"+"\n"
            s+= "|?  |"   +"\n"     
            s+= "| ? |"+"\n"
            s+= "|__?|" 
            return s
            
            

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """        
        if self.visible == True:
            return '('+str(self.rank)+", " + str (self.suit)+')'
        else:
            return "(?, ?)"

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert type(visible)== bool
        if visible == True:
            self.visible = True 
        else:
            self.visible = False
        
    
