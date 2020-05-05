class graf:
	liczbaWierzcholkow=0
	liczbaPolaczen=0
	wierzcholekPoczatkowy=0
	nazwaPliku=''
	wierzcholekAList=[]
	wierzcholekBList=[]
	wspolrzednaXList=[]
	wspolrzednaYList=[]
	typPrzeszkodyList=[]
	
	#funkcja inicjujaca graf, w argumencie przyjmuje nazwe pliku wygenerowanego przez modul napisany w jezyku C++	
	def inicjuj(self,nazwa):
		#Otwieranie pliku i kopiowanie zawartosci do zmiennej str
		self.nazwaPliku=nazwa
		f=open(self.nazwaPliku, 'r+')
		str=f.read()
		f.close()
		#Podział zmiennej str (separatorem sa znaki biale)
		podz=str.split()
		
		self.liczbaWierzcholkow=podz[0]
		self.liczbaKrawedzi=podz[1]
		self.wierzcholekPoczatkowy=podz[2]

		for i in range(3,len(podz)):
			if(i%5==3):
				self.wierzcholekAList.append(int(podz[i]))
			elif(i%5==4):
				self.wierzcholekBList.append(int(podz[i]))
			elif(i%5==0):
				self.wspolrzednaXList.append(int(podz[i]))
			elif(i%5==1):
				self.wspolrzednaYList.append(int(podz[i]))
			else:
				self.typPrzeszkodyList.append(podz[i])
	
	#Funkcja sluzaca do diagnostyki
	def wyswietl(self):
		f=open(self.nazwaPliku, 'r+')
		str=f.read()
		f.close()
		podz=str.split()
		print(podz)
		print(":::",self.wierzcholekAList)
		print(":::",self.wierzcholekBList)
		print(":::",self.wspolrzednaXList)
		print(":::",self.wspolrzednaYList)
		print(":::",self.typPrzeszkodyList)


#Tworzenie pustego obiektu klasy graf
obiekt=graf()
#Inicjowanie obiektu klasy graf na podstawie pliku tekstowego wygenerowanego przez generator grafow napisany w jezyku C++
obiekt.inicjuj('test.dat')
#wyswietlanie na potrzeby diagnostyki
obiekt.wyswietl()
