#!/usr/bin/env python3

uurwaarden = '673,1499,82,119341,13,996308,53,7,4711,2,189320'
lijst = uurwaarden.split(',')
tot = 0

for nr, uur in enumerate(lijst):
    print('Uur %2s: %7s' % (nr+1, uur))
    tot += int(uur)

print('Totaal: %d' % tot)
