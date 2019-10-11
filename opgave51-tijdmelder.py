import time
import sys

if len(sys.argv) == 2:
    try:
        interval = float(sys.argv[1])
    except Exception as e:
        raise Exception('waarde is niet numeriek')
else:
    raise Exception('Geef een interval in seconden mee')

#need_to_wait = 60 - time.localtime().tm_sec
#print ('Sleeping for %ss, until it is a whole minute' % need_to_wait)
#time.sleep(need_to_wait)

while True:
    try:
        print(time.strftime('%Y/%m/%d  %H:%M:%S  Bingggg', time.localtime()))
        time.sleep(interval)
    except KeyboardInterrupt:
        break



