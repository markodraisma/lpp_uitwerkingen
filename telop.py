def telop(*getallen):
    """
    functie telop verwacht 0 of meer getallen.
    param: getallen (tuple)
    return: som
    """
    som = 0
    for getal in getallen:
        som += getal
    return som

print (telop())
print(telop( 1,2,3,4 ))
