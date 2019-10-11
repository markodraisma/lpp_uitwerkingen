with open("woorden.txt") as f:
    alllines = f.readlines()
    alllines = [ s[::-1] for s in alllines ] 
    for line in sorted(alllines):
        print(line[::-1],end="")
    print()
