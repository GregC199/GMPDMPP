import math
import pandas as pd
#matplotlib inline
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import colorbar

wierzcholekAList=[]
wierzcholekBList=[]
wspolrzednaXList=[40, 9, 81, 83, 100, 22, 32, 16, 43, 65]
wspolrzednaYList=[99, 70, 59, 87, 100, 54, 78, 24, 32, 44]
wierzcholkiPrzeszkodaList=[4,6,9]
przeszkodaTypList=['o','o','o']
promienList=[10,8,17]

arrPunktowX=[]
arrPunktowY=[]

rozdzielczosc=5

def rysujOkrag(promien):
    kat=0
    krok=90
    odleglosc=999
    while odleglosc>rozdzielczosc:
        while kat<360:
            arrPunktowX.append(promien*math.cos(kat)+wspolrzednaXList[i])
            arrPunktowY.append(promien*math.sin(kat)+wspolrzednaYList[i])
            kat=kat+krok
        krok=krok/2
        kat=krok
        odleglosc=krok/360*2*math.pi*promien
    
for x in range(0, len(wierzcholkiPrzeszkodaList)):
    typ=przeszkodaTypList[x]
    i=wierzcholkiPrzeszkodaList[x]
    okragTyp='o'
    prostokatTyp='k'
    if typ=='o':#przeszkoda jest okregiem 
        promien=promienList[x]
        print("wierzcholek", x, ", X:",wspolrzednaXList[i],", Y:",wspolrzednaYList[i])
        arrPunktowX.append(wspolrzednaXList[i])#srodek X
        arrPunktowY.append(wspolrzednaYList[i])#srodek Y
        #W tej funkcji dodawane sa punkty na okregu
        rysujOkrag(promien)
        odlegloscWSrodku=promien
        #W tym while dodawane sa punkty wewnatrz okregu (czyli punkty na okregu o mniejszym promieniu)
        iteracjaSrodka=1
        while odlegloscWSrodku>rozdzielczosc:
                promienSrodek=promien/(2*iteracjaSrodka)
                licznikPromienia=1
                for x in range (0,pow(2,(iteracjaSrodka-1))):
                    kat=0
                    krok=90
                    rysujOkrag(licznikPromienia*(promienSrodek))
                    licznikPromienia=licznikPromienia+2
                odlegloscWSrodku=odlegloscWSrodku/2
                iteracjaSrodka=iteracjaSrodka+1
        #jesli wieksza niz rozdzielczosc to dodaj pomiedzy srodkiem a punktami na luku
        #po wyjsciu z while (dobra rozdzielczosc w srodku) przeszkoda jest gotowa
    else:#przeszkoda jest kwadratem
        print("o")

df = pd.DataFrame()

df['x'] = arrPunktowX
df['y'] = arrPunktowY

df.head()

fig, ax = plt.subplots()

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
