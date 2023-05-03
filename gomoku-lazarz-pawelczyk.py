import os
from colorama import Fore, Back

def mapa(tablica_graczy):
    #os.system('cls')

    narozniki={
        "znak1": "┌",
        "znak2": "┐",
        "znak3": "├",
        "znak4": "┤",
        "znak5": "└",
        "znak6": "┘",
        "znak7": "┬",
        "znak8": "┼",
        "znak9": "┴"
    }
    linie={
        "poziom": "─",
        "pion": "│"
    }

    size = len(tablica_graczy)
    poziomeLinie = [linie["poziom"]*3]*size
    poziomWdol = narozniki["znak7"].join(poziomeLinie)
    poziomSrodek = narozniki["znak8"].join(poziomeLinie)
    poziomWgore = narozniki["znak9"].join(poziomeLinie)

    print(Fore.WHITE,narozniki["znak1"]+poziomWdol+narozniki["znak2"]+"\n",end="",sep="")

    for i,wiersz in enumerate(tablica_graczy):
        print(Fore.WHITE,linie["pion"],end="",sep="")
        for j in wiersz:
            if j=="X":
                print(Fore.GREEN," X ",end="",sep="")
            elif j=="O":
                print(Fore.RED," O ",end="",sep="")
            else:
                print(Fore.WHITE,"   ",end="",sep="")
            print(Fore.WHITE,linie["pion"],end="",sep="")
        print()
        if i<size-1:
            print(Fore.WHITE,narozniki["znak3"]+poziomSrodek+narozniki["znak4"]+"\n",end="",sep="")
    print(Fore.WHITE,narozniki["znak5"]+poziomWgore+narozniki["znak6"]+"\n",end="",sep="")





if __name__ == "__main__":
    rozmiar = 15
    gracze = []
    for i in range(rozmiar):
        kolumna = [0 for i in range(rozmiar)]
        gracze.append(kolumna)
    mapa(gracze)


    gracz = "X"
    while True:
        mapa(gracze)
        if gracz == "X": print(Fore.GREEN,"Gracz 1\n")
        else: print(Fore.RED,"Gracz 2\n")

        sprawdzanie=True
        while sprawdzanie==True :    
            x = int(input("Podaj wsp x: "))
            y = int(input("Podaj wsp y: "))
            if gracze[y][x]!="X" and  gracze[y][x]!="O":
                
                sprawdzanie=False
        gracze[y][x] = gracz
        if gracz =="X":
            gracz="O"
        elif gracz=="O":
            gracz="X"
