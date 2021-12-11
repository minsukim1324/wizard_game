"""
This program is a card game which is very similar to the card game wizard.

"""
__author__ = "7389272, Kim, 7614343, Kang"
__email__ = "s8158863@rz.uni-frankfurt.de" 

import wizard_game

def main():
    while True:
        wizard_game.wizard()
        try:
            exit = str(input("Wollen sie wirklch das Spiel verlassen? Geben sie 'n' für nein und 'y' für ja ein: "))
        
        except ValueError or exit != "y" or exit != "n":
            print("kein richtige Eingabe bitte geben sie 'y' oder 'n' ein")
            
        
        if exit == "y":
            break
        else:
            continue

if __name__=="__main__":
    main()