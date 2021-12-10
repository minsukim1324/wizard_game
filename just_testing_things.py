
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


players_info = {1 : [("rot", 1),("rot", 2)], 2 : [("rgruen", 1),("adfasdf", 2)], 3:[("rgru", 1),("adsdf", 2)], 4:[("ren", 1),("asdf", 2)]}
c = [("rot", 1),("rgruen", 1),("ren", 1)]
b = list(players_info)
print(b)
print(len(c))

for x in range(0,len(c)):

    for i in range(1,len(b)+1):

        if c[x] in players_info[i]:
            print (b[i-1])
            
            break
        else:
            continue
    
        




