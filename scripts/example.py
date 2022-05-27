from pythonic_plots import plt
import numpy as np
x = np.linspace(0, 10, 100)
panel = [plt.plot(x, x**2),
         plt.plot(x, x**3),
         plt.plot(x, x+2)]
plt.save(panel, "scripts/panel1.png")
plt.show(panel)


panel = [[plt.plot(x, x**2), plt.hist(x**2)],
         [plt.plot(x, x**3), plt.hist(x**3)],
         [plt.plot(x, x+2),  plt.hist(x+2)]]
plt.save(panel, "scripts/panel2.png")
plt.show(panel)

panel = [plt.plot(x, x**2, label="square") + plt.plot(x, x, label="linear") + plt.legend(),
         plt.plot(x, x**3) + plt.set_title("Cubic function"),
         plt.plot(x, x+2) + plt.set_xlabel("Price")]
plt.save(panel, "scripts/panel3.png")
plt.show(panel)

panel = [[plt.plot(a*x+b)+plt.set_title(f"{a}x+{b}") for b in (0, 2, 5)]
         for a in (0.5, 2, 3)]
plt.show(panel, sharex="all", sharey="all")
plt.save(panel, "scripts/panel4.png")
