/*
 * generator.cpp
 *
 *  Created on: 4 maj 2020
 *      Author: ciesl
 */
#include "generator.h"

void generator_graf::wypisz_dane(int wierzcholki, int il_krawedz, fstream& strumien) ///funkcja wypisujaca wygenerowane grafy do pliku
{
    int liczba_poz_wyk = il_krawedz - wierzcholki + 1;  ///liczba wykonan pozostalych po stworzeniu sciezki
                                                        ///laczacej wszystkie wierzcholki grafu
    int tmp = 0;
    int numer_wierzcholka = wierzcholki;
    int licznik = 0;

    strumien.open("dane.txt", ios_base::app);           ///otwieramy strumien danych zapisu do pliku

    strumien << wierzcholki<<" "<<il_krawedz<<" "<<rand()%wierzcholki<<endl;
                                                        ///wypisujemy ilosc wierzcholkow, krawedzi i wierzcholek startowy
                                                        ///wierzcholek startowy oraz wagi krawedzi sa pseudolosowe
    for(int i = 0; i < wierzcholki - 1 && i < il_krawedz -1 ; i++)
                                                        ///wypisujemy glowny cykl laczacy wszystkie wierzcholki po kolei
    {
        strumien << i<< " "<<i+1<<" "<<rand()%100+1<<endl;
    }

    while(licznik < liczba_poz_wyk) ///wypisujemy pozostale krawdzie w zaleznosci od wypelnienia
    {
        tmp = 0;

        while(licznik < liczba_poz_wyk && tmp < numer_wierzcholka - 2)
        {
            strumien << numer_wierzcholka - 1<<" "<< tmp <<" "<<rand()%10+1<<endl;

            licznik++;
            tmp++;
        }
        numer_wierzcholka--;
    }
    strumien.close();           ///zamykamy strumien do pliku

}



