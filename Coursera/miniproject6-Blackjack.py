# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
done = False
outcome = ""
hint = "New deal?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        hand_list = []
        self.hand_list = hand_list
    def __str__(self):
        # return a string representation of a hand
        all_card = ""
        for i in self.hand_list:
            all_card += str(i) + " "
        #return "Hand contains " + all_card
        return "Hand contains " + all_card
    def add_card(self, card):
        # add a card object to a hand
        self.card = card
        self.hand_list.append(self.card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        have_ace = False
        for card in self.hand_list:
            hand_value += VALUES[card.get_rank()] 
            if str(card)[1] == 'A':
                have_ace = True    
        if not have_ace: 
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
                
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for num , card in enumerate(self.hand_list):
            card.draw(canvas, [pos[0] + num * (CARD_SIZE[0]+10), pos[1]])    
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        deck_list = []
        self.deck_list = deck_list
        for suit in SUITS: 
            for rank in RANKS:
                self.deck_list.append(Card(suit, rank))
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck_list)
    def deal_card(self):
        # deal a card object from the deck
        return self.deck_list.pop()
    def __str__(self):
        # return a string representing the deck
        all_deck = ""
        for i in self.deck_list:
            all_deck += str(i) + " "
        return "Deck contains " + all_deck

#define event handlers for buttons
def deal():
    global hint, in_play, round_deck, outcome, score, Done
    global round_deck, dealer, player
    done = False
    outcome = ""
    round_deck = Deck()
    dealer = Hand()
    player = Hand()
    # your code goes here
    round_deck.shuffle()
    dealer.add_card(round_deck.deal_card())
    dealer.add_card(round_deck.deal_card())
    player.add_card(round_deck.deal_card())
    player.add_card(round_deck.deal_card())
    #print "dealer: " + str(dealer)
    #print "player: " + str(player)
    if in_play:
        score -= 1
    in_play = True
    hint = "Hit or Stand?"
    #print "in_play:" + str(in_play), "done:" + str(done)
def hit():
    # replace with your code below
    global outcome, in_play, round_deck, score,done 
    # if the hand is in play, hit the player
    if in_play and player.get_value() <= 21:
        player.add_card(round_deck.deal_card())
        #print "player: " + str(player)
    # if busted, assign a message to outcome, update in_play and score
    if in_play and player.get_value() > 21 :
        outcome = "You have busted"
        #print outcome
        hint = "New deal?"
        in_play = False
        score -= 1
        done = True   
    #print "in_play:" + str(in_play), "done:" + str(done)
def stand():
    # replace with your code below
    global in_play, score, outcome, hint, done
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() <= 17:
            dealer.add_card(round_deck.deal_card())

        # assign a message to outcome, update in_play and score
        if 21 >= dealer.get_value() >= player.get_value():
            outcome = "You lose."
            score -= 1
        else:
            outcome = "You win."
            score += 1
        #print str(dealer), str(player), outcome
        hint = "New deal?"
        in_play = False
        done = True
    #print "in_play:" + str(in_play), "done:" + str(done)
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global dealer, player, outcome, hint, in_play, done
    """
    card = Card("S", "A")
    card.draw(canvas, [300, 300])
    """
    canvas.draw_text('Blackjack', (100, 100), 40, 'Aqua', "sans-serif")
    canvas.draw_text('Dealer', (100, 180), 30, 'Black', "sans-serif")
    canvas.draw_text('Player', (100, 380), 30, 'Black', "sans-serif")
    canvas.draw_text('Score ' + str(score), (400, 100), 30, 'Black', "sans-serif")
    canvas.draw_text(hint, (300, 380), 30, 'Black', "sans-serif")
    canvas.draw_text(outcome, (300, 180), 30, 'Black', "sans-serif")
    if done:
        dealer.draw(canvas, [100, 200])
        player.draw(canvas, [100, 400])
    if in_play:
        dealer.draw(canvas, [100, 200])
        player.draw(canvas, [100, 400])
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_SIZE[0] / 2, 200 + CARD_SIZE[1] / 2], CARD_BACK_SIZE)
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
#deal()
frame.start()


# remember to review the gradic rubric
