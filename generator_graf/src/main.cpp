
#include "libs.h"
#include "generator.h"
int max_ilosc_wierzcholkow (int liczba){
	int wynik = (liczba*(liczba - 1))/2;

	return wynik;
}
void menu(){
	string nazwa_pliku;

	bool warunek,warunek_wierzcholki,warunek_krawedzi,warunek_kontynuacja;


	int ilosc_wierzch, ilosc_krawedzi, test;

	test = 0;
	ilosc_wierzch = ilosc_krawedzi = -1;

	warunek_kontynuacja = false;
	warunek_wierzcholki = false;
	warunek_krawedzi = false;

	warunek = true;


	while(warunek == true){

		test = 0;
		ilosc_wierzch = ilosc_krawedzi = -1;

		warunek_kontynuacja = false;
		warunek_wierzcholki = false;
		warunek_krawedzi = false;

		warunek = true;

		while(warunek_wierzcholki == false){

			cout << "Podaj dodatnia liczbe wierzcholkow!\n";
			cin >> ilosc_wierzch;
			if( !cin )
			{ // wpisano coœ, co nie jest liczb¹
			    cin.clear();
			    cin.sync();

			    cout <<"Nie wpisano liczby!\n";
			    warunek_wierzcholki = false;
			}
			else
			{ // wpisano liczbê
				warunek_wierzcholki = true;
			}
			if(ilosc_wierzch < 0)warunek_wierzcholki = false;

		}

		while( warunek_krawedzi == false){

			cout << "Podaj liczbe krawedzi co najmniej rowna lub wieksza od liczby wierzcholkow!\n";
			cin >> ilosc_krawedzi;
			if( !cin )
			{ // wpisano coœ, co nie jest liczb¹
			    cin.clear();
			    cin.sync();

			    cout <<"Nie wpisano liczby!\n";
			    warunek_krawedzi = false;
			}
			else
			{ // wpisano liczbê
				warunek_krawedzi = true;
			}
			if(ilosc_krawedzi > max_ilosc_wierzcholkow(ilosc_wierzch))warunek_krawedzi = false;
			if(ilosc_krawedzi < ilosc_wierzch)warunek_krawedzi = false;
		}

		cout << "Podaj nazwe pliku wraz z rozszerzeniem, do ktorego chcesz zapisac graf!\n";
		cin >> nazwa_pliku;
		if( !cin )
		{ // wpisano coœ, co nie jest stringiem
		    cin.clear();
		    cin.sync();

		    cout <<"Nie wpisano nazwy pliku!\n";
		}

		generator_graf* graf = new generator_graf(ilosc_krawedzi,ilosc_wierzch);

		graf->zapis_do_pliku(nazwa_pliku);

		delete graf;

		while(warunek_kontynuacja == false){
			cout << "Wygenerowac kolejny graf? (0 - nie, 1 - tak)\n";

			cin >> test;
			if( !cin )
			{ // wpisano coœ, co nie jest liczb¹
				cin.clear();
				cin.sync();

				cout <<"Nie wpisano liczby!\n";
			}

			if(test == 0 || test == 1)warunek_kontynuacja = true;
		}

		if(test == 0)warunek = false;

	}
}

int main(){

	menu();
	return 0;
}
