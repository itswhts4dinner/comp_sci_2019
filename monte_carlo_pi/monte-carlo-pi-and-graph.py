import matplotlib.pyplot as plt
import matplotlib.figure
import numpy as np
import random

imax = int(input("How many points would like for the Monte-Carlo integration?"))
##The unit circle
x= np.arange(0.0, np.pi/2, .001)

l = plt.plot(np.cos(x), np.sin(x), 'ro')

plt.setp(l, markersize=.1)
plt.setp(l, markerfacecolor='C0')

i = 0
N = 0
while i <=imax:
    
    x = random.randint(1,1000)/1000
    y = random.randint(1,1000)/1000

    if (x**2 + y**2 <=1):
        N = N+1
        point = plt.plot(x, y, 'go')
        plt.setp(point, markersize=1)
#        plt.setp(point, markerfacecolor='C0')
    else:
        point = plt.plot(x, y, 'ro')
        plt.setp(point, markersize=1)
#        plt.setp(point, markerfacecolor='C5')

    i = i+1
estpi = N/imax*4
plt.text(
        0.5, 1.1,
        ['The value of pi from this integration is ',estpi],
        ha='center')
plt.show()
print(estpi)
