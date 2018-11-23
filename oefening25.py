#!/usr/bin/env python3

uurwaarden = '673,1499,82,119341,13,996308,53,7,4711,2,189320'
l = uurwaarden.split(',')
tot = 0

for nr, uurw in enumerate(l):
    print('Uur {:>2}: {:>7}'.format(nr+1, uurw))
    tot += int(uurw)

formatstr = 'Totaal: {{:{}}}'.format( len( str(tot) ) )
#            Totaal: {:7}
print('DEBUG: formatstr: ', formatstr)
print(formatstr.format(tot))
