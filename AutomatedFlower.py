from turtle import *
import colorsys

speed(0)
bgcolor("black")
h=2
for i in range(15):
    for j in range(18):
        c=colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h+=0.005
        rt(90)
        circle(120-j*6, 90)
        lt(90)
        circle(120-j*6, 90)
        rt(180)
    circle(40,24)
done()