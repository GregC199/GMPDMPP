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
    int memory[ilosc_przeszkod];

    bool war = false;
    bool war2 = false;

    for(int i = 0; i<ilosc_przeszkod;++i)//inicjalizacj warto�ci dla tablicy memory
    {
    	memory[i] = -1;
    }

    strumien << wierzcholki<<" "<<il_krawedz<<" "<<rand()%wierzcholki<<endl;
                                                        ///wypisujemy ilosc wierzcholkow, krawedzi i wierzcholek startowy
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

    strumien << tmp << " "<<przeszkoda[rand()%2]<<endl;

    if(ilosc_przeszkod > 1){

    	memory[0] = tmp;
    	tmp = 0;

        for(int i = 1; i < ilosc_przeszkod; ++i){
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



