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
        hand_cards.update({i + 1 : dealt_cards[i]})

    return hand_cards

def get_hand_cards(all_handcards: Dict, player_number: int) -> List[Tuple[int,str]]:
    """
    
    """

    return all_handcards.get(player_number, "Invalid name")

def laying_cards(hand_cards: List[Tuple[int,str]],index_of_card: int):

    return_cards = hand_cards[index_of_card]
    hand_cards.remove(hand_cards[index_of_card])

    return return_cards


def compare_cards(n):

    for i in range(n):
        cards.bigger_card(pool[n],pool[n+1],trumpf)



if __name__ == "__main__":
    dealt_cards = [[(2,"rot"),(3,"rot")],[(4,"rot"),(5,"gruen")],[(6,"gelb"),(7,"rot")]]
    print(hand_cards(dealt_cards))
    collection_of_handcards = hand_cards(dealt_cards)
    print(get_hand_cards(collection_of_handcards,2))



    
    

