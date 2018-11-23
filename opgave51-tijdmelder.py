#!/usr/bin/env python3
import time
import sys

# vang de 1e cmdline argument op, dit interpreteren we als de interval (n)
if len(sys.argv) == 2:
    n = float(sys.argv[1])
# we accepteren alleen 1 parameter, anders fout!
else:
    print('ERROR: I need exacltly one argument: interval')
    print('Usage:')
    print('     %s interval' % sys.argv[0])
    sys.exit(1)

# wacht tot de volgende min. grens
pauseren = 60 - time.localtime().tm_sec
print('Wachten tot de min. grens, %s sec' % pauseren)
time.sleep(pauseren)

# schrijf uit de tijd om de zoveel sec. (aangeegeven door n)
# 2018/01/30 11:45:16 Biinggg
# print(     )
while True:
    tijdstr = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
    tijdstr = tijdstr + ' Biinngggggg'
    print(tijdstr)
    time.sleep(n)