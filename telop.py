def telop(a=0, b=0, *rest):
    som = a + b
    for getal in rest:
        som += getal
    return som

if __name__ == '__main__':
    print("Test", telop(3,4))
    print("Test", telop(5))
    print("Test", telop(3,4,5,6))
