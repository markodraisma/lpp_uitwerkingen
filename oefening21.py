#!/usr/bin/env python3


files = ['limerick.txt', 'news.1.pdf', 'verhaal' ]

for f in files:
    try:
        pos_laatste_punt = f.rindex('.')
    except:
        print('File "', f, '" heeft geen extensie')
    else:
        # print('File "', f, '" zonder extensie: ', f[:pos_laatste_punt])
        print('File %s zonder extensie: ' % f[:pos_laatste_punt])

