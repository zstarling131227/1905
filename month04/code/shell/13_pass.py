#!/usr/bin/env python3
import string
import random

key=string.ascii_letters + string.digits+'_'

passs = ''
for i in range(8):
    one = random.choice(key)
    passs += one

print(passs)
