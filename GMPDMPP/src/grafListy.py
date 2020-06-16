import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

class graf:
	liczbaWierzcholkow=0
	liczbaPolaczen=0
	wierzcholekPoczatkowy=0
	nazwaPliku=''
	wierzcholekAList=[]
	wierzcholekBList=[]
	wspolrzednaXList=[]
	wspolrzednaYList=[]
	wierzcholkiPrzeszkodaList=[]
	przeszkodaTypList=[]
	parametrPrzeszkodyA=[]#promien w przypadku koła, bok A w przypadku prostokąta
	parametrPrzeszkodyB=[]#bok B w przypadku prostokąta

	#funkcja inicjujaca grafTest, w argumencie przyjmuje nazwe pliku wygenerowanego przez modul napisany w jezyku C++	
	def inicjuj(self,nazwa):
		#Otwieranie pliku i kopiowanie zawartosci do zmiennej str
		self.nazwaPliku=nazwa
		f=open(self.nazwaPliku, 'r+')
		str=f.read()
		f.close()
		#Podział zmiennej str (separatorem sa znaki biale)
		podz=str.split()
		
		self.liczbaWierzcholkow=int(podz[0])
		self.liczbaKrawedzi=int(podz[1])
		self.wierzcholekPoczatkowy=int(podz[2])

		for i in range(3,self.liczbaKrawedzi*6+3):
			if(i%6==3):
				self.wierzcholekAList.append(int(podz[i]))
			elif(i%6==4):
				self.wierzcholekBList.append(int(podz[i]))
			elif(i%6==5):
				self.wspolrzednaXList.append(int(podz[i]))
			elif(i%6==0):
				self.wspolrzednaYList.append(int(podz[i]))
			elif(i%6==1):
				self.parametrPrzeszkodyA.append(int(podz[i]))
			elif(i%6==2):
				self.parametrPrzeszkodyB.append(int(podz[i])) 
		for i in range(self.liczbaKrawedzi*6+3,len(podz)):
			if(i%2==1):
				self.wierzcholkiPrzeszkodaList.append(int(podz[i]))
			elif(i%2==0):
				self.przeszkodaTypList.append(podz[i])
		
	#Funkcja sluzaca do diagnostyki
	def wyswietl(self):
		f=open(self.nazwaPliku, 'r+')
		str=f.read()
		f.close()
		podz=str.split()
		print(podz)
		print("::WierzcholekA:   ",self.wierzcholekAList)
		print("::WierzcholekB:   ",self.wierzcholekBList)
		print("::WspolrzednaX:   ",self.wspolrzednaXList)
		print("::WspolrzednaY:   ",self.wspolrzednaYList)
		print("::Przeszkody:     ",self.wierzcholkiPrzeszkodaList)
		print("::Typ przeszkody: ",self.przeszkodaTypList)
		print("::Parametr A :    ",self.parametrPrzeszkodyA)
		print("::Parametr B :    ",self.parametrPrzeszkodyB)

#Tworzenie pustego obiektu klasy grafTest
#obiekt=graf()
#Inicjowanie obiektu klasy grafTest na podstawie pliku tekstowego wygenerowanego przez generator grafow napisany w jezyku C++
#obiekt.inicjuj('test.dat')
#wyswietlanie na potrzeby diagnostyki
#obiekt.wyswietl()
