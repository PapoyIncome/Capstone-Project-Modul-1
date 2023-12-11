import os, random
os.system('cls')
from tabulate import tabulate

def generate_nopeg():
    nomor_acak = str(random.randint(10000, 99999))
    nopeg = 'NPR' + nomor_acak 
    #listB [i] [0] nopeg
    for i in range(len(listB)):
            if listB[i][0] == nopeg:     
                continue
            else:           
                return nopeg
    
    #menampilkan key yang ada di header dan valunya ada didalam listB
def my_print(key):
    header = ["No", "Nopeg", "Nama Pegawai", "Jabatan", "Gaji Karyawan", "Domisili", "Hazzard", "Keterangan"]
    table_data = []
    
    #merapikan data berdasarkan urutan 
    for i, data in enumerate(key, start=1):
        data = [str(datapersonal).upper() 
                for datapersonal in data]
        table_data.append([i] + data)
    
    # Menggunakan tabulate untuk mencetak tabel
    print("Daftar Pegawai")
    print(tabulate(table_data, headers=header, tablefmt="pretty"))  

listB = [
    ["NPR85444","Muhammad Reza","Direktur",15000000,"Dalam Kota","Non Ketinggian","-"],
    ["NRP24888","Teguh Darmawan","Human Capital",7500000,"Luar Kota","Non Ketinggian","-"],
    ["NPR24966","Deris Firaun","Operational",10000000,"Luar Kota","Ketinggian","-"],
    ["NPR23577","Yudi Kurniawan","NDT LVL1",7000000,"Dalam Kota","Ketinggian","SP1"],
    ["NPR22444","Wildan Firdaus","Tank Inspector",13000000,"Luar Kota","Ketinggian","-"]
]

kalimat = """
Selamat Datang di Sistem Informasi Kepegawaian PT. SETCO QUALITY

List Menu:
1. Menampilkan Daftar Pegawai (R)
2. Menambahkan Daftar Pegawai (C)
3. Menghapus Pegawai (D)
4. Mengubah Data Pegawai (U) 
5. Exit Program
"""

kalimat_submenu = """
Pilih Varible yg Ingin Di Update  


1. Nama Pegawai
2. jabatan Pegawai 
3. Gaji Pegawai 
4. Domisili Pegawai
5. Hazzard 
6. Keterangan Pegawai
7. Update Total
8. Exit
"""
while True:
    try:
        print(kalimat)
        n = int(input("Masukan Pilihan Menu Yang Ingin Dijalankan: "))

        if n == 1:
            my_print(listB)
        elif n == 2:
                       
            while True :
                try:
                    os.system('cls')
                    my_print(listB)
                    nopeg = generate_nopeg()
                    nama = input("Masukkan Nama Pegawai: ")
                    jabatan = input("Jabatan: ")
                    #agar tidak terjadi kesalahan input
                    while True :
                        harga = input("Masukkan Gaji: ")
                        if harga.isdigit() == True :
                            break 
                        else : print("Masukan Angka Dengan Benar !")
                    domisili = input("Apakah Dari Dalam Kota (y/n) : ")
                    if domisili.lower() == 'y' :
                        domisili = 'Dalam Kota' 
                    elif domisili.lower() == 'n':
                        domisili = 'Luar Kota'
                    else: continue
                    
                    hazzard = input("Masukan Hazzard Ketinggian (y/n) : ")
                    if hazzard.lower() == 'y' :
                        hazzard = 'Ketinggian'
                    elif hazzard.lower() == 'n' :
                        hazzard = 'Non Ketinggian'
                    else: continue
                    keterangan_pegawai = "-"
                    
                    
                    break
                except Exception as e:
                    print(f"Terjadi kesalahan: {e}")
                    input('Enter untuk melanjutkan...')
            
            t = [nopeg, nama, jabatan, harga, domisili, hazzard, keterangan_pegawai]
            listB.append(t)
            my_print(listB)
        elif n == 3:
            my_print(listB)
            nopeg_delete = input("Masukkan Nopeg Yang Ingin Di Delete: ")
             # mendelete berdasarkan nopeg
            for i in listB:
                if i[0] == str(nopeg_delete):
                    listB.pop(listB.index(i))
                    my_print(listB)
        elif n == 4:
            my_print(listB)
            update = input("Masukan Nomor Pegawai Yang ingin di Update: ")
            while True:
                print(kalimat_submenu)
                n = int(input("Masukkan No Menu yang Ingin Diganti : "))
                if n == 1 :
                    name_new = input("Masukan Nama yang baru :")
                    for i in listB:
                        if i[0] == str(update):
                            i[1] = name_new
                elif n == 2 :
                    jabatan_new = input("Masukan Jabatan Baru: ")
                    for i in listB:
                        if i[0] == str(update):
                            i[2] = jabatan_new
                elif n == 3 :
                    while True :
                        gaji_new = input("Masukkan Gaji: ")
                        if gaji_new.isdigit() == True :
                            break 
                        else : print("Masukan Angka Dengan Benar !")
                    for i in listB:
                        if i[0] == str(update):
                            i[3] = gaji_new
                            
                elif n == 4 :
                    domisili_new = input("Masukan Domilisi yg Baru (y/n) : ")
                    if domisili_new.lower() == 'y' :
                        domisili_new = 'Dalam Kota' 
                    elif domisili_new.lower() == 'n':
                        domisili_new = 'Luar Kota'
                    else: continue
                    for i in listB:
                        if i[0] == str(update):
                            i[4] = domisili_new
                elif n == 5 :
                    hazzard_new = input("Masukan hazzard yang Baru (y/n) : ")
                    if hazzard_new.lower() == 'y' :
                        hazzard_new = 'Ketinggian' 
                    elif hazzard_new.lower() == 'n':
                        hazzard_new = 'Non Ketinggian'
                    else: continue
                    for i in listB:
                        if i[0] == str(update):
                            i[5] = hazzard_new
                elif n == 6 : 
                    keterangan_pegawai_new = input("Masukan Keterangan: ")
                    if keterangan_pegawai_new == "":
                        keterangan_pegawai_new = "-"
                    for i in listB:
                        if i[0] == str(update):
                            i[6] = keterangan_pegawai_new   
                elif n == 7 :
                    name_new = input("Masukan Nama yang baru :")
                    jabatan_new = input("Masukan Jabatan Baru: ")
                    while True :
                        gaji_new = input("Masukkan Gaji: ")
                        if gaji_new.isdigit() == True :
                            break 
                        else : print("Masukan Angka Dengan Benar !")
                    domisili_new = input("Masukan Domilisi yg Baru (y/n) : ")
                    if domisili_new.lower() == 'y' :
                        domisili_new = 'Dalam Kota' 
                    elif domisili_new.lower() == 'n':
                        domisili_new = 'Luar Kota'
                    else: continue
                    hazzard_new = input("Masukan hazzard yang Baru (y/n) : ")
                    if hazzard_new.lower() == 'y' :
                        hazzard_new = 'Ketinggian' 
                    elif hazzard_new.lower() == 'n':
                        hazzard_new = 'Non Ketinggian'
                    else: continue
                    keterangan_pegawai_new = input("Masukan Keterangan: ")
                    if keterangan_pegawai_new == "":
                        keterangan_pegawai_new = "-"
                    for i in listB:
                        if i[0] == str(update):
                            i[1] = name_new
                            i[2] = jabatan_new
                            i[3] = gaji_new
                            i[4] = domisili_new
                            i[5] = hazzard_new
                            i[6] = keterangan_pegawai_new
                            my_print(listB)
                elif n == 8 :
                    break 
                for i in listB:
                        if i[0] == str(update):
                            print(i)
        elif n == 5:
            break
        else: 
            print("Pilih Menu yang benar !")    
            
    except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            input('Enter untuk melanjutkan...')