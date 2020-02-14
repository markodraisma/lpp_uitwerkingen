#!/usr/bin/env python3

try:
    f = open("anim_layout_changes.mp4", "rb")
except Exception:
    import sys
    sys.exit("Fout bij openen bestand")

while True:
    buf = f.read(1024)   # lees een groep bytes
    if not buf:          # einde bestand bereikt?
        break
    for c in buf:        # behandel elk byte
        if c >= 32 and c < 127:   # is byte printbaar?
            print( chr(c) )       # dan print teken

f.close()
