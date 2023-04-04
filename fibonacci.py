import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n):
    f = []
    for i in range(1, n + 1):
        if i > 2:
            f.append(f[i-2] + f[i-3])
        else:
            f.append(1)
    return f

def color(i):
    r = 0
    g = 1 
    b = 1 - i/10
    return (r, g, b)

plt.axes()
count = 0
l = [0]
for i in range(1, 10):
    l.append(fibonacci(i)[i-1])
    if count < 3:
        if count == 0:
            if i == 1: 
                posx = 0
                posy = 0
            else:
                posx = posx
                posy = posy - l[i-1]
            ab = plt.Line2D((posx, posx + l[i]), (posy, posy), color = color(i), lw=1.5)
            plt.gca().add_line(ab)
        if count == 1:
            posx = posx + l[i-1]
            posy = posy
            bc = plt.Line2D((posx, posx), (posy, posy + l[i]), color = color(i), lw=1.5)
            plt.gca().add_line(bc)
        if count == 2:
            posx = posx
            posy = posy + l[i-1]
            cd = plt.Line2D((posx, posx - l[i]), (posy, posy), color = color(i), lw=1.5)
            plt.gca().add_line(cd)
        count = count + 1
        continue
    if count == 3:
        posx = posx - l[i-1]
        posy = posy
        da = plt.Line2D((posx, posx), (posy, posy - l[i]), color = color(i), lw=1.5)
        plt.gca().add_line(da)
        count = 0
plt.axis('scaled')
print(l)
plt.show()