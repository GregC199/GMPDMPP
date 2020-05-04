#ifndef KOLO_H
#define KOLO_H

#include "wierzcholek.h"

class kolo : wierzcholek
{
public:
    kolo(){
        czyKolo=true;
    };
    kolo(int promien, int wspolrzednaXarg, int wspolrzednaYarg);
    int promien;
    void losujParametry();

};

#endif // KOLO_H
