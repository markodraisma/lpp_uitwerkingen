lijst = "limerick.txt news.1.pdf verhaal"
lijst = lijst.split()


for naam in lijst:
    i = naam.rfind(".")
    if i >= 0:
        print(naam[0:i])
    else:
        print(naam)
