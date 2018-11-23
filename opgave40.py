#!/usr/bin/env python3

def telklinkers(s):
    """
    Deze functie telt het aantal klinkers in een string

    :param s: str, Input string
    :return: int, Aantal klinkers in s
    """
    #
    nr_of_klinkers = 0
    for letter in s:
       if letter.lower() in 'aeiou':
            nr_of_klinkers += 1 
    return nr_of_klinkers

in_str = input('Geef svp. een string, en ik vertel hoeveel klinkers erin zitten :') 
print(telklinkers(in_str))
