import sys
from logging2 import Logger

logger = Logger("message")

for item in sys.argv:
    print(item)
print(sys.argv)

try:
    if sys.argv[1] =='1234':
        print("ok")
except:
    print(" not good")

logger.info("gol")
