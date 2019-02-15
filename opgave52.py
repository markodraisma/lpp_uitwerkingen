#!/usr/bin/env python3

def counter(filename):

    try:
        fh = open(filename,'rt', encoding="UTF-8")
    except Exception:
        import sys
        print('File %s not found!' % filename)
        raise 

    nr_of_lines = 0
    nr_of_words = 0
    nr_of_chars = 0
    nr_of_bytes = 0


    for line in fh:
        nr_of_lines += 1
        words = line.split()
        nr_of_words += len(words)
        nr_of_chars += len(line)
        nr_of_bytes += len(line.encode())

    print('%20s: %4d lines, %4d words, %5d characters, %5d bytes' % \
            (filename, nr_of_lines, nr_of_words, nr_of_chars, nr_of_bytes))    
    fh.close()

import glob

filenamen = glob.glob("*.txt")
for file in filenamen:
    counter(file)
