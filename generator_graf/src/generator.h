/*
 * generator.h
 *
 *  Created on: 4 maj 2020
 *      Author: ciesl
 */

#ifndef GENERATOR_H_
#define GENERATOR_H_

#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <fstream>
using namespace std;

class generator_graf{
public:
	int ile_kraw;
	int ile_wierzch;

	generator_graf(int il_k, int il_w){
		ile_kraw = il_k;
		ile_wierzch = il_w;

	}

	void wypisz_dane(int wierzcholki, int il_krawedz, fstream& strumien); ///funkcja wypisujaca wygenerowane grafy do pliku

};



#endif /* GENERATOR_H_ */
