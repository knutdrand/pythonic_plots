from importlib import reload
import pythonic_plots.pythonic_plots as pp
import numpy as np

reload(pp)
ax = pp.Module()

x = np.arange(10)

plt.show2([[plt.plot(x, x**i, label="pow")+plt.plot(x, x+1, label="plus") + plt.legend() for i in range(1, j)]
          for j in range(2, 5)])


plt.show([plt.plot(x, x**i) + plt.set_xlabel("x") for i in range(1, 4)])
plt.show([plt.plot(x, x**i) + plt.set_xlabel("x") for i in range(1, 4)], n_col=2)
plt.show([plt.plot(x, x**i) + plt.set_xlabel("x") for i in range(1, 5)], n_row=3)
plt.show([[plt.plot(x, x**i) for i in range(1, j)]
          for j in range(2, 5)])

plt.show([[plt.plot(x, x**i, label="pow")+plt.plot(x, x+1, label="plus") + plt.legend() for i in range(1, j)]
          for j in range(2, 5)])
