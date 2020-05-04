#include "prostokat.h"

prostokat::prostokat(int bokA, int bokB, int orientacja, int wspolrzednaXarg, int wspolrzednaYarg) :
    bokA(bokA), bokB(bokB), orientacja(orientacja)
{
    wspolrzednaX=wspolrzednaXarg;
    wspolrzednaY=wspolrzednaYarg;
    czyKolo=false;
}
