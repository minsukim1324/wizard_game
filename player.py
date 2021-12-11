"""
Contains the functions all about the players in the card game wizard

"""

__author__ = "7389272, Kim, 7614343, Kang"
__email__ = "s8158863@rz.uni-frankfurt.de" 

from typing import Tuple, List, Dict

def list_of_player(players = int) -> List[str]:
    """
    creates a list with all the names of the players

    :param number_of_players: gives the amount of player who is playing the game
    :return: [(int,str)] - returns a list with the names as strings
    :rtype [(str)]
    """
    list_of_players = []
    for i in range(players):  
        while True:
            try:
                names = str(input("Bitte Name des Spielers eingeben: "))
                list_of_players.append(names)
                if names == "":
                    raise ValueError
                break
            except ValueError:
                print("Bitte nur Buchstaben eingeben!!")
    return list_of_players

def create_player_trick(players,dict_of_players={}):

    """
    creates a dictionairy with the names as a key and the trick as the value

    :param number_players: gives the number of players that are playing 
    :param list_of_player: gives a list of playernames
    :return {(str : int)} - returns a dictionary with the name and the number of tricks
    :rtype {(str : int)}
    """

    for i in range (1, players + 1):
        dict_of_players.update({i : 0})
    
    return dict_of_players


def add_points(dict_of_player: Dict,list_of_winner: List[int]):
    for i in range (0,len(list_of_winner)):
        dict_of_player[list_of_winner[i]]+=1

    return dict_of_player


def winner_names(list_of_player: List[str],list_of_winner: List[int]):
    x = []

    for i in range (len(list_of_winner)):
        x.append(list_of_player[list_of_winner[i]-1])
    
    return x



if __name__=="__main__":
    a = ["zion","minsu","asdfasdf"]
    b = [3]
    print(winner_names(a,b))

