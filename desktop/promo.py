promo = "Sale: sm\u00f8rrebr\U000000f8d voor 2\u20ac\n"

f = open("promo1.txt", "w", encoding="ascii", errors="ignore")
f.write(promo)
f.close()

f2 = open("promo1.txt", encoding="ascii")
print(f2.readline())
f2.close()
