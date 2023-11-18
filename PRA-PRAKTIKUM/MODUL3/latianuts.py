def hitung_total_harga(list_produk):
    return sum(x['harga'] for x in list_produk)
    
def hitung_total_produk(list_produk):
    return len(list_produk)
def main():
  list_produk = [
    {
      "nama": "Buku",
      "harga": 100000
    },
    {
      "nama": "Pensil",
      "harga": 20000
    },
    {
      "nama": "Penghapus",
      "harga": 5000
    }
  ]

  total_harga = hitung_total_harga(list_produk)
  print(total_harga)
  jumlah_produk = hitung_total_produk(list_produk)
  print(jumlah_produk)

if __name__ == "__main__":
  main()