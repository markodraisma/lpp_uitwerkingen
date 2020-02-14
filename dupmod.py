#!/usr/bin/env python3

def dubbelen(lijst):
    """
    Maak list met indexnummers van de dubbele namen in lijst.
    De lijst moet gesorteerd zijn.
    Return-waarde is de list met index-nummers.
    """
    retlist = []

    for i in range(1, len(lijst)):
        if lijst[i] == lijst[i-1]:
            retlist.append(i)

    return retlist

if __name__ == '__main__':

    namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']

    namen.sort()

    print("De invoerlijst wordt:", namen)

    dublist = dubbelen(namen)

    print("De indexen van de duplicaten zijn:", dublist)
