with open("verhaal.txt") as f:
    lines = f.readlines()
    #lines.reverse()
    for line in reversed(lines):
        print(line, end="")
