"""
Contains a part of the functions for ERP04, EPR05.

This file may only be used in Tutorium 04 & 22.
"""

__author__ = "Lukas, Patrick"

from typing import Tuple, List


def create_card_list(number_of_cards: int) -> List[Tuple[int, str]]:
    """
    creates a list of tuple's (cards), with the colors green, red, yellow, blue (in german) and of
    the range 1 to number_of_cards.

    :param number_of_cards: number card of each type of cards
    :return: [(int, str)] - list of all the card for a game, len of the list is number_of_cards * 4
    """
    list_cards = []
    for i in range(1, number_of_cards + 1):
        for j in ["grün", "gelb", "blau", "rot"]:
            list_cards.append((i, j))
    return list_cards


def bigger_card(card_one: Tuple[int, str], card_two: Tuple[int, str], trump: str) -> int:
    """
    returns a number with declares if card_one is bigger than the other

    :param card_one: first card, contains value and the color
    :type card_one: (int, str)
    :param card_two: second card, contains value and the color
    :type card_two: (int, str)
    :param trump: str - color with has a bigger weight than the others
    :return: number - 0: if card_one is lower than card_two
                      1: if card_one is equal card_two
                      2: if card_one is bigger than card_two
    """

    if card_one[1] == trump:
        # card one is trump
        if card_two[1] == trump:
            # card two is trump, check bigger number of both cards
            if card_one[0] > card_two[0]:
                return 2
            if card_one[0] == card_two[0]:
                return 1
            return 0
        # card two is no trump -> card one is bigger
        return 2
    if card_two[1] == trump:
        # card one no trump & card two is trump -> card two is bigger
        return 0
    # no trump card - only value
    if card_one[0] > card_two[0]:
        return 2
    if card_one[0] == card_two[0]:
        return 1
    return 0


def deal_cards(list_cards: List[Tuple[int, str]],
               players: int,
               number_of_cards: int) -> List[List[Tuple[int, str]]]:
    """
    deals the cards of the deck to the players

    :param list_cards: shuffled list
    :param players: number of players, with get cards
    :param number_of_cards: number of card per player
    :return: [[(int, str)]] - returns players sublist with the corresponding cards
    :rtype [[(int, str)]]
    """
    return_list = []
    for i in range(players):
        return_list.append(list_cards[i * number_of_cards:i * number_of_cards + number_of_cards])
    return return_list



def remaining_cards(list_cards: List[Tuple[int, str]],
                    number_of_cards: int,
                    number_of_player: int) -> List[Tuple[int, str]]:
    """ Specifies the remaining cards after dealing.
    :param list_cards: the complete card deck
    :param number_of_cards: cards per player
    :param number_of_player: amount of player
    :return: remaining cards
    """
    return list_cards[number_of_player*number_of_cards:]





if __name__ == '__main__':
    pass