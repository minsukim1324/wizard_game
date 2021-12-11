"""
Contains the functions for the cards in wizard

"""
__author__ = "7389272, Kim, 7614343, Kang"
__email__ = "s8158863@rz.uni-frankfurt.de" 

import random 
from typing import Tuple, List, Dict
import cards
import operator



def shuffle_deck(list_cards: List[List[Tuple[int, str]]]) -> List[List[Tuple[int, str]]]:
    """
    shuffles the given deck

    :param list_cards: list of cards 
    :return: [(int,str)] - returns the shuffled list
    :rtype [(int,str)]
    """

    random.shuffle(list_cards)
    return list_cards



def hand_cards(dealt_cards: List) -> Dict:
    """
    returns a dictionary with int as a key from 1 to max num of the players that are playing
    and a list of cards that were dealt to them.
    
    :param dealt_cards: list of all dealt cards for each player
    :return: {int : [(int,str)]} - returns a dictonary for each player with their hand cards as the value
    :rtype {int : [(int,str)]}
    """

    hand_cards = {}
    for i in range (len(dealt_cards)):
        hand_cards.update({i + 1: dealt_cards[i]})

    return hand_cards

def get_hand_cards(all_handcards: Dict, player_number: int) -> List[Tuple[int,str]]:
    """
    returns the value(handcards) of a certain key(number of the player) in the given dictionary

    :param all_handcards: dictionary with all handcards from all playerself
    :param player_number: is the number of the player (i.e first player -> 1)
    :return: [(int,str)] -  returns handcards of the player
    :rtype [(int,str)]
    """

    return all_handcards.get(player_number)


def laying_cards(hand_cards: List[Tuple[int,str]],index_of_card: int):
    """

    
    """

    return_cards = hand_cards[index_of_card]
    hand_cards.remove(hand_cards[index_of_card])

    return return_cards



def card_compare(list_of_played_cards: List, players: int, trumpf: str):
    """
    
    
    """

    winner_list = []
    winner_list.append(list_of_played_cards[0])
    a = winner_list[0]
    for i in range(1,(players)):
        b = list_of_played_cards[i]
        a = winner_list[0]
        x = cards.bigger_card(a,b,trumpf)
        if x == 0:
            del winner_list [:]
            winner_list.append(list_of_played_cards[i])
        elif x == 1:
            winner_list.append(list_of_played_cards[i])
        else: 
            x == 2
            continue
    return winner_list


def get_trump(reamaining_deck: List[Tuple[int,str]]):
    """
    returns the colour of the trump card

    """
    trump_card = reamaining_deck[0]
    
    return trump_card[1]


def winner(winner_cards: List[Tuple[int,str]],dict_handcards: Dict,list_keys: List[int]):
    """


    """
    winner_list = []
    for x in range(0,len(winner_cards)):

        for i in range(1,len(list_keys)+1):
            
            if winner_cards[x] in dict_handcards[i]:
                winner_list.append(list_keys[i-1])
                break
            
            else:
                continue

    return winner_list


def end_winner(player_trick: Dict):
    """
    return the player who has the most tricks
    """
    sorted_list = sorted(player_trick.items(), key=operator.itemgetter(1))
    sorted_list.reverse()

    end_winner = []
    end_winner.append(sorted_list[0][0])
    for i in range(len(sorted_list)-1):
        if sorted_list[i][1] == sorted_list[i+1][1]:
            end_winner.append(sorted_list[i+1][0])
            continue
        else: 
            break

    return end_winner


if __name__ == "__main__":
    a = [("rot", 1)]
    b = {1 : [("rot", 1),("rot", 2)], 2 : [("rgruen", 1),("adfasdf", 2)]}
    c = [1,2]

    print(winner(a,b,c))

    
    

