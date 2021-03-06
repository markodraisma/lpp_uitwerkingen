#!/usr/bin/env python3

filename = 'verhaal.txt'

try:
    fh = open(filename,'r')
except Exception:
    import sys
    print('File %s not found!' % filename)
    sys.exit()

nr_of_lines = 0
nr_of_words = 0
nr_of_chars = 0

print()

for line in fh:
    print(line.rstrip())
    nr_of_lines += 1
    words = line.split()
    nr_of_words += len(words)
    nr_of_chars += len(line)

print('\nFile %s has %d lines, %d words, %d characters' % \
        (filename, nr_of_lines, nr_of_words, nr_of_chars))    
fh.close()







