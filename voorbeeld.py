def telop(a, b):
    if type(a or b) not in (int, float):

        raise Exception("type moet int of float zijn, was a=%s ,b=%s" % (type(a), type(b)))
    return a + b
try:
   x = telop(3,4)
   y = telop("4", "5")
except Exception as e:
   print("Er ging iets mis")
   raise
else:
   print(x, y)
