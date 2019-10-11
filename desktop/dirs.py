#! /usr/bin/env python3

import os
from os.path import join, getsize

for dezedir, subdirs, nondirs in os.walk('/usr'):
  som=0
  for naam in nondirs:
    padnaam = join(dezedir, naam)
    try:
      som+=getsize(padnaam)
    except OSError:
      pass

  if som > 0:
    print('Files in %s gebruiken %d bytes ' % (dezedir, som))

