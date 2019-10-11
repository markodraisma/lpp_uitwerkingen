#! /usr/bin/env python3

import glob

files = glob.glob('*.txt')
for filenaam in files:
  try: 
    f = open(filenaam, encoding="utf-8")
  except Exception:
    import sys
    sys.exit('Bestand kan niet worden geopend: %s' % filenaam)
  rcount = 0
  wcount = 0
  ccount = 0

  for regel in f:
    rcount += 1
    wcount += len(regel.split())
    ccount += len(regel)

  print("%15s: %5d %7d %7d" % (filenaam, rcount, wcount, ccount))

  f.close()
