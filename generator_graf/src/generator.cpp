/*
 * generator.cpp
 *
 *  Created on: 4 maj 2020
 *      Author: ciesl
 */
#include "generator.h"

void generator_graf::generator_z_zapisem(int wierzcholki, int il_krawedz, fstream& strumien) ///funkcja wypisujaca wygenerowane grafy do pliku
{
    int liczba_poz_wyk = il_krawedz - wierzcholki + 1;  ///liczba wykonan pozostalych po stworzeniu sciezki
                                                        ///laczacej wszystkie wierzcholki grafu
    int tmp;
    int numer_wierzcholka = wierzcholki;
    int licznik = 0;

    char przeszkoda[2];
    przeszkoda[0] = 'k';
    przeszkoda[1] = 'o';

    int ilosc_przeszkod = (int)ceil((double)wierzcholki/20.0);
    int memory[ilosc_przeszkod+1];

    bool war = false;
    bool war2 = false;

    for(int i = 0; i<ilosc_przeszkod+1;++i)//inicjalizacj wartoœci dla tablicy memory
    {
    	memory[i] = -1;
    }

    tmp=rand()%wierzcholki;
    memory[0] = tmp;

    strumien << wierzcholki<<" "<<il_krawedz<<" "<<tmp<<endl;

    tmp = 0;													///wypisujemy ilosc wierzcholkow, krawedzi i wierzcholek startowy
                                                        ///wierzcholek startowy oraz wagi krawedzi sa pseudolosowe
    for(int i = 0; i < wierzcholki - 1 && i < il_krawedz -1 ; ++i)
                                                        ///wypisujemy glowny cykl laczacy wszystkie wierzcholki po kolei
    {
        strumien << i<< " "<<i+1<<" "<<rand()%96+5<<" "<<rand()%96+5<<endl;
    }

    while(licznik < liczba_poz_wyk) ///wypisujemy pozostale krawdzie w zaleznosci od wypelnienia
    {
        tmp = 0;

        while(licznik < liczba_poz_wyk && tmp < numer_wierzcholka - 2)
        {
            strumien << numer_wierzcholka - 1<<" "<< tmp <<" "<<rand()%96+5<<" "<<rand()%96+5<<endl;

            ++licznik;
            ++tmp;
        }
        --numer_wierzcholka;
    }

    tmp = rand()%wierzcholki;

    while(tmp == memory[0]){

    	tmp = rand()%wierzcholki;
    }


    strumien << tmp << " "<<przeszkoda[rand()%2]<<endl;

    if(ilosc_przeszkod > 1){

    	memory[1] = tmp;
    	tmp = 0;

        for(int i = 2; i < ilosc_przeszkod+1; ++i){
        	while(war == false){
        		war2 = false;
        		tmp = rand()%wierzcholki;
        		for(int j = 0; j < i; ++j){
        			if(tmp == memory[j])war2 = true;
        		}
        		if(war2 == false)war = true;

        	}

        	memory[i] = tmp;

        	strumien << tmp << " "<<przeszkoda[rand()%2]<<endl;
        }
    }



}

void generator_graf::zapis_do_pliku(string& nazwa){

	fstream str;

    str.open(nazwa, ios_base::app);           ///otwieramy strumien danych zapisu do pliku

    this->generator_z_zapisem(this->ile_wierzch, this->ile_kraw, str); //wywolujemy metode zapisu do zadanego strumienia

    str.close();           ///zamykamy strumien do pliku
}



