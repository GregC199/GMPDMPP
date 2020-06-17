import math
import pandas as pd
#matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import colorbar
import grafListy
import os,sys
from reportlab.lib.colors import red
from Crypto.Random.random import randrange
from matplotlib.colors import LogNorm

rozdzielczosc_hisogram = 8
rozdzielczoscKol=1
rozdzielczoscProstokatow=1

df = pd.DataFrame()
f = pd.DataFrame()
calosc = pd.DataFrame()

arrNiskiX=[]
arrNiskiY=[]

arrPunktowX=[]
arrPunktowY=[]

wierzcholekAList=[]
wierzcholekBList=[]

caloscX=[]
caloscY=[]

#do rysowania pliku pgm
arrKrawedziX=[]
arrKrawedziY=[]

#
#inicjowanie wczytania grafu
#

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

def wyswietlMenu():
    print("Co chcesz zrobic?", flush=True)
    print("0 - zakoncz prace programu")
    print("1 - wyswietl przeszkody")
    print("2 - wyswietl wykres wykonany w kde")
    print("3 - wyswietl wykres wykonany w seaborn")
    print("4 - wyswietl histogram wykonany przy pomocy biblioteki matplotlib")
    print("5 - wyswietl wyswietl mape punktow wykonana przy pomocy gestosci prawdopodobienstwa")
    print("6 - wyswietl punkty wylosowane przy nalozeniu funkcji rozkladu prawodopobienstwa")
    print("7 - wyswietl histogram")
    print("8 - wyswietl mape w formacie pgm")
    print("9 - wyswietl mape prawdopodobienstwa (moze zajac pare minut..)")    

 # 1 - przeszkody punkty niebieskie, 2 - zielony z konturami, 3 - ???, 4 - to z bokami, 5 - przeszkody punkty + niski potencjał na czerwono
 # 6 - punkty duzo, 7 - histogram, 8 - nie chce sie policzyc ://, 9 - pgm     

def obliczRozmiary():

    najwieksza_x = math.ceil(max(wspolrzednaXList)/10)*10
    najwieksza_y = math.ceil(max(wspolrzednaYList)/10)*10

    print("x max:" , najwieksza_x , "max y" , najwieksza_y)
    return [0,max(najwieksza_x,najwieksza_y),0,max(najwieksza_x,najwieksza_y)]

rozmiary = obliczRozmiary()

rozmiarX = rozmiary[1]
rozmiarY = rozmiary[3]
#
#Przeszkody
#


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
            kat=kat+krok

            
            #DO ZNAJDYWANIA PUNKTOW PRZEJSCIOWYCH
            if czyKrawedz=='y':
                arrKrawedziX.append(promien*math.cos(kat*math.pi/180)+wspolrzednaXList[i])
                arrKrawedziY.append(promien*math.sin(kat*math.pi/180)+wspolrzednaYList[i])
                kat=kat+krok


        krok=krok/2
        kat=krok
        odleglosc=krok/360*2*math.pi*promien
        


#
#                Przeszkody obsługa
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
        #W tej funkcji dodawane sa punkty na okregu
        rysujOkrag(promien,'y')
        odlegloscWSrodku=promien
        #W tym while dodawane sa punkty wewnatrz okregu (czyli punkty na okregu o mniejszym promieniu)
        iteracjaSrodka=1
        for x in range (1,promien-1):
            rysujOkrag(x,'n')
    else:#przeszkoda jest kwadratem
        A=bokA[i]
        B=bokB[i]
        print("wierzcholek", x, ", X:",wspolrzednaXList[i],", Y:",wspolrzednaYList[i])
        arrPunktowX.append(wspolrzednaXList[i])#srodek X
        arrPunktowY.append(wspolrzednaYList[i])#srodek Y
        rysujProstokatv2(A,B)



#
#zapis przeszkod do macierzy
#

tablica2D = [[0] * (rozmiarX) for i in range(rozmiarY)]
for i in range(0, len(arrPunktowX)):
    tablica2D[math.floor(arrPunktowX[i])][math.floor(arrPunktowY[i])]=1
#print(tablica2D)

tablica2DRaw=tablica2D.copy()

def przygotujPlikPgm():
    print("Wszystkie punkty: ",len(arrPunktowX),", punkty na krawedzi: ",len(arrKrawedziX))

    for i in range(0, rozmiarX):
        print(i)
        for j in range(0, rozmiarY): 
            if tablica2DRaw[i][j]==0:
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
                                wartosc=math.floor(255/(odlegloscOdWysokiego*0.1))
                            if wartosc<255:
                                tablica2DRaw[i][j]=wartosc
                            else:
                                tablica2DRaw[i][j]=255
    for i in range(0, rozmiarX):
        print(i)
        for j in range(0, rozmiarY):
            if tablica2DRaw[i][j]==0:
                #KOPIUJE WARTOŚĆ Z SĄSIEDZTWA
                if i%3==0 and j%3==0 and i<rozmiarX-1 and j<rozmiarY-1:#nie działa
                    tablica2DRaw[i][j]=tablica2DRaw[i+1][j+1]
                elif i%3==0 and j%3==1 and j<rozmiarY-1:#nie działa
                    tablica2DRaw[i][j]=tablica2DRaw[i+1][j]
                elif i%3==0 and j%3==2 and i!=0 and j<rozmiarY-1:
                    tablica2DRaw[i][j]=tablica2DRaw[i+1][j-1]
                elif i%3==1 and j%3==0 and i<rozmiarX-1:
                    tablica2DRaw[i][j]=tablica2DRaw[i][j+1]
                elif i%3==1 and j%3==2 and i!=0:
                    tablica2DRaw[i][j]=tablica2DRaw[i][j-1]
                elif i%3==2 and j%3==0 and j!=0 and i<rozmiarX-1:
                    tablica2DRaw[i][j]=tablica2DRaw[i-1][j+1]
                elif i%3==2 and j%3==1 and j!=0:
                    tablica2DRaw[i][j]=tablica2DRaw[i-1][j]
                elif i%3==2 and j%3==2 and j!=0 and i!=0:
                    tablica2DRaw[i][j]=tablica2DRaw[i-1][j-1]

    # open file for writing
    filename = 'x.pgm'
    with open(filename, 'w+') as f:
        print('P2', file=f)
        print(rozmiarX," ",rozmiarY,file=f)
        print('255', file=f)
        for i in reversed(range(0,rozmiarX)):
            for j in range(0,rozmiarY): 
                print(tablica2DRaw[j][i]," ",file=f,end="")
            print(" ",file=f)

########### Niski potencjał

def WyrysujPotencjalNiski(x_wsp,y_wsp,a,b):

    for i in range (x_wsp,x_wsp+a):
        for j in range(y_wsp,y_wsp+b):
            arrNiskiX.append(i)
            arrNiskiY.append(j)

def ZnajdzMiejsceNaPotNiski(wielkosc_pola):
    A=wielkosc_pola
    B=wielkosc_pola
    
    mozliwe_potencjaly_X=[]
    mozliwe_potencjaly_Y=[]
    
    powtorzenie = 0
    
    x_mem = 0
    y_mem = 0
    
    warunek = True
        
    for x in range(1, len(tablica2D[0])-A):
        for y in range(1, len(tablica2D[0])-B):
            for i in range(x,x+A):
                for j in range(y,y+B):
                    if tablica2D[i][j] != 0:
                        warunek = False
                    
            if warunek == False:
                warunek = True
            else:
                mozliwe_potencjaly_X.append(x)
                mozliwe_potencjaly_Y.append(y)
    
    x_mem = mozliwe_potencjaly_X[0]
    y_mem = mozliwe_potencjaly_Y[0]
    print("niski pot srodek", ", X:",x_mem,", Y:",y_mem)
    WyrysujPotencjalNiski(x_mem, y_mem, A, B)
    
    x_mem += A
    y_mem += B
    
    znaleziono = False
    
    for i in range(0,len(mozliwe_potencjaly_X)):
        if znaleziono == False:
            if mozliwe_potencjaly_X[len(mozliwe_potencjaly_X) - i - 1] > x_mem and mozliwe_potencjaly_Y[len(mozliwe_potencjaly_X) - i - 1] > y_mem:
                    x_mem = mozliwe_potencjaly_X[len(mozliwe_potencjaly_X) - i - 1]
                    y_mem = mozliwe_potencjaly_Y[len(mozliwe_potencjaly_X) - i - 1]
                    print("niski pot srodek", ", X:",x_mem,", Y:",y_mem)
                    WyrysujPotencjalNiski(x_mem, y_mem, A, B)
      




#
#Oblsuga potencjalow niskich
#
ZnajdzMiejsceNaPotNiski(10)

#dodanie niskich potencjałów do macierzy
for i in range(0, len(arrNiskiX)):
    tablica2D[math.floor(arrNiskiX[i])][math.floor(arrNiskiY[i])]=-1

#
#tworzenie calosci punktow
#

'''
tutaj rozmycie lub poniżej tej części kodu
'''

losowanie = 0

for i in range(rozmiarX):
    for j in range(rozmiarY):
        
        #print("tablica i:", i, " j:",j)
        if tablica2D[i][j] == -1:
            
            losowanie = randrange(0,math.floor(0.05*rozdzielczosc_hisogram*rozdzielczosc_hisogram))
            tablica2D[i][j] = losowanie
            
            #print("losowanie:",losowanie)
                
                
        elif tablica2D[i][j] == 0:
            
            tablica2D[i][j] = randrange(math.floor(0.34*rozdzielczosc_hisogram*rozdzielczosc_hisogram),math.floor(0.5*rozdzielczosc_hisogram*rozdzielczosc_hisogram))
            
            #print("tablica2D:",tablica2D[i][j])
        
        elif tablica2D[i][j] == 1:
            
            losowanie = randrange(math.floor(0.94*rozdzielczosc_hisogram*rozdzielczosc_hisogram),math.floor(1*rozdzielczosc_hisogram*rozdzielczosc_hisogram))
            tablica2D[i][j] = losowanie
            #print("tablica2D:",tablica2D[i][j])

'''
tutaj rozmycie lub wyżej
'''
    
def Tablica2DxRozdzielczosc(rozdzielczosc):
    
    for x in range(0,rozmiarX):
        for y in range(0, rozmiarY):
            
            powtorzenia = 0
            for i in range(rozdzielczosc*x,rozdzielczosc*x+rozdzielczosc):
                for j in range(rozdzielczosc*y,rozdzielczosc*y+rozdzielczosc):
                    if tablica2D[x][y] > powtorzenia:
                        caloscX.append(i)
                        caloscY.append(j)
                        
                        #print("dodaje punkt i:",i," j:",j)
                        
                        powtorzenia = powtorzenia + 1
                        
Tablica2DxRozdzielczosc(rozdzielczosc_hisogram)


#
#wykresy
#

#przeszkody

#przeszkody zapisane do datafrema
df['x'] = arrPunktowX
df['y'] = arrPunktowY

df.head()

#fig, ax = plt.subplots()

#ax.set_xlim(rozmiary[0],rozmiary[1])
#ax.set_ylim(rozmiary[2],rozmiary[3])

wyswietlMenu()
wybor = int(input("Twoj wybor: "))
while wybor!=0:
    print(wybor)
    if wybor==1:
        #same punkty z nakladaniem sie
        sns.lmplot( x="x", y="y", data=df, fit_reg=False)
        plt.show()

    elif wybor==2:
        sns.kdeplot(df['x'],df['y'], n_levels=2, shade="True").set_title('Rozmieszczenie przeszkód')
        sns.kdeplot(df['x'],df['y'], n_levels=2)
        plt.show()
    elif wybor==3:
        sns.regplot(x=df['x'],y=df['y'], fit_reg=False)
        plt.show()
    elif wybor==4:
        #ten z rozkladem punktow na bokach
        sns.jointplot(x=df["x"], y=df["y"],n_levels=2, kind='kde')
        plt.show()
    elif wybor==5:
        #
        #niskie potencjaly
        #

        f['x'] = arrNiskiX
        f['y'] = arrNiskiY

        f.head()

        fi, a = plt.subplots()
        #wykres rozmiejscowienia przeszkod i niskich potencjalow

        sns.regplot(x=f['x'], y=f['y'], fit_reg=False,color='r', ax=a).set_title('Rozmieszczenie przeszkód(niebieski) i niskich potencjałów(czerwony)')

        sns.regplot(x=df['x'], y=df['y'], fit_reg=False, color='b', ax=a)
        plt.show()
    elif wybor==6:
        #
        #calosc
        #
        calosc['x'] = caloscX
        calosc['y'] = caloscY
        calosc.head()

        '''
        plt.streamplot(calosc['x'],calosc['y'])
        streamplot - histogram przepływu'''

        #punkty
        figure, axes = plt.subplots()

        plt.title('Mapa prawdopodobieństwa punktowa')

        plt.plot(caloscX,caloscY,'.',color='black')
        plt.show()
    elif wybor==7:
        #
        #calosc
        #
        calosc['x'] = caloscX
        calosc['y'] = caloscY
        calosc.head()

        #histogram 2D
        figur, axis = plt.subplots()

        b = axis.hist2d(calosc['x'], calosc['y'],bins=(rozmiarX/2,rozmiarY/2))

        plt.pcolormesh(calosc, shading='gouraud')

        plt.title('Histogram 2D mapy prawdopodobieństwa, 0 - ujemny potencjał, 255 - dodatni potencjał')

        plt.colorbar(b[3], ax=axis)
        plt.show()
    elif wybor==8:
        przygotujPlikPgm()
    elif wybor==9:

        #
        #calosc
        #
        calosc['x'] = caloscX
        calosc['y'] = caloscY
        calosc.head()

        #zagęszczenie

        new, axxx = plt.subplots()
        sns.kdeplot(calosc['x'],calosc['y'],n_levels=2, shade="True",ax=axxx).set_title('Mapa prawdopodobieństwa - zagęszczenie')

        sns.kdeplot(df['x'],df['y'], n_levels=2, ax=axxx)

        plt.show()
    else:
        print("Podaj poprawna opcje!")
    wybor = int(input("Twoj wybor: "))
