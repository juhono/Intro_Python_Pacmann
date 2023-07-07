import os
import re
import time
from tabulate import tabulate


def clean():
    if os.name =="posix":
        os.system("clear")
    elif os.name =="nt" :
        os.system("cls")
        
def initial():
    list1 = []
    while True :
        try :
            while True :
                try :
                    name = input("Masukkan nama barang \t: ").title()
                    if not name.replace(" ","").isalpha() :
                        raise ValueError
                    break
                except ValueError :
                    print("Invalid, karakter yg Anda masukkan bukan string")
            qty = int(input("Qty pembelian \t: "))
            price = int(input("Harga barang \t: Rp "))
            if not isinstance (qty, int) :
                raise Exception
            list1.append(name)
            list1.append(qty)
            list1.append(price)
            repeat = input("Akan lanjut ke pembelian lagi (y/n)? ").lower()
            if (repeat=='y') :
                continue
            else :
                break
        except Exception :
            print("Harap hanya masukkan nilai numerik bulat, silahkan di ulang")
    result_dict = {list1[i]: [list1[i + 1],list1[i+2],list1[i + 1]*list1[i+2]] for i in range(0, len(list1), 3)}
    Store(result_dict)
    return result_dict

def print_table(mydata): 
    headers = ["Nama", "Qty", "Price/Unit", "sub Total"]
    index_tbl = [i for i in range(1,len(mydata)+1)]
    return(tabulate([(key,) + tuple(value) for key, value in mydata.items()], headers=headers, tablefmt='fancy_grid', showindex= index_tbl, missingval = "N/A"))

def calc_total(dataku1):
    total = 0
    for key,value in dataku1.items():
        total += value[2]
    print(f"Total belanja Anda saat ini adalah Rp : {total}")

class Store :
    def __init__(self,list_hasil):
        self.data = list_hasil

    def add(self):
        print(tabulate(self.data,headers="keys"))

    def update_name(self,exist_name,next_name):
        try:
            if exist_name not in self.data.keys():
                raise Exception
            self.data[next_name] = self.data[exist_name]
            del self.data[exist_name]
            print(print_table(self.data))
            calc_total(self.data)
        except Exception:
            print("Nama item yang Anda masukkan tidak ada, coba gunakan menu ke 2")

    def search_name(self, lookup_str):
        try:
            mylist = []
            for i in self.data.keys():
                mylist.append(i)
            r = re.compile(f".*{lookup_str}")
            newlist = list(filter(r.match, mylist))
            if len(newlist) != 0:
                print(f"Alternatif nama item yang Anda cari based on keyword, adalah :")
                print(tabulate([newlist], tablefmt='fancy_grid', showindex= False, missingval = "N/A"))
            else:
                print(f"Data tidak di temukan, apakah sdh memasukkan keyword dengan benar? ")
        except Exception:
            print("Maaf, Data tidak ditemukan")

    def update_qty(self,name_value1,rev_value1):
        try:
            if name_value1 not in self.data.keys():
                raise Exception
            self.data[name_value1][0] = rev_value1
            self.data[name_value1][2] = self.data[name_value1][0] * self.data[name_value1][1]
            print(print_table(self.data))
            calc_total(self.data)
        except Exception :
            print("Nama item yang Anda masukkan tidak ada dalam keranjang pembelian,\nSilahkan gunakan menu 1a utk cek nama item")
    
    def update_price(self,name_price,rev_price):
        try:
            if name_price not in self.data.keys():
                raise Exception
            self.data[name_price][1] = rev_price
            self.data[name_price][2] = self.data[name_price][0] * self.data[name_price][1]
            print(print_table(self.data))
            calc_total(self.data)
        except Exception:
            print("Maaf nama yang anda masukkan salah")
    
    def delete_item(self, item_del):
        try:
            if item_del not in self.data.keys():
                raise Exception
            print(f'Record dengan nama : {item_del} di hapus')
            del self.data[item_del]
            print(print_table(self.data))
            calc_total(self.data)
        except Exception:
            print("Maaf nama yang anda masukkan salah")
   
    @property
    def show_basket(self):
        if len(self.data) == 0:
            print(f"\nKeranjang Belanjaan Anda masih kosong")
        else:
            print(f"\nKeranjang Belanjaan Anda saat ini :")
            print(print_table(self.data))       
    
    @property
    def calc_final(self):
        total_all = 0
        for value in self.data.values():
            total_all += value[2]
        disc = 0
        disc = 0.1 if total_all > 50 else 0.08 if (30 < total_all <= 50) else 0.05 if (20 < total_all <= 30) else 0
        disc_all = disc * total_all
        print(f"Total pembelian Anda (sebelum diskon) adalah \t: {total_all}")

        if_true = "Maaf, Anda belum mendapat diskon"
        if_false = f"Selamat, Anda mendapat diskon sebesar \t\t: {disc_all}"
        print((if_false, if_true)[total_all <= 20])
        print(f"Total Belanja Yang Harus Anda Bayar adalah \t: {total_all - disc_all}")

        with open("data.txt",'w',encoding="utf-8") as file:
            file.write("Print Out Pembelanjaan @ Pac-Store \n")
            file.write(print_table(self.data))
            file.write("\n")
            file.write(f"Grand Total Pembayaran : Rp. {round(total_all - disc_all,2)}\n")
            file.write(f"Generated on : {time.strftime('%d-%B-%Y')}")
    
    @property
    def cancel_all(self):
        confirmation = input("Apakah anda yakin akan membatalkan semua transaksi (y/n)? ").lower()
        try :
            if confirmation not in ['y','n'] :
                raise Exception
            if confirmation == "y" :
                print("Semua transaksi Anda telah di hapus")
                self.data.clear()
                print(print_table(self.data))
            else :
                print("Proses Anda di batalkan, silahkan lanjutkan ke menu selanjutnya")
        except Exception :
            print("Harap memilih huruf 'Y' atau 'N' saja")
