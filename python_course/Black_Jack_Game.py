"""
Game Play

To play a hand of Blackjack the following steps must be followed:

1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10.If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
11.Determine the winner and adjust the Player's chips accordingly
12.Ask the Player if they'd like to play again

"""

# imports and variables

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

#class definitions

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    
    def __init__(self):
        self.deck = []  # starting with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop() 
        return single_card

# uncomment below if necessary for test if it works so far
# test_deck = Deck()
# test_deck.shuffle() # keep it as a comment if you want to have deck in order!
# print(test_deck)


class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card) #card passed in is from class Deck():
        self.value += values[card.rank] #Deck.deal() -> single Card(suit,rank)
        if card.rank == 'Ace': #track aces
            self.aces += 1
    
    def adjust_for_ace(self):
        
        #If total value > 21 and I still have an ACE
        #than change my ace to be 1 instead of an 11!!!
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1



# test_deck = Deck()
# test_deck.shuffle()

# #Player
# test_player = Hand()
# #Deal 1 card from the deck Card(suit,rank)
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)


class Chips:
    
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


#Function Defintions:


#function for taking bets
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry, please provide an integer!")
        else:
            if chips.bet > chips.total:
                print(f"Sorry you don't have enough chips! You have: {chips.total}")
            else:
                break


#function for taking hits
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


#function prompting the Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Hit or Stand? Enter h or s ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print("Player Stands, Dealer's Turn")
            playing = False
        
        else:
            print("Sorry I didn't understand that, Please enter h or s only!")
            continue    
        break


#functions to display cards
def show_some(player,dealer):
    
    print('DEALERS HAND:')
    print('one card hidden!')
    print('',dealer.cards[1])
    print('\n')
    print('PLAYERS HAND:')
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    
    print('DEALERS HAND:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('PLAYERS HAND:')
    for card in player.card:
        print(card)

#functions to handle end of game scenarios
def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Player Wins! Dealer Busted!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer Wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Player and Dealer tie! PUSH")


# GAME PLAY:

while True:
    # Print an opening statement
    
    print("Welcome to BlackJack Game!!!")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())   

    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    
    # Inform Player of their chips total 
    print(f"\n Players total chips are at: {player_chips.total}")

    # Ask to play again
    new_game = input("Would you like to play another hand? y/n")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break


