#!/usr/bin/env python3

import sys

#def tax(Ynsd,Sl,Ss):
#    tax = Ynsd * Sl -Ss
#    return tax

Sl_tab = [0.03, 0.10, 0.20, 0.25, 0.30, 0.35, 0.45]
Ss_tab = [0, 105, 555, 1005, 2755, 5505, 13505]

for arg in sys.argv[1:]:
    inp=arg.split(':')
    try:
        Gh = int(float(inp[0]))
        ShuiQian = int(float(inp[1]))
    except:
        print("Parameter Error")
    SheBao = ShuiQian * 0.165
    YingNaSuoDe = ShuiQian - SheBao - 3500
    if YingNaSuoDe < 1500 and YingNaSuoDe >0:
        Shuilv = Sl_tab[0]
        Susuan = Ss_tab[0]
    elif YingNaSuoDe >= 1500 and YingNaSuoDe <4500:
        Shuilv = Sl_tab[1]
        Susuan = Ss_tab[1]
    elif YingNaSuoDe >= 4500 and YingNaSuoDe <9000:
        Shuilv = Sl_tab[2]
        Susuan = Ss_tab[2]
    elif YingNaSuoDe >= 9000 and YingNaSuoDe <35000:
        Shuilv = Sl_tab[3]
        Susuan = Ss_tab[3]
    elif YingNaSuoDe >= 35000 and YingNaSuoDe <55000:
        Shuilv = Sl_tab[4]
        Susuan = Ss_tab[4]
    elif YingNaSuoDe >= 55000 and YingNaSuoDe <80000:
        Shuilv = Sl_tab[5]
        Susuan = Ss_tab[5]
    elif YingNaSuoDe >= 80000:
        Shuilv = Sl_tab[6]
        Susuan = Ss_tab[6]
    else:
        Shuilv = 0
        Susuan = 0
    YingNaTax = YingNaSuoDe * Shuilv - Susuan
    Tax = YingNaSuoDe * Shuilv - Susuan
    ShuiHou = ShuiQian - SheBao - Tax
    print(format(Gh) + ':'+"{:.2f}".format(ShuiHou))
