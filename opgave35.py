#!/usr/bin/env python3

filename = 'verhaal.txt'

try:
    fh = open(filename,'rt', encoding="utf-8")
except Exception:
    import system
    print('File %s not found!' % filename)
    system.exit()

nr_of_lines = 0
nr_of_words = 0
nr_of_chars = 0
nr_of_bytes = 0

print()

for line in fh:
    print(line.rstrip())
    nr_of_lines += 1
    words = line.split()
    nr_of_words += len(words)
    nr_of_chars += len(line)
    nr_of_bytes += len(line.encode("utf-8"))
##    nr_of_bytes += len(bytes(str.encode(line)))

print('\nFile %s has %d lines, %d words, %d characters, %d bytes' % \
        (filename, nr_of_lines, nr_of_words, nr_of_chars, nr_of_bytes))    
fh.close()
