def main():
    mijntekst = input("geef een tekst op: ")
    k, m  = telklinkers(mijntekst)
    print("aantal klinkers:", k, "aantal medeklinkers:", m)

def telklinkers(tekst):
    klinkers = 'aeiouy'
    klinkers += klinkers.upper()
    rest = 'abcdefghijklmnopqrstuvwxyz'
    rest += rest.upper()
    aantalklinkers = 0
    aantalmedeklinkers = 0
    for letter in tekst:
        if letter in klinkers:
            aantalklinkers += 1
        elif letter in rest:
            aantalmedeklinkers += 1
    return aantalklinkers, aantalmedeklinkers

main()

