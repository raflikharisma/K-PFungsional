import matplotlib.pyplot as plt
from functools import reduce
import numpy as np




nilai_mahasiswa = [75,80, 90, 65, 70,85,95,78,88,92]
mahasiswa = list(map(lambda i: f"MHS{i+1}", range(len(nilai_mahasiswa))))

average = reduce(lambda x, y: x + y, nilai_mahasiswa)/len(nilai_mahasiswa)
data = np.array(nilai_mahasiswa)
plt.title("Diagram Batang Nilai Ujian Mahasiswa")
plt.axhline(y=average, color="red", linestyle='dashed', linewidth=1.5, label = "Average")
plt.xlabel("Mahasiswa")
plt.ylabel("Nilai Mahasiswa")
plt.plot(average)
plt.bar(mahasiswa, data)
plt.legend()
plt.show()


