#!/usr/bin/env python

def telklinkers(s):
    """
    Deze functie telt het aantal klinkers in een string

    :param s: str, Input string
    :return: int, Aantal klinkers in s
    """
    #
    if not type(s) == str:
        raise Exception("Geen string opgegeven.")
    nr_of_klinkers = 0
    for letter in s:
       if letter.lower() in 'aeiouy':
            nr_of_klinkers += 1 
    return nr_of_klinkers

#in_str = input('Van welke tekst zal ik de klinkers tellen?\n\n> ') 
#print(telklinkers(in_str))
print(telklinkers(12345))
