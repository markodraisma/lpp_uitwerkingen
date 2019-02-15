def vermenigvuldig(a, b):
    return a * b

def telop(a, b):
    return a + b


def voeruit(f, start, einde):
    resultaat = start
    for i in range(start+1,einde + 1):
        resultaat = f(resultaat, i)
    return resultaat

def teller():
    n = 0
    def inner():
        nonlocal n
        n+=1
        return n
    return inner


print(voeruit(telop,1,5))
print(voeruit(vermenigvuldig,1,5))

x = teller()
print(x())
print(x())
print(x())
