#ifndef PROSTOKAT_H
#define PROSTOKAT_H

#include "wierzcholek.h"

class prostokat : wierzcholek
{
public:
    prostokat(){
        czyKolo=false;
    };
    prostokat(int bokA, int bokB, int orientacja, int wspolrzednaXarg, int wspolrzednaYarg);
    void losujParametry();
    int bokA;
    int bokB;
    int orientacja;//wzgledem ukladu globalnego
};

#endif // PROSTOKAT_H
