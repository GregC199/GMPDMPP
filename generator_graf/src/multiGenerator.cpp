//Plik rozszerzajacy program o wczytywanie konfiguracji z pliku (ulatwia losowanie wielu grafow)
//Przykladowe zastosowanie funkcji generujacej zostalo przedstawione w zakomentowanej funkcji main()
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
#include "generator.h"

int maxIloscKrawedzi(int liczba){
	int wynik = (liczba*(liczba-1))/2;
	return wynik;
}

void generujWiele(std::string nazwaPliku){
	std::ifstream plik;
	plik.open(nazwaPliku);

	std::istream_iterator<double> start(plik), end;
	std::vector<double> odczyt(start, end);

	for (int i=0;i<odczyt.size();++i){

		if(i%2==0){
			//odczyt[i] -> liczba wierzcholkow
			//odczyt[i+1] -> liczba krawedzi
	                std::cout<<odczyt[i]<<" "<<odczyt[i+1]<<": ";
			if(odczyt[i] > odczyt[i+1])
				std::cout<<"Krawedzi musi byc wiecej niz wierzcholkow. Operacja nie powiodla sie."<<std::endl;
			else if(odczyt[i+1]>maxIloscKrawedzi(odczyt[i]))
				std::cout<<"Zbyt duza ilosc krawedzi. Operacja nie powiodla sie."<<std::endl;
			else{
				generator_graf* graf = new generator_graf(odczyt[i+1],odczyt[i]);
	       			std::string tmpName="graf_auto"+std::to_string(i/2);
				graf->zapis_do_pliku(tmpName);
                		delete graf;
			}
		}


	}
	std::cout<<std::endl;

}

//int main(){
//	generujWiele("konf.dat");
//}
