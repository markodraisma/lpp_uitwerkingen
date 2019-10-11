#!/usr/bin/env python3

# class SortedDict........


if __name__=='__main__':

    n = SortedDict({'allo': 3, 'hallo': 2, 'nee': 9, 'hoi': 5})

    print(n)

    l = SortedDict()
    l["hoi"]=5
    l["hallo"]=2
    l["allo"]=3
    l["nee"]=9

    for k in l.keys():
        print(k, l[k])

    print(l)


