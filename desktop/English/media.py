#!/usr/bin/env python3

class Medium(object):
    """ a library-medium class
    meant as superclass for real media
    """
    pass

class Book(Medium):
    """ a library-book class
    """
    pass

#             title             price   author                   #pages
leapr = Book("Learning Python", 35.50, "Mark Lutz & David Ascher", 595)

#             title                    price  author     #pag  illustrator
#astrx = Comic("Asterix and Cleopatra", 3.95, "Goscinny", 32, "Uderzo")

#             title                   price   director         minage
#spody = Dvd("2001, a space odyssey", 17.50, "Stanley Kubrick", 12)

leapr.show()

#astrx.show()
#spody.show()
