import math
import pandas as pd
#matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import colorbar
import grafListy
import os,sys

wierzcholekAList=[]
wierzcholekBList=[]
#wspolrzednaXList=[40, 9, 81, 83, 100, 22, 32, 16, 43, 65]
#wspolrzednaYList=[99, 70, 59, 87, 100, 54, 78, 24, 32, 44]
#wierzcholkiPrzeszkodaList=[4,6,9,1,3,7]
#przeszkodaTypList=['o','o','o','k','k','k']
#promienList=[0,0,0,0,10,0,8,0,0,17]
#bokA=[0,16,0,16,0,0,0,10,0,0]
#bokB=[0,12,0,10,0,0,0,42,0,0]

#wierzcholkiPrzeszkodaList=[5]
#przeszkodaTypList=['o']
#promienList=[0,0,0,0,10,20,8,0,0,17]
#bokA=[0,8,0,8,0,20,0,5,0,0]
#bokB=[0,6,0,5,0,20,0,21,0,0]

obiekt=grafListy.graf()
obiekt.inicjuj('test.dat')

wspolrzednaXList=obiekt.wspolrzednaXList
wspolrzednaYList=obiekt.wspolrzednaYList
wierzcholkiPrzeszkodaList=obiekt.wierzcholkiPrzeszkodaList
przeszkodaTypList=obiekt.przeszkodaTypList

parametrA=obiekt.parametrPrzeszkodyA
parametrB=obiekt.parametrPrzeszkodyB

promienList=parametrA
bokA=parametrA
bokB=parametrB

arrPunktowX=[]
arrPunktowY=[]

rozdzielczoscKol=4
rozdzielczoscProstokatow=6;

def rysujLiniePozioma(A,xStart,y):
    xStop=xStart+A
    arrPunktowX.append(xStart)
    arrPunktowY.append(y)
    arrPunktowX.append(xStop)
    arrPunktowY.append(y)
    odlegloscA=A
    iteracjaA=1
    while odlegloscA>rozdzielczoscProstokatow:
        mianownik=pow(2,(iteracjaA))
        for x in range(0,pow(2,(iteracjaA)-1)):
            arrPunktowX.append(xStart+(x*2+1)*A/mianownik)
            arrPunktowY.append(y)

        iteracjaA=iteracjaA+1
        odlegloscA=odlegloscA/2


def rysujProstokat(A,B):
    #narysuj rogi
    arrPunktowX.append(wspolrzednaXList[i]+A/2)
    arrPunktowY.append(wspolrzednaYList[i]+B/2)
    arrPunktowX.append(wspolrzednaXList[i]-A/2)
    arrPunktowY.append(wspolrzednaYList[i]+B/2)
    arrPunktowX.append(wspolrzednaXList[i]-A/2)
    arrPunktowY.append(wspolrzednaYList[i]-B/2)
    arrPunktowX.append(wspolrzednaXList[i]+A/2)
    arrPunktowY.append(wspolrzednaYList[i]-B/2)
    odlegloscA=A
    odlegloscB=B
    iteracjaA=1
    iteracjaB=1
    while odlegloscA>rozdzielczoscProstokatow:
        mianownik=pow(2,(iteracjaA))
        for x in range(0,pow(2,(iteracjaA)-1)):
            arrPunktowX.append(wspolrzednaXList[i]-A/2+(x*2+1)*A/mianownik)
            arrPunktowY.append(wspolrzednaYList[i]+B/2)
            arrPunktowX.append(wspolrzednaXList[i]-A/2+(x*2+1)*A/mianownik)
            arrPunktowY.append(wspolrzednaYList[i]-B/2)
        iteracjaA=iteracjaA+1
        odlegloscA=odlegloscA/2
    while odlegloscB>rozdzielczoscProstokatow:
        mianownik=pow(2,(iteracjaB))
        for x in range(0,pow(2,(iteracjaB)-1)):
            arrPunktowX.append(wspolrzednaXList[i]+A/2)
            arrPunktowY.append(wspolrzednaYList[i]-B/2+(x*2+1)*B/mianownik)
            arrPunktowX.append(wspolrzednaXList[i]-A/2)
            arrPunktowY.append(wspolrzednaYList[i]-B/2+(x*2+1)*B/mianownik)    
        iteracjaB=iteracjaB+1
        odlegloscB=odlegloscB/2

def rysujProstokatv2(A,B):
    rysujProstokat(A,B)

    #rysuj linie pionowa, ale zamiast robic dodawanie do tablicy punktow to rysowanie linii poziomej
    xStart=wspolrzednaXList[i]-A/2
    
    yStart=wspolrzednaYList[i]-B/2
    yStop=yStart+B
    odlegloscB=B
    iteracjaB=1
    while odlegloscB>rozdzielczoscProstokatow:
        mianownik=pow(2,(iteracjaB))
        for y in range(0,pow(2,(iteracjaB)-1)):
            rysujLiniePozioma(A,xStart,yStart+(y*2+1)*B/mianownik)
        iteracjaB=iteracjaB+1
        odlegloscB=odlegloscB/2



def rysujOkrag(promien):
    kat=0
    krok=90
    odleglosc=999
    while odleglosc>rozdzielczoscKol:
        while kat<360:
            arrPunktowX.append(promien*math.cos(kat*math.pi/180)+wspolrzednaXList[i])
            arrPunktowY.append(promien*math.sin(kat*math.pi/180)+wspolrzednaYList[i])
            kat=kat+krok
        krok=krok/2
        kat=krok
        odleglosc=krok/360*2*math.pi*promien
        
def obliczRozmiary():

    najwieksza_x = math.ceil(max(wspolrzednaXList)/10)*10+20
    najwieksza_y = math.ceil(max(wspolrzednaYList)/10)*10+20

    return [0,najwieksza_x,0,najwieksza_y]

rozmiary = obliczRozmiary()

#
#                Program główny
#



for x in range(0, len(wierzcholkiPrzeszkodaList)):
    typ=przeszkodaTypList[x]
    i=wierzcholkiPrzeszkodaList[x]

    if typ=='o':#przeszkoda jest okregiem 
        promien=promienList[i]
        print("wierzcholek", x, ", X:",wspolrzednaXList[i],", Y:",wspolrzednaYList[i], ", r: ", promien)
        arrPunktowX.append(wspolrzednaXList[i])#srodek X
        arrPunktowY.append(wspolrzednaYList[i])#srodek Y
        #W tej funkcji dodawane sa punkty na okregu
        rysujOkrag(promien)
        odlegloscWSrodku=promien
        #W tym while dodawane sa punkty wewnatrz okregu (czyli punkty na okregu o mniejszym promieniu)
        iteracjaSrodka=1
        while odlegloscWSrodku>rozdzielczoscKol:
                for x in range (0,pow(2,(iteracjaSrodka-1))):
                    rysujOkrag(promien*(2*x+1)/(pow(2,iteracjaSrodka)))
                odlegloscWSrodku=odlegloscWSrodku/math.pi
                iteracjaSrodka=iteracjaSrodka+1
        #jesli wieksza niz rozdzielczosc to dodaj pomiedzy srodkiem a punktami na luku
        #po wyjsciu z while (dobra rozdzielczosc w srodku) przeszkoda jest gotowa
    else:#przeszkoda jest kwadratem
        A=bokA[i]
        B=bokB[i]
        print("wierzcholek", x, ", X:",wspolrzednaXList[i],", Y:",wspolrzednaYList[i])
        arrPunktowX.append(wspolrzednaXList[i])#srodek X
        arrPunktowY.append(wspolrzednaYList[i])#srodek Y
        rysujProstokatv2(A,B)

#macierz 
rozmiarX = rozmiary[1]
rozmiarY = rozmiary[3]


tablica2D = [[0] * rozmiarX for i in range(rozmiarY)]
for i in range(0, len(arrPunktowX)):
    tablica2D[math.floor(arrPunktowX[i])][math.floor(arrPunktowY[i])]=1
#print(tablica2D)


# open file for writing 
filename = 'x.pgm'
with open(filename, 'w+') as f:
    print('P1', file=f)
    print(rozmiarX," ",rozmiarY,file=f) 
    for i in range(0, rozmiarX):
        for j in range(0, rozmiarY): 
            print(tablica2D[i][j]," ",file=f,end="")
        print(" ",file=f)
df = pd.DataFrame()

df['x'] = arrPunktowX
df['y'] = arrPunktowY



    

df.head()



fig, ax = plt.subplots()

ax.set_xlim(rozmiary[0],rozmiary[1])
ax.set_ylim(rozmiary[2],rozmiary[3])

sns.kdeplot(df['x'],df['y'], n_levels=2, shade="True", ax=ax).set_title('Mapa prawdopodobieństwa metodą pól potencjałów')

sns.kdeplot(df['x'],df['y'], n_levels=2, ax=ax)

sns.regplot(x=df['x'],y=df['y'], fit_reg=False, ax=ax)


#plt.streamplot(df['x'],df['y'])
#streamplot - histogram przepływu

#same punkty z nakladaniem sie
sns.lmplot( x="x", y="y", data=df, fit_reg=False)

#ten z rozkladem punktow na bokach
sns.jointplot(x=df["x"], y=df["y"],n_levels=2, kind='kde')


plt.show()
