#First Name: Ahmad Naween
#Last Name: Samandar
#ID: 300446112


########################
###### CARD GAME
########################

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
        input("Press enter to continue. ")
        print("\n" + "*" * 59)
    except SyntaxError:
        pass


def make_deck():
    '''()->list of str
    Returns a list of strings representing the playing deck,
    with one queen missing.
    '''
    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']  
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    deck.remove('Q\u2663')  # remove one Queen as per game rules
    return deck


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str, list of str)
    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's (Robot's) deck,
    and the second represents the other player's (Human's) deck.
    '''
    dealer = deck[::2] #dealer will receive 0,2,4,6,8,.... cards
    human = deck[1::2] #human will receive 1,3,5,7,9,...... cards
    return dealer, human


def remove_pairs(l):
    '''(list of str)->list of str
    Returns a copy of list l where all pairs from l are removed and
    the elements of the new list are shuffled.

    Precondition: elements of l are cards represented as strings.

    >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    no_pairs = [] #empty list to hold pair values after removal
    rank_count = {} #it holds cards according to their rank

    for card in l:
        #it iterates through list, and add values according to rank into rank_count
        rank = card[:-1]
        if rank in rank_count:
            rank_count[rank].append(card)
        else:
            rank_count[rank] = [card]

    for cards in rank_count.values():
        #then it iterates through rank_count to find whether card is paired or unpaired by odd nummber condition
        if len(cards) % 2 == 1:
            no_pairs.extend(cards[:1])

    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''(list)-None
    Prints elements of a given list deck separated by a space.
    '''
    print(" ".join(deck))


def get_valid_input(n):
    '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
    #infinite loop until breaks
    while True:
        # it handles exception if occurs
        try:
            #it enters number as string and convert to int
            choice = int(input(f"Give me an integer between 1 and {n}: "))
            # it does the condition from 1 to the available numbers of cards whitin choice variable
            if 1 <= choice <= n:
                return choice
            else:
                #if it is not correct number, it pops up the following message
                print(f"Invalid number. Please enter integer between 1 and {n}: ", end="")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def play_game():
    '''()->None
    This function plays the game
    '''
    deck = make_deck()
    shuffle_deck(deck)
    dealer, human = deal_cards(deck)

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards.")
    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()

    dealer = remove_pairs(dealer)
    human = remove_pairs(human)
    turn = "Human"  # Human starts first
    #infinite while loop checking human and dealer list until it gets emtpy
    while len(dealer) > 0 and len(human) > 0:
        if turn == "Human":
            print("\nYour turn.")
            print("Your current deck of cards is:")
            print_deck(human)
            print(f"I have {len(dealer)} cards. If 1 stands for my first card and")
            print(f"{len(dealer)} for my last card, which of my cards would you like?")

            #according to dealer deck, it prompts users input and insure it is within the range with (-1)
            card_index = get_valid_input(len(dealer)) - 1
            selected_card = dealer.pop(card_index)
            print(f"You asked for my {card_index + 1} card.")
            print(f"Here it is. It is {selected_card}")

            #it adds selected cards to the list of selected_cards for human
            human.append(selected_card)
            print("With", selected_card, "added, your current deck of cards is:")
            print_deck(human)

            #it removes discarding pairs and give turn to robot
            human = remove_pairs(human)
            print("And after discarding pairs and shuffling, your deck is:")
            print_deck(human)
            turn = "Robot"
            wait_for_player()

        else:
            print("\nMy turn.")
            #with the assist of random funciton, it randomly picks a card from human list
            selected_card = random.choice(human)
            #remove it from human list
            human.remove(selected_card)
            #add it to dealer list
            dealer.append(selected_card)

            dealer = remove_pairs(dealer)
            print(f"I took your {random.randint(1, len(human) + 1)} card.")
            turn = "Human"
            wait_for_player()
    #when human list or dealer list get empty (finish cards), for either of them congragulaiton message will be printed
    if len(human) == 0:
        print("Ups. You do not have any more cards.")
        print("Congratulations! You, Human, win!")
    else:
        print("Ups. I do not have any more cards.")
        print("Congratulations! I, Robot, win!")


play_game()
