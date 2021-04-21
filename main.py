import numpy as np
ls = [1, 2, 3, 4, 5]
array = np.array(np)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# fig = plt.figure()
# x= np.arange(10)
# y= np.arange(10)
# plt.plot(x,y)

# plt.xlabel("Bored Level")
# plt.title("Boredoom")
# plt.savefig('plot1')

x=np.linspace(0,2* np.pi)
y1 = np.cos(x)
y2 = np.sin(x)
y3 = -1* np.sin(x)
y4 = -1* np.cos(x)

fig_sine = plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)

fig_sine.savefig('sinegraph')