#!/usr/bin/env python3

wisselgeld = 1788


rest = 0

aantal_500 = wisselgeld // 500
terug = aantal_500 * 500 
rest = wisselgeld - terug

aantal_200 = rest // 200
terug = terug + aantal_200 * 200
rest = wisselgeld - terug

aantal_100 = rest // 100
terug = terug + aantal_100 * 100
rest = wisselgeld - terug

aantal_50 = rest // 50
terug = terug + aantal_50 * 50
rest = wisselgeld - terug

aantal_20 = rest // 20
terug = terug + aantal_20 * 20
rest = wisselgeld - terug

aantal_10 = rest // 10
terug = terug + aantal_10 * 10
rest = wisselgeld - terug

aantal_5 = rest // 5
terug = terug + aantal_5 * 5
rest = wisselgeld - terug



print('Aantal bijletten van 500:', aantal_500)
print('Aantal bijletten van 200:', aantal_200)
print('Aantal bijletten van 100:', aantal_100 )
print('Aantal bijletten van 50:', aantal_50 )
print('Aantal bijletten van 20:', aantal_20 )
print('Aantal bijletten van 10:', aantal_10 )
print('Aantal bijletten van 5:', aantal_5 )
print('Teruggavebedrag:', terug) 

