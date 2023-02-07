# 線を書くプログラム

import turtle
import colorsys

# はいけいのせってい
s = turtle.Screen()
s.bgcolor('black')

# 線の設定
t = turtle.Turtle()

# 線の太さ
t.width(2)

# せんの早さ
#  早い　0 > 10 > 9 > 8 > 7 > 6 > 5 > 4 > 3 > 2 > 1　おそい
t.speed(0)

n = 100
h = 100

# 線の数のせってい
for i in range(100):

    #　色のせってい
    c = colorsys.hsv_to_rgb(h, 1, 0.9)

    # ここを消すと、色が変わらなくなる
    h += 1/n

    t.color(c)
    # 140°左に曲がる
    t.left(140)

    for j in range(3):
        # 広がる設定 ( i+30 とかでも増えるよ！)
        t.forward(i*2)

    # print(i)
