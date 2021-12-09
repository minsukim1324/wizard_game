"""
This is a one of the modules for the game wizard.

"""

__author__ = "7389272, Kim",",Kang"
__email__ = "s8158863@rz.uni-frankfurt.de" 

from typing import Tuple, List

def list_of_player(number_of_players = int) -> List[str]:
    """
    creates a list with all the names of the players

    :param number_of_players: gives the amount of player who is playing the game
    :return [(int,str)] - returns a list with the names as strings
    :rtype [(str)]
    """
    list_of_players = []
    for i in range(1,number_of_players + 1):
            
            player_name = str(input("Geben Sie den Namen des Spieler ein: "))
            list_of_players.append(player_name)
    
    return list_of_players

def create_player_trick(number_players,list_of_player,dict_of_players={}):

    """
    creates a dictionairy with the names as a key and the trick as the value

    :param number_players: gives the number of players that are playing 
    :param list_of_player: gives a list of playernames
    :return {(str : int)} - returns a dictionary with the name and the number of tricks
    :rtype {(str : int)}
    """

    for i in range (number_players):
        dict_of_players.update({list_of_player[i] : 0})

    return dict_of_players



if __name__=="__main__":
    print(list_of_player(3))

