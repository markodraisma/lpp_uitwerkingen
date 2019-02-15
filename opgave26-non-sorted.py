#!/usr/bin/env python3

# namen = ['els', 'els', 'els', 'els', 'henk', 'henk', 'jan', 'jan', 'john', 'piet', 'piet']

namen = ['jan', 'john', 'john', 'jan', 'els', 'piet', 'henk', 'john', 'jan', 'els', 'piet']
print('Lijst van namen:')
print(namen)

unique_elements = []

for idx,elem in enumerate(namen):
    if elem in unique_elements:
        print('--- Duplicaat element %s op pos %d' % (elem, idx+1))
    else:
        print('    Nieuw element %s op pos %d' % (elem, idx+1))
        unique_elements.append(elem)
