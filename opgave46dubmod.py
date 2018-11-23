#!/usr/bin/env python3 
'''Deze module bevat de dubbelen() functie tbv. opgave46
'''
 
def dubbelen(l_namen):
    '''Geef de index van dubbele elementen uit de lijst l_namen
    '''
    l_namen = l_namen[:]
    vorige = ''
    l_dubbelen = []
    for idx,elem in enumerate(l_namen):
        if elem == vorige:
            # print(idx)
            l_dubbelen.append(idx)
        else:
            vorige = elem
    return l_dubbelen

if __name__ == '__main__':
    namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
          'els', 'john', 'els', 'jan', 'els', 'henk']
    namen.sort()
    print('---', dubbelen(namen))
    # print('gebruik: python3 opgave46duplicaten.py')
    print('Ik wordt nu direct aangeroepen! __name__ = ', __name__)
else:
    print('Ik ben nu geïmporteerd! __name__ = ', __name__)
