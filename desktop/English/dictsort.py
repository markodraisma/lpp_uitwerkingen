#!/usr/bin/env python3

# class SortedDict........


if __name__=='__main__':

    n = SortedDict({'ello': 3, 'hello': 2, 'not': 9, 'hey': 5})

    print(n)

    l = SortedDict()
    l["hey"]=5
    l["hello"]=2
    l["ello"]=3
    l["not"]=9

    for k in l.keys():
        print(k, l[k])

    print(l)
