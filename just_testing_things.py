import operator
b = 1
c = "aleks"
points = 0
def swith_demo(argument):
    switcher = {
        1: (b,points),
        2: c,
        3: "Mar"
    }
    return switcher.get(argument, "Invalid month")
import random

a=(1, 5)
b=(3, 7)



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

create_player_trick(2)
print("'tricks'" )



