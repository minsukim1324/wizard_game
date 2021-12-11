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
player_trick={1:5,2:3,3:6}
sorted_list = sorted(player_trick.items(), key=operator.itemgetter(1))
print(sorted_list)

