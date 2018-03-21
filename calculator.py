#!/usr/bin/env python3

import sys
try:
    GongZiJinE = int(float(sys.argv[1]))
except:
    print("Parameter Error")

YiNaShuiE = GongZiJinE - 3500
if YiNaShuiE <= 1500:
    tax = YiNaShuiE * 0.03
elif YiNaShuiE > 1500 and YiNaShuiE <= 4500:
    tax = YiNaShuiE * 0.10 - 105
elif YiNaShuiE > 4500 and YiNaShuiE <= 9000:
    tax = YiNaShuiE * 0.20 - 555
elif YiNaShuiE > 9000 and YiNaShuiE <= 35000:
    tax = YiNaShuiE * 0.25 - 1005
elif YiNaShuiE > 35000 and YiNaShuiE <= 55000:
    tax = YiNaShuiE * 0.30 - 2755
elif YiNaShuiE > 55000 and YiNaShuiE <= 80000:
    tax = YiNaShuiE * 0.35 - 5505
elif YiNaShuiE > 80000:
    tax = YiNaShuiE * 0.45 - 13505
print("{:.2f}".format(tax)) 
