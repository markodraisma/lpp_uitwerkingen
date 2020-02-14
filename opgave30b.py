#!/usr/bin/env python3

f = open("anim_layout_changes.mp4", "rb")
tekens = "" # ruimte om tekens op te sparen

while True:
    buf = f.read(1024) # lees zwikkie bytes
    if not buf: # einde bestand bereikt?
        break
    for c in buf: # behandel elk byte
        if c >= 32 and c < 127: # is byte printable?
            tekens += chr(c) # dan toevoegen aan verzamelde tekens
        else: #zo niet?
            if len(tekens) >= 4: # als verzamelde tekens voldoende,
                print(tekens) # dan print verzamelde tekens
                tekens = "" # poets verzamelde tekens leeg
    if len(tekens) >= 4: # stond er nog een restje tekens?
        print(tekens) # dan print het restje

f.close()
