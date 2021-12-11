"""
This program is a card game which is very similar to the card game wizard.

"""
__author__ = "7389272, Kim, 7614343, Kang"
__email__ = "s8158863@rz.uni-frankfurt.de" 


import random 
import cards
import second_part_cards
import copy
import player
import sys

#ToDo bots und Benutzerschnittstelle mit Anfrage und Hilfestellungen
#robust mit eingabe 
#exit restart the game 


def wizard():
    
    #number of players who is playing the game possible answer 2-5
    while True:
        try:
            print("Dieses Spiel können von 2 bis 5 Spieler spielen")
            players = int(input("Anzahl der Spieler: "))
            if players > 5 or players < 2:
                raise ValueError
            break
        except ValueError:
            print("Bitte eine ganze Zahl zwischen 2 bis 5!!")
            print("")

    #decide which output the game will give 
    print("Welche Gewinnmöglichkeit möchten sie wählen")
    print("")
    print("Für meisten Stiche gewonnen geben Sie 't' ein")
    print("Für die meisten gewonnenen Runden geben Sie 'r' ein")
    while True:
        try:
            winner_output = str(input("Geben sie ihre Wahl ein:"))
            if winner_output == 't' or winner_output == 'r':
                break
            else:
                raise ValueError
        except ValueError:
            print("Bitte nur tricks oder rounds eingeben")
    
    
    #list with the names in it
    list_of_players = player.list_of_player(players)


    #dict with player num and trick(trick is 0 at the beginning)
    player_trick = player.create_player_trick(players)

    #dict with player num and number of rounds won (at the beginning = 0)
    player_round = copy.deepcopy(player_trick)
    
    #startplayer
    starting_num = random.randint(0,players - 1)

    #max rounds
    #max_rounds = (60 - 1) // players
    max_rounds = 2 #Testfall
#Schleife start
#round start

    for round in range(1,max_rounds + 1):
        print("")
        print("")
        print("Round",round,"is starting")
        print("")

        #complete card deck
        complete_deck = cards.create_card_list(15)

        #startplayer
        startplayer = list_of_players[starting_num]
        print("Der Spieler",startplayer,"startet die Runde")
        print("")
        
        #shuffle cards
        shuffled_deck = second_part_cards.shuffle_deck(complete_deck)

        #dealing cards to the player
        dealt_cards = cards.deal_cards(shuffled_deck,players,round)

        #set trumpcard
        remaining_deck = cards.remaining_cards(shuffled_deck,round,players)
        trump_colour = second_part_cards.get_trump(remaining_deck)
        print("Das ist die Trumpffarbe: ", trump_colour)
        print("")
        

        #seperate the hand cards into the player number
        dict_handcards = second_part_cards.hand_cards(dealt_cards) 
        copy_dict_handcards = copy.deepcopy(dict_handcards)

        #playing cards
        #first print whos turn it is and which card would the player lay
        #pool is the list where all the cards will come in
        pool = []
        while len(dict_handcards[starting_num + 1])> 0:

            for n in range(players):
                print("Spieler ",list_of_players[starting_num],"ist dran")
                print(second_part_cards.get_hand_cards(dict_handcards, starting_num + 1))
                print("")

                #add card that are layed 
                print("Der Kartenindex wird mit einer Ganzzahl angegeben")
                print ("Sie sagt aus an welcher Stelle die Karte steht(0.Stelle,1.Stelle,...)")
                print("Für einen neustart, geben Sie bitte 100 ein")
                print("")
                print("")
                
                while True:
                    try:
                        card_index = int(input("Kartenindex angeben(oder 100): "))
                        
                        #if card_index == 100:
                            #here comes the funktion to quit the program
                            #print("Sie haben das Spiel neu gestartet...")
                            #dont know how to quit the programm 
          
                        if card_index > round - 1 or card_index < 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Bitte den index der Karte eingeben(Es startet bei 0)")
                        print("")
                        print("")
                
                #laying the selected card in the pool
                pool.append(second_part_cards.laying_cards(dict_handcards[starting_num + 1],card_index))

                #increase starting_num with 1 so the next player can make his move 
                starting_num += 1
                if starting_num == players: #if the max player is reached the first player have to move again 
                    starting_num = 0
                
                print("Es wurden diese Karten gelegt")
                print(pool)
                for d in range(3):
                    print("")
            
            #compare cards
            #liste of the keys of dict_handcards
            keys_handcards = list(dict_handcards)
            

            #liste of all winning cards in this round
            winner_cards = second_part_cards.card_compare(pool,players,trump_colour)
            

            #liste of all winner this round
            winner_this_trick = second_part_cards.winner(winner_cards,copy_dict_handcards,keys_handcards)

            #name
            #namen ausgeben vom gewinner
            winner_names = player.winner_names(list_of_players, winner_this_trick)
            print("Gewinner dieses Stiches ist")
            print(winner_names)
            print("")
            print("")

            #add up trick
            trick_result = player.add_points(player_trick, winner_this_trick)
            print("Derzeitiger Stand",trick_result)
            print("")
            print("")

             #reset evrything
            starting_num += 1
            if starting_num == players:
                    starting_num = 0

            #clear pool for the new trick
            pool.clear()
            
        #decide the round winner who has the most tricks
        round_winner = second_part_cards.end_winner(player_trick)
        round_winner_names = player.winner_names(list_of_players,round_winner)

        #add one point to the winner or winners in the name_round dictionairy
        player.add_points(player_round, round_winner)
        
        #print the roundwinners name
        print("Der Gewinner dieser Runde ist")
        print (round_winner_names)
        for f in range(5):
            print("")
            

           

    #GanzGewinner definieren

    #if funktion für die Auswahl des Gewinners
    if winner_output == 't':

        end_winner = second_part_cards.end_winner(player_trick)
        end_winner_names = second_part_cards.winner_names(list_of_players,end_winner)
        if len(end_winner_names)>1:

            print("Die Gewinner sind")
            print(end_winner_names)
        else:
            print("Der Gewinner ist")
            print(end_winner_names)

    else:

        end_winner_round = second_part_cards.end_winner(player_round)
        end_winner_round_names = player.winner_names(list_of_players,end_winner_round)
        if len(end_winner_round_names)>1:

            print("Die Gewinner sind")
            print(end_winner_round_names)
        else:
            print("Der Gewinner ist")
            print(end_winner_round_names)


if __name__ =="__main__":
    wizard()


    

