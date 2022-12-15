import numpy as np
import matplotlib.pyplot as plt
with open ("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
data_array = np.loadtxt("data.txt", dtype=int)
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

t = [i/100 for i in range(len(data_array))]
voltage = [i*3.3/256 for i in data_array]

voltage1 = np.array(voltage)
i_max = voltage1.argmax()

print(i_max/100)
print(len(t)/100-i_max/100)

ax.plot(t, voltage, "-", linewidth=2, markersize=4, label="V(t)")

plt.text(255, 2.2, "Время заряда {time:.2f} с".format(time=i_max/100), fontsize=10)

plt.yticks(np.arange(0, 3.5, step=0.5))
plt.ylabel("Напряжение, В")
plt.xticks(np.arange(0, 11, step=2))
plt.xlabel("Время, С")
plt.title("Процесс заряда и разряда конденсатора в RC-цепочке")

plt.minorticks_on()
plt.grid(True, "both", "both")

ax.legend()

plt.savefig("graph.svg")
plt.show()

