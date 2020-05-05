/*
 * generator.h
 *
 *  Created on: 4 maj 2020
 *      Author: ciesl
 */

#ifndef GENERATOR_H_
#define GENERATOR_H_

#include "libs.h"
#include <cmath>

class generator_graf{
public:
	int ile_kraw;
	int ile_wierzch;
	int val_wypelnienie;

	generator_graf(int il_k, int il_w){
		ile_kraw = il_k;
		ile_wierzch = il_w;

	};

	void generator_z_zapisem(int wierzcholki, int il_krawedz, fstream& strumien); ///funkcja generujaca oraz wypisujaca graf do pliku

	~generator_graf(){
		cout << "Zwalniam pamiec!";
	};

};



#endif /* GENERATOR_H_ */
