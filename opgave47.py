def myrange(start, end, step=1):
    if start == end:
        raise Exception("Start en eind zijn gelijk")
    for i in range(start,end, step):
        yield i


def test():
    for i in myrange(10,10,10):
        print(i)


try:
   test()
except Exception as e:
    print("Er ging iets fout:", e.args)

