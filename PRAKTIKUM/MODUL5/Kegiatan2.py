import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("D:\KULIAH\SEMESTER 5\FUNGSIONAL\PRAKTIKUM\Click Here\PRAKTIKUM\MODUL5\data_produk.csv")
 
data["Total Harga"] = data["Harga Produk"]*data["Jumlah Beli"]
print(data.to_string())

plt.subplot(1, 2 , 1)
plt.title("Hubungan Harga Produk dan Jumlah Produk Terjual")
plt.scatter(data["Harga Produk"], data["Jumlah Beli"])
plt.xlabel("Harga Produk")
plt.ylabel("Jumlah Produk Terjual")

plt.subplot(1, 2, 2)
plt.title("Pendapatan Produk")
plt.bar(data["Nama Produk"], data["Total Harga"])
plt.xlabel("Nama Produk")
plt.ylabel("Pendapatan Produk")
plt.show()