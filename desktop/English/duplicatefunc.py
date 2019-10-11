#!/usr/bin/env python3

def duplicates(lst):
    """
    Create a list of index numbers from the duplicate values
    in the list that is given as a parameter.
    Assume that the given list is sorted.
    Return the list with index numbers.
    """
    # Add your own code here:
    pass

names = [ 'eve', 'john', 'pete', 'eve',  'hank', 'eve',
          'joe', 'eve',  'joe',  'pete', 'hank' ]

names.sort()

print("The input list becomes:", names)

dublist = duplicates(names)

print("The indexes of the duplicates are:", dublist)
