try:
    bestand = open("anim_layout_changes.mp4","rb")
except Exception: 
    import system
    system.exit("Fout bij inlezen")
print(bestand.seek(0,2))
bestand.close()
