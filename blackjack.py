from deck import Deck
from hand import DealerHand, PlayerHand
from card import Card

# don't change these imports
from numpy.random import randint, seed
seed(20)

class Blackjack:
    """
    Game of blackjack!

    # Removes the game summaries from the previous doctest run
    >>> from os import remove, listdir
    >>> for f in listdir("game_summaries"):
    ...    remove("game_summaries/" + f)

    #######################################
    ### Doctests for calculate_score() ####
    #######################################
    >>> card_1 = Card("A", "diamonds")
    >>> card_2 = Card("J", "spades")
    >>> hand_1 = PlayerHand()
    >>> Blackjack.calculate_score(hand_1)
    0
    >>> hand_1.add_card(card_1)
    >>> Blackjack.calculate_score(hand_1) # (Ace)
    11
    >>> hand_1.add_card(card_2)
    >>> Blackjack.calculate_score(hand_1) # (Ace, Jack)
    21

    >>> card_3 = Card("A", "spades")
    >>> hand_2 = PlayerHand()
    >>> hand_2.add_card(card_1, card_3)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace)
    12
    >>> hand_2.add_card(card_2)
    >>> Blackjack.calculate_score(hand_2) # (Ace, Ace, Jack)
    12

    >>> hand_3 = PlayerHand()
    >>> card_4 = Card(2, "spades")
    >>> card_5 = Card(4, "spades")
    >>> hand_3.add_card(card_4, card_5)
    >>> Blackjack.calculate_score(hand_3)
    6
    >>> odd_hand = PlayerHand()
    >>> card_n = Card(10, "clubs")
    >>> card_m = Card("A", "clubs")
    >>> odd_hand.add_card(card_n,card_m)
    >>> Blackjack.calculate_score(odd_hand)
    21

    #######################################
    ### Doctests for determine_winner() ####
    #######################################
    >>> blackjack = Blackjack(10)
    >>> blackjack.determine_winner(10, 12)
    -1
    >>> blackjack.determine_winner(21, 21)
    0
    >>> blackjack.determine_winner(22, 23)
    0
    >>> blackjack.determine_winner(12, 2)
    1
    >>> blackjack.determine_winner(22, 2)
    -1
    >>> blackjack.determine_winner(2, 22)
    1
    >>> print(blackjack.get_log())
    Player lost with a score of 10. Dealer won with a score of 12.
    Player and Dealer tie.
    Player and Dealer tie.
    Player won with a score of 12. Dealer lost with a score of 2.
    Player lost with a score of 22. Dealer won with a score of 2.
    Player won with a score of 2. Dealer lost with a score of 22.
    <BLANKLINE>  
    >>> blackjack.reset_log()

    #######################################
    ### Doctests for play_round() #########
    #######################################
    >>> blackjack_2 = Blackjack(10)
    >>> blackjack_2.play_round(1, 15)
    >>> print(blackjack_2.get_log())
    Round 1 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (10, clubs) (A, clubs)
    Dealer Cards: (Q, clubs) (?, ?)
    Dealer Cards Revealed: (7, diamonds) (Q, clubs)
    Player won with a score of 21. Dealer lost with a score of 17.
    <BLANKLINE>
    >>> blackjack_2.reset_log()
   
    >>> blackjack_2.play_round(3, 21)
    >>> print(blackjack_2.get_log())
    Round 2 of Blackjack!
    wallet: 15
    bet: 5
    Player Cards: (4, clubs) (7, clubs)
    Dealer Cards: (A, hearts) (?, ?)
    Player pulled a (J, hearts)
    Dealer Cards Revealed: (5, clubs) (A, hearts)
    Dealer pulled a (6, clubs)
    Dealer pulled a (2, clubs)
    Dealer pulled a (8, clubs)
    Player won with a score of 21. Dealer lost with a score of 22.
    Round 3 of Blackjack!
    wallet: 20
    bet: 10
    Player Cards: (6, hearts) (9, diamonds)
    Dealer Cards: (K, hearts) (?, ?)
    Player pulled a (Q, hearts)
    Dealer Cards Revealed: (J, diamonds) (K, hearts)
    Player lost with a score of 25. Dealer won with a score of 20.
    Round 4 of Blackjack!
    wallet: 10
    bet: 5
    Player Cards: (5, diamonds) (10, diamonds)
    Dealer Cards: (2, diamonds) (?, ?)
    Player pulled a (3, diamonds)
    Player pulled a (7, spades)
    Dealer Cards Revealed: (2, diamonds) (2, hearts)
    Dealer pulled a (K, spades)
    Dealer pulled a (3, spades)
    Player lost with a score of 25. Dealer won with a score of 17.
    <BLANKLINE>
    
    >>> with open("game_summaries/game_summary2.txt", encoding = 'utf-8') as f:
    ...     lines = f.readlines()
    ...     print("".join(lines[10:26]))
    Dealer Hand:
    ____
    |7  |
    | ♦ |
    |__7|
    ____
    |Q  |
    | ♣ |
    |__Q|
    Winner of ROUND 1: Player
    <BLANKLINE>
    ROUND 2:
    Player Hand:
    ____
    |4  |
    | ♣ |
    <BLANKLINE>

    >>> blackjack_3 = Blackjack(5)
    >>> blackjack_3.play_round(5, 21)
    >>> print(blackjack_3.get_log())
    Round 1 of Blackjack!
    wallet: 5
    bet: 5
    Player Cards: (2, clubs) (2, hearts)
    Dealer Cards: (2, diamonds) (?, ?)
    Player pulled a (3, clubs)
    Player pulled a (3, diamonds)
    Player pulled a (3, hearts)
    Player pulled a (3, spades)
    Player pulled a (4, clubs)
    Player pulled a (4, diamonds)
    Dealer Cards Revealed: (2, diamonds) (2, spades)
    Dealer pulled a (4, hearts)
    Dealer pulled a (4, spades)
    Dealer pulled a (5, clubs)
    Player lost with a score of 24. Dealer won with a score of 17.
    Wallet amount $0 is less than bet amount $5.

    >>> blackjack_4 = Blackjack(500)
    >>> blackjack_4.play_round(13, 21) # At least 52 cards will be dealt
    >>> blackjack_4.reset_log()
    >>> blackjack_4.play_round(1, 17)
    >>> print(blackjack_4.get_log())
    Not enough cards for a game.
    """
    # Class Attribute(s)
    num_games = 0
    new_ranks= {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10,"A":11}
    my_deck = Deck()
    def __init__(self, wallet):
        # Initialize instance attributes
        # auto-increment as needed
        #WRITE ASSERT STATEMENTS LATER
        #self.my_deck = Deck()
        self.wallet  =  wallet 
        self.game_number = Blackjack.num_games+1
        self.log = ''
        self.bet_amount = 5 
        self.bet_required = 5
    
    def play_round(self, num_rounds, stand_threshold):
        """
        Plays `num_rounds` Blackjack rounds.

        Parameters:
            num_rounds (int): Number of rounds to play.
            stand_threshold (int): Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold)
        """
        # This could get pretty long!
        # ADD ASSERT STATEMENTS do it in  a for loop
        assert type(num_rounds) == int
        assert num_rounds > 0
        assert type(stand_threshold) == int 
        assert stand_threshold > 0
        
        for this_round in range(num_rounds):
            if len(Blackjack.my_deck.cards) < 4:
                self.log += 'Not enough cards for a game.' #"DO WE HAVE TO ADD TO THE LOG and return it? OR JUST NOT DO ANYTHING FOR IT"
            #HOH TO EXIT PROGRAM OR STOP PLAYING GAME?
            elif self.wallet < self.bet_amount:
                self.log += "Wallet amount $"+ str(self.wallet)+ "is less than bet amount $"+ str(self.bet_amount)+'/n'
               
            else:
                self.log += "Round "+str(this_round+1)+ " of Blackjack!"+ '\n'
                self.log += "wallet: "+ str(self.wallet)+ '\n'
                self.log += "bet: "+ str(self.bet_amount)+ '\n'
                
                #mong_num = 
                #oh_num = randint(1,5,1)[0]
                shuffled = Blackjack.my_deck.shuffle(modified_overhand= randint(1,5,1)[0], mongean = randint(1,5,1)[0])
            
                pl_hand = PlayerHand()
                dl_hand = DealerHand()
        
                for i in range(0,2):
                    Blackjack.my_deck.deal_hand(pl_hand)
                    Blackjack.my_deck.deal_hand(dl_hand)
                    
        
                self.log+= 'Player Cards: '+ str(pl_hand.cards[0].__repr__())+" "+str(pl_hand.cards[1].__repr__())+'\n' 
                self.log+= "Dealer Cards: "+ str(dl_hand.cards[0].__repr__())+' '+str(dl_hand.cards[1].__repr__())+'\n'
                
                Blackjack.hit_or_stand(self,pl_hand, stand_threshold)
                dl_hand.reveal_hand()
                self.log += 'Dealer Cards Revealed:'+ dl_hand.cards.__repr__()+'\n'
            
                self.hit_or_stand(dl_hand,17)
            
                pl_score = Blackjack.calculate_score(pl_hand)
                dl_score = Blackjack.calculate_score(dl_hand)
            
                winner= self.determine_winner(pl_score,dl_score)
            
                if winner == 1:
                    self.wallet+= self.bet_amount
                    self.bet_required +=5
                    self.add_to_file(pl_hand,dl_hand,"Player")
                elif winner == -1:
                    self.wallet -= 5
                    self.bet_required -= 5
                    self.add_to_file(pl_hand,dl_hand,"Dealer")
                else:
                    self.wallet += 0
                    self.bet_required += 0
                    self.add_to_file(pl_hand,dl_hand,"Tied")
                            
    def calculate_score(hand):
        """
        Calculates the score of a given hand. 

        Sums up the ranks of each card in a hand. Jacks, Queens, and Kings
        have a value of 10 and Aces have a value of 1 or 11. The value of each
        Ace card is dependent on which value would bring the score closer
        (but not over) 21. 

        Should be solved using list comprehension and map/filter. No explicit
        for loops.

        Parameters:
            hand: The hand to calculate the score of.
        Returns:
            The best score as an integer value.
        """
        #HOW TO CALCULATE FOR DEALER CARDS?? write assert statement
        assert isinstance(hand,PlayerHand) or isinstance(hand,DealerHand)
        score= 0
        score_list = [Blackjack.new_ranks[card_tuples.rank] for card_tuples in hand.cards]
        score_list.sort()
        if sum(score_list) <= 21:
            score+= sum(score_list)
            return score
        else:
            elevens = list(filter( lambda x: x == 11,score_list))
            others = list(filter( lambda x: x!= 11,score_list))
    
            if 21- sum(others) <= 11:
                changed = [ 1 for i in elevens]
                score = sum(others) + sum(changed)
                return score
            else:
                changed = [ 1 for i in elevens[:-1]]
                others = others+[11]
                score = sum(others) + sum(changed)
                return score 
            
                
        

    def determine_winner(self, player_score, dealer_score):
        """
        Determine whether the Blackjack round ended with a tie, dealer winning, 
        or player winning. Update the log to include the winner and
        their scores before returning.

        Returns:
            1 if the player won, 0 if it is a tie, and -1 if the dealer won
        """
        p_diff = 21 - player_score
        d_diff = 21 - dealer_score
        if p_diff < 0 and d_diff < 0:
            self.log += 'Player and Dealer tie.\n'
            return 0
        elif p_diff == d_diff :
            self.log += 'Player and Dealer tie.\n'
            return 0
        elif p_diff > 0 and d_diff >0 and p_diff < d_diff:
            self.log += 'Player won with a score of '+ str(player_score)+'. Dealer lost with a score of '+ str(dealer_score)+'.\n'
            return 1
        elif p_diff < 0:
            self.log += 'Player lost with a score of '+ str(player_score)+'. Dealer won with a score of '+ str(dealer_score)+'.\n'
            return -1
        elif p_diff > 0 and d_diff >0 and p_diff > d_diff:
            self.log += 'Player lost with a score of '+ str(player_score)+'. Dealer won with a score of '+ str(dealer_score)+'.\n'
            return -1
        elif d_diff < 0:
            self.log += 'Player won with a score of '+ str(player_score)+'. Dealer lost with a score of '+ str(dealer_score)+'.\n'
            return 1
            
            

    def hit_or_stand(self, hand, stand_threshold):
        """
        Deals cards to hand until the hand score has reached or surpassed
        the `stand_threshold`. Updates the log everytime a card is pulled.

        Parameters:
            hand: The hand the deal the cards to depending on its score.
            stand_threshold: Score threshold for when the player
            will stand (ie player stands if they have a score >= 
            this threshold).
        """
        #while Blackjack.calculate_score(hand) >= stand_threshold:
        if len(Blackjack.my_deck.cards) > 0:
            if Blackjack.calculate_score(hand) < stand_threshold:
                Blackjack.my_deck.deal_hand(hand)
                if isinstance(hand,PlayerHand) == True:
                    self.log += "Player pulled a "+ hand.cards[0].__repr__()+'\n'
                else:
                    self.log += "Dealer pulled a "+ hand.cards[0].__repr__()+'\n'

    def get_log(self):
        return self.log
    
    def reset_log(self):
        self.log = ''
        
        
        
    def add_to_file(self, player_hand, dealer_hand, result):
        """
        Writes the summary and outcome of a round of Blackjack to the 
        corresponding .txt file. This file should be named game_summaryX.txt 
        where X is the game number and it should be in `game_summaries` 
        directory.
        """
        
        # Remember to use encoding = "utf-8" 
        with open("./game_summaries/game_summary" +str(self.game_number)+'.txt', "x") as f:
            f.write("ROUND "+ str(self.game_number)+'\n'+'Player Hand:\n'+str(player_hand)+'\n' \
            +"Dealer Hand:\n"+str(dealer_hand)+'\n'+'Winner of ROUND '+ str(self.game_number)+': '+str(result))
            
