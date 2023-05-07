import os
from colorama import Fore, Back

def mapa(tablica_graczy):
    os.system('cls')

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


def sprawdz_wygrana(gracze, gracz):
    size = len(gracze)
    # Sprawdzenie wierszy  
    for i in range(size):  #petla powtarzająca się tyle razy ile wysokość planszy
        for j in range(size-4): #petla powtarzająca się tyle razy ile szaerokość planszy -4 ponieważ później nie bedzie 5 elemntów tych samych
            
            if [gracze[i][j+k] for k in range(5)]==[gracz]*5:  #tworzy liste z 5 kolejnych elemtnów w wierszu i przyrównuje ja do listy 5 elemtnów X lub O 
                
                print(Fore.WHITE, "Gracz", gracz, "wygrał!", end="")
                quit()
    # Sprawdzenie kolumn
    for i in range(size-4):  #petla powtarzająca się tyle razy ile wysokość planszy -4 poniewaz niżej nie bedzie już 5 taki samych elemtnów
        for j in range(size):
           
            if [gracze[k][j] for k in range(i,i+5)] == [gracz]*5: # sprawdza wszystkie kombinace w każej kolumnie i sprawdza czy powstała lista zawiera same X albo O 
                print(Fore.WHITE, "Gracz", gracz, "wygrał!", end="")
                quit()


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
            if x>=0 and x<=14 and y>=0 and x<=14:
                if gracze[y][x]!="X" and  gracze[y][x]!="O" :
                
                  sprawdzanie=False
        
        gracze[y][x] = gracz
        sprawdz_wygrana(gracze, gracz)    
        if gracz =="X":
            gracz="O"
            

        elif gracz=="O":
            gracz="X"
        sprawdz_wygrana(gracze, gracz)    
          

        


