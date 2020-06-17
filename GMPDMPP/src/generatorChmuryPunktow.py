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

rozmiarX=500
rozmiarY=500

rozdzielczoscKol=1
rozdzielczoscProstokatow=1
rozdzielczoscKolWewn=1

arrKrawedziX=[]
arrKrawedziY=[]

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


    #DO ZNAJDYWANIA PUNKTOW PRZEJSCIOWYCH
    arrKrawedziX.append(wspolrzednaXList[i]+A/2)
    arrKrawedziY.append(wspolrzednaYList[i]+B/2)
    arrKrawedziX.append(wspolrzednaXList[i]-A/2)
    arrKrawedziY.append(wspolrzednaYList[i]+B/2)
    arrKrawedziX.append(wspolrzednaXList[i]-A/2)
    arrKrawedziY.append(wspolrzednaYList[i]-B/2)
    arrKrawedziX.append(wspolrzednaXList[i]+A/2)
    arrKrawedziY.append(wspolrzednaYList[i]-B/2)



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
      

            #DO ZNAJDYWANIA PUNKTOW PRZEJSCIOWYCH
            arrKrawedziX.append(wspolrzednaXList[i]-A/2+(x*2+1)*A/mianownik)
            arrKrawedziY.append(wspolrzednaYList[i]+B/2)
            arrKrawedziX.append(wspolrzednaXList[i]-A/2+(x*2+1)*A/mianownik)
            arrKrawedziY.append(wspolrzednaYList[i]-B/2)
      

        iteracjaA=iteracjaA+1
        odlegloscA=odlegloscA/2
    while odlegloscB>rozdzielczoscProstokatow:
        mianownik=pow(2,(iteracjaB))
        for x in range(0,pow(2,(iteracjaB)-1)):
            arrPunktowX.append(wspolrzednaXList[i]+A/2)
            arrPunktowY.append(wspolrzednaYList[i]-B/2+(x*2+1)*B/mianownik)
            arrPunktowX.append(wspolrzednaXList[i]-A/2)
            arrPunktowY.append(wspolrzednaYList[i]-B/2+(x*2+1)*B/mianownik)    
        

            #DO ZNAJDYWANIA PUNKTOW PRZEJSCIOWYCH
            arrKrawedziX.append(wspolrzednaXList[i]+A/2)
            arrKrawedziY.append(wspolrzednaYList[i]-B/2+(x*2+1)*B/mianownik)
            arrKrawedziX.append(wspolrzednaXList[i]-A/2)
            arrKrawedziY.append(wspolrzednaYList[i]-B/2+(x*2+1)*B/mianownik)    
        

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



def rysujOkrag(promien, czyKrawedz):
    kat=0
    krok=90
    odleglosc=999
    while odleglosc>rozdzielczoscKol:
        while kat<360:
            arrPunktowX.append(promien*math.cos(kat*math.pi/180)+wspolrzednaXList[i])
            arrPunktowY.append(promien*math.sin(kat*math.pi/180)+wspolrzednaYList[i])
            
            #DO ZNAJDYWANIA PUNKTOW PRZEJSCIOWYCH
            if czyKrawedz=='y':
                arrKrawedziX.append(promien*math.cos(kat*math.pi/180)+wspolrzednaXList[i])
                arrKrawedziY.append(promien*math.sin(kat*math.pi/180)+wspolrzednaYList[i])
            kat=kat+krok
        krok=krok/2
        kat=krok
        odleglosc=krok/360*2*math.pi*promien
        

for x in range(0, len(wierzcholkiPrzeszkodaList)):
    typ=przeszkodaTypList[x]
    i=wierzcholkiPrzeszkodaList[x]

    if typ=='o':#przeszkoda jest okregiem 
        promien=promienList[i]
        print("wierzcholek", x, ", X:",wspolrzednaXList[i],", Y:",wspolrzednaYList[i], ", r: ", promien)
        arrPunktowX.append(wspolrzednaXList[i])#srodek X
        arrPunktowY.append(wspolrzednaYList[i])#srodek Y
        #W tej funkcji dodawane sa punkty na okregu
        rysujOkrag(promien,'y')
        odlegloscWSrodku=promien
        #W tym while dodawane sa punkty wewnatrz okregu (czyli punkty na okregu o mniejszym promieniu)
        iteracjaSrodka=1
        #while odlegloscWSrodku>rozdzielczoscKolWewn:
        for x in range (1,promien-1):
            rysujOkrag(x,'n')
    else:#przeszkoda jest kwadratem
        A=bokA[i]
        B=bokB[i]
        print("wierzcholek", x, ", X:",wspolrzednaXList[i],", Y:",wspolrzednaYList[i])
        arrPunktowX.append(wspolrzednaXList[i])#srodek X
        arrPunktowY.append(wspolrzednaYList[i])#srodek Y
        rysujProstokatv2(A,B)

tablica2D = [[0] * rozmiarX for i in range(rozmiarY)]
for i in range(0, len(arrPunktowX)):
    tablica2D[math.floor(arrPunktowX[i])][math.floor(arrPunktowY[i])]=255
#print(tablica2D)

print("Wszystkie punkty: ",len(arrPunktowX),", punkty na krawedzi: ",len(arrKrawedziX))



for i in range(0, rozmiarX):
    print(i)
    for j in range(0, rozmiarY): 
        if tablica2D[i][j]==0:
            if i%3==1 and j%3==1:
                #na poczatku przypisuje jakas wysoka
                odlegloscOdWysokiego=10000
                ###for przejezdza po wszystkich punktach z arrPunktowX i arrPunktowY
                for x in range(0, len(arrKrawedziX)):
                    #Dla każdego ze sprawdzanych punktów liczy odległość jeszcze raz
                    odlegloscTmp=math.sqrt(((arrKrawedziX[x]-i)*(arrKrawedziX[x]-i))+((arrKrawedziY[x]-j)*(arrKrawedziY[x]-j)))
                    if odlegloscTmp<odlegloscOdWysokiego:
                        odlegloscOdWysokiego=odlegloscTmp
                        #przypisz 1/wartość do odpowiedniego pola w tablicy 2D (może być * współczynnik)
                        if odlegloscOdWysokiego!=0:
                            wartosc=math.floor(255/(odlegloscOdWysokiego*0.2))
                        if wartosc<255:
                            tablica2D[i][j]=wartosc
                        else:
                            tablica2D[i][j]=255
for i in range(0, rozmiarX):
    print(i)
    for j in range(0, rozmiarY): 
        if tablica2D[i][j]==0:
            #KOPIUJE WARTOŚĆ Z SĄSIEDZTWA
            if i%3==0 and j%3==0 and i<rozmiarX-1 and j<rozmiarY-1:#nie działa
                tablica2D[i][j]=tablica2D[i+1][j+1]
            elif i%3==0 and j%3==1 and j<rozmiarY-1:#nie działa
                tablica2D[i][j]=tablica2D[i+1][j]
            elif i%3==0 and j%3==2 and i!=0 and j<rozmiarY-1:
                tablica2D[i][j]=tablica2D[i+1][j-1]
            elif i%3==1 and j%3==0 and i<rozmiarX-1:
               tablica2D[i][j]=tablica2D[i][j+1]
            elif i%3==1 and j%3==2 and i!=0:
                tablica2D[i][j]=tablica2D[i][j-1]
            elif i%3==2 and j%3==0 and j!=0 and i<rozmiarX-1:
                tablica2D[i][j]=tablica2D[i-1][j+1]
            elif i%3==2 and j%3==1 and j!=0:
                tablica2D[i][j]=tablica2D[i-1][j]
            elif i%3==2 and j%3==2 and j!=0 and i!=0:
                tablica2D[i][j]=tablica2D[i-1][j-1]

# open file for writing
filename = 'x.pgm'
with open(filename, 'w+') as f:
    print('P2', file=f)
    print(rozmiarX," ",rozmiarY,file=f)
    print('255', file=f)
    for i in reversed(range(0,rozmiarX)):
        for j in range(0,rozmiarY): 
            print(tablica2D[j][i]," ",file=f,end="")
        print(" ",file=f)

#df = pd.DataFrame()
#df['x'] = arrPunktowX
#df['y'] = arrPunktowY
#df.head()
#fig, ax = plt.subplots()
#sns.kdeplot(df['x'],df['y'], n_levels=2, shade="True", ax=ax).set_title('Mapa prawdopodobieństwa metodą pól potencjałów')
#sns.kdeplot(df['x'],df['y'], n_levels=2, ax=ax)
#sns.regplot(x=df['x'],y=df['y'], fit_reg=False, ax=ax)
#same punkty z nakladaniem sie
#sns.lmplot( x="x", y="y", data=df, fit_reg=False)
#ten z rozkladem punktow na bokach
#sns.jointplot(x=df["x"], y=df["y"],n_levels=2, kind='kde')
#plt.show()
