import os
import time
import module
from tabulate import tabulate

# Memanggil function clean di module.py
# Membersihkan layar Display agar tdk terlalu "crowded" 
# Fungsi seperti console.clear() di C#
module.clean()
print(f"Hello,.....{os.getlogin()}")
print(f"Ini adalah program Pra-Syarat Basic Python @ Pacmann")
# Delay selama 3 second agar user memiliki kesempatan membaca "greeting"
time.sleep(3)

while True:
    module.clean()
    title1 = " SELAMAT DATANG DI SUPERSTORE PAC-STORE "
    title2 = "PROJECT UTK PRASYARAT KELAS BASIC PYTHON"
    print(title1)
    print(title2)
    print("=" * max(len(title1),len(title2)), end="\n\n")
    print(f"Silahkan pilih dari salah satu menu di bawah")
    print(f"1. Pembelian")
    print(f"2. Cari Nama")
    print(f"3. Edit Nama")  
    print(f"4. Edit Quantity")  
    print(f"5. Edit Harga")
    print(f"6. Delete Item")
    print(f"7. Lihat Keranjang Belanjaan")
    print(f"8. Hitung total dan save")
    print(f"9. Batalkan pembelian\n")

    user_option = input("Masukkan opsi (angka saja) : ")

    if user_option == "1":
        """ Opsi Untuk Memasukkan Data Pertama Kali
        Input:
            Nama Barang / Item : Char (str)
            Qty dan Price      : Digit (int)
        """
        result = module.initial()
        print(module.print_table(result))

    elif user_option == "2":
        """ Opsi Untuk Mencari /Find Nama Barang Berdasarkan Keyword Tertentu
        Input:
            Nama Barang / Item : Char (str)
        Output:
            Tabel Alternatif Nama Barang
        """
        module.clean()
        search_str = input("Masukkan Nama Yang Akan di Cari : ").title()
        instance_search = module.Store(result)
        instance_search.search_name(search_str)

    elif user_option == "3":
        """ Opsi Untuk Merevisi Nama Barang
        Input:
            Nama Barang Awal   : Char (str)
            Nama Barang Revisi : Char (str)
        Output:
            Tabel Dengan Update Nama Barang Revisi
        """
        module.clean()
        curr_name = input ("Masukkan Nama Awal \t: ").title()
        rev_name = input ("Masukkan Nama Revisi \t: ").title()
        instance1 = module.Store(result)
        instance1.update_name(curr_name,rev_name)

    elif user_option == "4":
        """ Opsi Untuk Merevisi Qty dari Nama Barang Tertentu
        Input:
            Nama Barang         : Char (str)
            Qty Barang Revisi   : Digit (int)
        Output:
            Tabel Dengan Update Nama Barang Revisi
        """
        module.clean()
        try:
            name_value = input("Masukkan Nama Item yang Qty ingin di Rev : ")
            rev_value = int(input("Masukkan Qty Revisi : "))
            if not isinstance (rev_value, int):
                raise Exception
            instance2 = module.Store(result)
            instance2.update_qty(name_value,rev_value)
        except Exception:
            print("Nilai yang Anda masukkan harus numerik bulat")

    elif user_option == "5" :
        """ Opsi Untuk Merevisi Harga dari Nama Barang Tertentu
        Input:
            Nama Barang         : Char (str)
            Hrg Barang Revisi   : Digit (int)
        Output:
            Tabel Dengan Update Harga Barang Revisi
        """
        module.clean()
        try:
            name_price = input("Masukkan Nama Rev \t: y")
            rev_price = float(input("Masukkan Harga Revisi \t: "))
            if not isinstance (rev_price, float):
                raise Exception
            instance3 = module.Store(result)
            instance3.update_price(name_price,rev_price)
        except Exception:
            print("Nilai yang Anda masukkan harus numerik")

    elif user_option == "6":
        """ Opsi Untuk Men"delete" Barang Yang Telah di Beli
        Input:
            Nama Barang         : Char (str)
        Output:
            Tabel Dengan Update Status Barang Yang Masih Tersisa di Basket
        """
        module.clean()
        item_del = input("Masukkan nama item yang akan di delete : ")
        instance4 = module.Store(result)
        instance4.delete_item(item_del)

    elif user_option == "7":
        """ Opsi Untuk Menampilkan Keranjang Belanja
        Output:
            Tabel Dengan Barang Yang Ada di Basket
        """
        module.clean()
        try :
            instance5 = module.Store(result)
            instance5.show_basket
        except NameError:
            print("keranjang masih kosong")

    elif user_option == "8":
        """ Opsi Untuk Menampilkan Final Price Dan Export ke file ext txt, agar bisa di cetak
        Output:
            Tabel Dengan Barang Yang Ada di Basket
            Info Diskon (Jika ada)
            Info Total Yang Harus di Bayar
            File .txt untuk di print
        """
        instance6 = module.Store(result)
        instance6.calc_final

    elif user_option == "9":
        """ Opsi Untuk Menampilkan Final Price Dan Export ke file ext txt, agar bisa di cetak
        Output:
            Tabel Dengan Barang Yang Ada di Basket
            Info Diskon (Jika ada)
            Info Total Yang Harus di Bayar
            File .txt untuk di print
        """
        instance7 = module.Store(result)
        instance7.cancel_all

    else:
        """ Menu jika user tidak memberikan inputan atau pilihan yang sesuai
        """
        print("\nSilahkan ulang kembali, anda memilih menu yg salah\n")

    print("\n================================= \n")
    is_done = input('Apakah akan melanjutkan ke menu utama (y/n)? ').lower() == "n"
    if is_done :
        print("Terima kasih sudah berbelanja di Pac-Store")
        break
