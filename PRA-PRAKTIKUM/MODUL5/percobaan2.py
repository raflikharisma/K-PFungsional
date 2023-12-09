import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,8, 10])
y = np.array([3, 10,5])

plt.figure(figsize=(10,5))
plt.title('Grafik Pendapatan 15 hari', loc='center', pad=20)
plt.plot(x, y, color = 'blue', marker='o')
plt.grid(color= 'darkgray', linestyle=':', linewidth=0.5)
plt.xlabel('Pendapatan')
plt.ylabel('Tanggal')
plt.xlim([0,15])
plt.ylim([0,15])
plt.show()