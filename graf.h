#ifndef GRAF_H
#define GRAF_H

#include <string>

class graf
{
public:
    graf();
    void generujGraf(int liczbaWierzcholkow, int maksymalnaKrawedz);
    void zapiszGrafDoPliku(std::string nazwaPliku);
};

#endif // GRAF_H
