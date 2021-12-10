"""
This program is a card game which is very similar to the card game wizard.

"""
__author__ = "7389272, Kim",",Kang"
__email__ = "s8158863@rz.uni-frankfurt.de" 

import random 
from typing import Tuple, List, Dict
import cards

def shuffle_deck(list_cards: List[Tuple[int, str]]) -> List[List[Tuple[int, str]]]:
    """
    shuffles the given deck

    :param list_cards: list of cards 
    :return [(int,str)] - returns the shuffled list
    :rtype [(int,str)]
    """

    random.shuffle(list_cards)
    return list_cards


def deal_cards_per_round(list_cards: List[Tuple[int, str]],round: int,player: int) -> List[List[Tuple[int, str]]]:
    """
    deal cards pending on which round is playing 

    :param list_cards: list of cards
    :param players: number of players, with get cards
    :param round: number of the round which is playing
    :return: [[(int, str)]] - returns players sublist with the corresponding cards
    :rtype [[(int, str)]]
    """
    return_list = cards.deal_cards(list_cards,player,round)

    return return_list


def hand_cards(dealt_cards):
    """
    
    
    """

    hand_cards = {}
    for i in range (len(dealt_cards)):
        hand_cards.update({i + 1: dealt_cards[i]})

    return hand_cards

def get_hand_cards(all_handcards: Dict, player_number: int) -> List[Tuple[int,str]]:
    """
    
    """

    return all_handcards.get(player_number, "Invalid name")


def laying_cards(hand_cards: List[Tuple[int,str]],index_of_card: int):
    """
    
    """

    return_cards = hand_cards[index_of_card]
    hand_cards.remove(hand_cards[index_of_card])

    return return_cards



def card_compare (list_of_played_cards: List, players: int, trumpf: str):
    """
    
    
    """

    winnerlist = []
    winnerlist.append(list_of_played_cards[0])
    a = winnerlist[0]
    for i in range(1,(players)):
        b = list_of_played_cards[i]
        a = winnerlist[0]
        x = cards.bigger_card(a,b,trumpf)
        if x == 0:
            del winnerlist [:]
            winnerlist.append(list_of_played_cards[i])
        elif x == 1:
            winnerlist.append(list_of_played_cards[i])
        else: 
            x == 2
            continue
    return winnerlist


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


if __name__ == "__main__":
    a = [("rot", 1)]
    b = {1 : [("rot", 1),("rot", 2)], 2 : [("rgruen", 1),("adfasdf", 2)]}
    c = [1,2]

    print(winner(a,b,c))

    
    

