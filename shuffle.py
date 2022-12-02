class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25
    
    
    """    
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert type(cards) == list
    
        if num ==0:
            return cards
        else:
            #NUM=ODD and deck = EVEN
            if num%2!=0 and len(cards)%2==0:
                mid = int(len(cards)/2)
                top_half = cards[:mid]
                bottom_half= cards[mid:]
                check = (len(top_half),len(bottom_half))
                top_range = num - int(num/2)
                bottom_range = int(num/2)
                remove = top_half[-top_range:] + bottom_half[:bottom_range]
                remainder = top_half[:-top_range]+bottom_half[bottom_range:]
                oneround= remove+remainder
                return Shuffle.modified_overhand(oneround,num-1)
            #NUM=EVEN and deck = EVEN
            elif num%2== 0 and len(cards)%2==0:
                mid = int(len(cards)/2)
                top_half = cards[:mid]
                bottom_half= cards[mid:]
                #check = (len(top_half),len(bottom_half))
                top_range = num - int(num/2)
                bottom_range = int(num/2)
                remove = top_half[-top_range:] + bottom_half[:bottom_range]
                remainder = top_half[:-top_range]+bottom_half[bottom_range:]
                oneround = remove+remainder
                return Shuffle.modified_overhand(oneround,num-1) 
            #NUM=EVEN and deck = ODD
            elif num%2!=0 and len(cards)%2!=0:
                middle = int(len(cards)/2)
                top_half= cards[:2]
                bottom_half= cards[2:]
                top_range = num - int(num/2)
                bottom_range = int(num/2)
                remove = top_half[-top_range:] + bottom_half[:bottom_range]
                remainder = top_half[:-top_range]+bottom_half[bottom_range:]
                oneround = remove+remainder
                return Shuffle.modified_overhand(oneround,num-1)
            #NUM=EVEN and deck = EVEN
            elif num%2==0 and len(cards)%2!=0:
                middle = int(len(cards)/2)
                top_half= cards[:2]
                bottom_half= cards[2:]
                top_range = num - int(num/2)
                bottom_range = int(num/2)
                remove = top_half[-top_range:] + bottom_half[:bottom_range]
                remainder = top_half[:-top_range]+bottom_half[bottom_range:]
                oneround = remove+remainder
                return Shuffle.modified_overhand(oneround,num-1)
                    
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        right_hand = []
        left_hand = cards
        if len(left_hand)==0:
            return right_hand
        else:
            if len(left_hand)%2==0:
                right_hand.append(left_hand[-1])
                return right_hand+ Shuffle.mongean(cards[:-1])
            else:
                right_hand.append(left_hand[-1])
                return Shuffle.mongean(cards[:-1])+ right_hand
                
                
            
    
