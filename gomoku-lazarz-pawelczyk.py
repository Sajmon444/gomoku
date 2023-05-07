#GOMOKU - Szymon Pawełczyk, Szymon Łazarz
#mapa od (1,1) do (15,15) wpisujemy współrzędne od 1 do 15 x i y

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

    # Sprawdzenie przekątnych "/"
    # Zaczynamy sprawdzać w wieszu 5 mapy, sprawdzamy po przekątnej w górę w prawą stronę, po czym przesuwamy się o jedno w prawo i znowu sprzawdzamy przekątną. Następnie, gdy w danym wierszu nie ma więcej możliwości, to idziemy jeden wiersz w dół i znowu sprzawdzamy.
    for i in range(4, size): #pętla powtarza się tyle razy, ile wysokość planszy, zaczynając od 4, ponieważ wcześniej nie zmieści się 5 takich samych znaków
        for j in range(size-4): #pętla powtarza się tyle razy ile szerokość planszy -4, ponieważ inaczej w warunku poniżej wyjdziemy za listę
            if [gracze[i-k][j+k] for k in range(5)] == [gracz]*5: #tworzymy listę 5 elementów (zaczynamy na jakimś indeksie listy, a poźniej skaczemy o jedno w prawo i jedno w górę) i sprawdzamy, czy ma 5 znaków X lub O
                print(Fore.WHITE, "Gracz", gracz, "wygrał!", end="")
                quit()
    # Sprawdzenie przekątnych "\"
    # Zaczynamy sprawdzać w początku mapy (punkt 1,1), sprawdzamy po przekątnej w dół w prawą stronę, po czym przesuwamy się o jedno w prawo i znowu sprzawdzamy przekątną. Następnie, gdy w danym wierszu nie ma więcej możliwości, to idziemy jeden wiersz w dół i znowu sprzawdzamy.
    for i in range(size-4): #pętla powtarza się tyle razy ile wysokość -4, ponieważ niżej nie może już być 5 takich samych elementó po skosie
        for j in range(size-4): #pętla powtarza się tyle razy ile szerokość, a odejmujemy 4, żeby w warunku niżej nie wyjść poza listę
            if [gracze[i+k][j+k] for k in range(5)] == [gracz]*5: #tworzymy listę 5 elementów (zaczynamy na jakimś indeksie listy, a poźniej skaczemy o jedno w prawo i jedno w dół) i sprawdzamy, czy ma 5 znaków X lub O
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
        
        if gracz == "X": print(Fore.GREEN,"Gracz X\n")
        else: print(Fore.RED,"Gracz O\n")

        sprawdzanie=True
        while sprawdzanie==True :    
            x = int(input("Podaj x: "))
            y = int(input("Podaj y: "))
            if x>=1 and x<=15 and y>=1 and x<=15:
                if gracze[y-1][x-1]!="X" and  gracze[y-1][x-1]!="O" :
                
                  sprawdzanie=False
        
        gracze[y-1][x-1] = gracz
        sprawdz_wygrana(gracze, gracz)    
        if gracz =="X":
            gracz="O"
            

        elif gracz=="O":
            gracz="X"
        sprawdz_wygrana(gracze, gracz)    
          

        


