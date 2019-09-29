import matplotlib.pyplot as plt
import numpy as np

jahre = np.array([0, 1, 2, 3, 4, 5, 6])
gewinn = 12.719866
initial = 54.444000

gewinne = (jahre * gewinn) - initial
kosten = np.repeat(0, len(jahre))

plt.style.use('dark_background')

plt.plot(jahre, gewinne, label="Bilanz")
plt.plot(jahre, kosten, label="Gewinnzone", linestyle="--")
plt.plot(initial / gewinn, 0, label="Break Event Point",
         linestyle="None", marker='o', color='b')
plt.ylabel('Millionen €')
plt.xlabel('Jahre')
plt.legend()

# plt.show()
plt.savefig("break-even-point.svg", transparent=True, format="svg")
