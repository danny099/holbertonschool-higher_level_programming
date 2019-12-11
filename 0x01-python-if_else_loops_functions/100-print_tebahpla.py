#!/usr/bin/python3
upp = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - upp)), end="")
    upp = 32 if upp == 0 else 0
