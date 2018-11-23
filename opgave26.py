#!/usr/bin/env python3

namen = ['els', 'els', 'els', 'els', 'henk', 'henk', 'jan', 'jan', 'john',
         'piet', 'piet']

for i in range(1,len(namen)):
    if namen[i] == namen[i-1]:
        print(i, namen[i])
