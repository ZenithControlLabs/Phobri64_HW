#!/usr/bin/python3

import math

OFS = 3.0

circs1 = [(1.4,55),(2.4,25)]

circs2 = [(0.9,70),(1.9,40)]

for circ in circs1:
    real_shit = (0.3629) / (2 * math.pi * circ[0]) * 360 * 3
    print(real_shit)
    ang = (math.pi)/180 * (180 + 45 - real_shit/2)
    print("Start (x,y) =({:5f},{:5f}) Angle = {:5f}".format(circ[0] * math.cos(ang),\
        OFS - circ[0] * math.sin(ang),
        360 - real_shit))
for circ in circs2:
    real_shit = (0.3629) / (2 * math.pi * circ[0]) * 360 * 3
    ang = (math.pi)/180 * (45 - real_shit/2)
    print("Start (x,y) =({:5f},{:5f}) Angle = {:5f}".format(circ[0] * math.cos(ang),\
        -OFS - circ[0] * math.sin(ang),
        360 - real_shit))

