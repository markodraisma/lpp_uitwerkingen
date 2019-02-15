for getal in range (2, 1001):
    priem=True
    for deler in range(2, getal):
        if deler<getal and getal%deler == 0:
            priem=False
            continue
    if priem: print(getal)
