import matplotlib.pyplot as plt
import numpy as np

depths = [2, 3, 4, 5, 6, 7]
times = [0.0032, 0.0222, 0.1741, 1.4027, 11.2457, 93.4237]

plt.plot(depths, times)

plt.xlabel("sügavusaste")
plt.ylabel("aeg (s)")

plt.title("Aja sõltuvus programmi sügavusastmest")

plt.grid(color = "gray", linestyle = "--", linewidth = 0.5)

plt.yticks([0, 20, 40, 60, 80, 100])

plt.show()