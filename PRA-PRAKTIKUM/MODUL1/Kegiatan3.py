#Penilaian Akhir Mahasiswa


dictNilai = {}

#fungsi nilai akhir
def penghitunganNilai(nama,uas, uts):
    nilai = (uas + uts)/2
    dictNilai[nama] = nilai
    

#fungsi nilai akhir semua mahasiswa
def tampilkan_nilai_akhir():
    for x,y in dictNilai.items():
        print("Nama: {}\t Nilai Akhir: {}".format(x,y))
        
        

def main():
    data_mahasiswa = {
        "Rafli" : {
            "nama" : "rafli",
            "uas" : 90
            },
        "Alviya" : [100, 100],
        "Geraldi" : [95, 76],
        "Rizky" : [70, 100]
    }
    for nama,nilai in data_mahasiswa.items():
         penghitunganNilai(nama,nilai[0],nilai[1])
        

    
    tampilkan_nilai_akhir()
    
    
if __name__ == "__main__":
    main()
    
    
    
    