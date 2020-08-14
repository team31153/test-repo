#!/usr/bin/env python3

radius = 5
def areaCircle(r):

    PI = 3.1415
    r = float(input(' Please Enter the radius of a circle: '))
    area = PI * r * r

    print(" Area Of a Circle = %.2f" %area)

areaCircle(radius)
