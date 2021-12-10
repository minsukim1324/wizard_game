"""
This program is a card game which is very similar to the card game wizard.

"""
__author__ = "7389272, Kim",",Kang"
__email__ = "s8158863@rz.uni-frankfurt.de" 


import random 
import cards
import second_part_cards
import copy
import player

#ToDo bots und Benutzerschnittstelle mit Anfrage und Hilfestellungen
#robust mit eingabe 
#exit restart the game 


def wizard():
    
    #number of players who is playing the game 
    players = int(input("Anzahl der Spieler "))
    
    #list with the names in it
    list_of_players = player.list_of_player(players)

    #dict with name and trick(trick is 0 at the beginning)
    player_trick = player.create_player_trick(players)
    
    #startplayer
    starting_num = random.randint(0,players - 1)

    #max rounds
    max_rounds = (60 - 1) // players
#Schleife start
#round start
    for round in range(1,max_rounds + 1):
        print("Round",round,"is starting")

        #complete card deck
        complete_deck = cards.create_card_list(15)

        #startplayer
        startplayer = list_of_players[starting_num]
        print("Der Spieler",startplayer,"startet die Runde")
        
        #shuffle cards
        shuffled_deck = second_part_cards.shuffle_deck(complete_deck)

        #dealing cards to the player
        dealt_cards = cards.deal_cards(shuffled_deck,players,round)

        #set trumpcard
        remaining_deck = cards.remaining_cards(shuffled_deck,round,players)
        trump_colour = second_part_cards.get_trump(remaining_deck)
        print("Das ist die Trumpffarbe", trump_colour)
        
        

        #seperate the hand cards into the player number
        dict_handcards = second_part_cards.hand_cards(dealt_cards) 
        copy_dict_handcards = copy.deepcopy(dict_handcards)

        #playing cards
        #first print whos turn it is and which card would be layed
        #pool is the list where all the cards will come in
        pool = []
        while len(dict_handcards[starting_num + 1])> 0:

            print("Spieler ",list_of_players[starting_num],"ist dran")
            print(second_part_cards.get_hand_cards(dict_handcards, starting_num + 1))
            
            #add card that are layed 
            card_index = int(input("Kartenindex angeben: "))
            pool.append(second_part_cards.laying_cards(dict_handcards[starting_num + 1],card_index))

            starting_num += 1
            if starting_num == players:
                starting_num = 0
            for i in range(5):
                print("")
            print("Es wurden diese Karten gelegt")
            print(pool)
            
            #compare cards
            #liste of the keys of dict_handcards
            keys_handcards = list(dict_handcards)
            

            #liste of all winning cards in this round
            winner_cards = second_part_cards.card_compare(pool,players,trump_colour)
            

            #liste of all winner this round
            winner_this_round = second_part_cards.winner(winner_cards,copy_dict_handcards,keys_handcards)
            print("Das ist der",winner_this_round)


            #name
            #namen ausgeben vom gewinner
            winner_names = player.winner_names(list_of_players, winner_this_round)
            print("Gewinner dieses Stiches ist")
            print(winner_names)

            #add up trick
            result = player.add_trick(player_trick, winner_this_round)
            print("Derzeitiger Stand",result)

            #reset evrything
            starting_num += 1
            if starting_num == players:
                    starting_num = 0
        

#GAnzGewinner definieren

if __name__ =="__main__":
    wizard()


    

