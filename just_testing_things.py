
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
"""
d = 0
players_info = {b : [("rot", 1),("rot", 2)], c : 0}
players_info[b]
players_info.update()

print(players_info[b][1])


e = ("rot",2)
"""
print(swith_demo(2))