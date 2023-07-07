# intro_to_python
Project sederhana ini di buat sebagai salah satu pra-syarat kelulusan kelas "Basic Python" di Pacmann Academy- Jakarta, Indonesia
Created on : June 2023

## Objectives
- Mengaplikasikan konsep dasar python, yang diharapkan dapat menjadi `solid foundation` untuk penggunaan python untuk keperluan data analysis dll 
- Mengaplikasikan pembuatan program dengan menggunakan konsep OOP
- Mengaplikasikan pembuatan program dengan memperhatikan kaidah penulisan code yang bersih (clean code) dengan mengacu pada panduan PEP8

## Deskripsi Singkat Program
Project ini bertujuan untuk mensimulasikan aktivitas cashier, dimana user di berikan kebebasan untuk melakukan input dan mengolah daftar belanjaan nya (self service cashier).
- Terdiri dari 2 file py, yaitu 'project.py' dan 'module.py'
- project.py : sebagai program utama yang akan memanggil dan meng cluster feature program
- module.py : sebagai wadah untuk function dan class (method) yang di gunakan oleh main.py
- secara garis besar, flow chart program dapat di lihat pada gambar di bawah :

![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/d46d70d3-fcc6-4ba3-8b58-5202bff625cd)

## How to Use
- Pastikan file project.py dan module.py dalam working directory yang sama
- Program dapat di panggil menggunakan Terminal, command : python project.py

## Tools dan Requirement
- Tools yang di gunakan menggunakan bahasa Python (saat pengerjaan menggunakan python ver 3.8.2 rc2), beserta beberapa library standard bawaan python guna menunjang "pencapaian requirement" yang di tetapkan. Metoda yang di gunakan adalah penggunaan dictionary dalam mengakses dan mengolah data yang di masukkan oleh user. Pemilihan dictionary, dengan pertimbangan bahwa pemahaman dictionary yg baik di harapkan dapat lebih mempermudah dalam pengolahan data di kemudian hari terutama penggunaan library pandas
- Requirement :
Seperti hal nya sebuah proses database, maka konsep dasar CRUD harus memiliki.
  * C (Create)
User dapat membuat record dengan memasukkan data yang di minta 
  * R (Read)
Untuk memverifikasi data, setiap action maka program akan mendisplay data terupdate dlm bentuk table
  * U (Update)
Jika user hendak me revisi field tertentu dari record tertentu (atau menambah data), maka program juga mengakomodir proses revisi tersebut
  * D (Delete)
Jika user memiliki pendapat lain saat proses perubahan, maka user dapat memilih untuk men "delete" baik berupa record tertentu atau bahkan keseluruhan.

## Deskripsi dan Test Case

- Saat awal program di jalankan, user akan di hadapkan pada menu pilihan :
  
  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/59ca1719-12c1-4089-8ecf-9f50179961c4)

  Misalkan user salah memilih, maka akan di tampilkan info bahwa pilihan di luar range yang di tetapkan :
  
  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/262bd306-6532-4cfa-94c0-e0a1e0b9d487)

- Opsi 1, akan membawa user kepada proses input pembelian barang.
  Guna mempermudah pemeriksaan, maka setelah user selesai meng input data pembelian maka akan di berikan list dalam bentuk table hasil inputan (basket)
  
  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/549b5a1a-2ddf-4ee9-bbb3-7c2c22338c0c)
  
  Andai user menginput di "Nama Barang" berupa Digit (int or float), maka sebagai proses "error proofing", program akan menampilkan pesan kesalahan, dan me request utk input ulang
  
  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/8d62d5e9-c240-401d-9008-0b6e8edccfb8)

  Demikian juga untuk input qty
  
  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/1ac1ed64-4a7b-431e-85e0-ae966ecb685b)

- Opsi 2, di gunakan jika pada saat user memerlukan "hint" untuk melakukan revisi (misal qty atau nama barang). User cukup memberikan  "partial words" dari nama item. Program akan memberikan rekomendasi item yg mengandung sebagian/keseluruhan kata tsb.
  Misal terdapat data pembelian seperti gambar di bawah, user hendak mencari item dengan keyword "ayam" :
  
  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/1a95b438-26ea-4223-9771-408bbb1c9d56)

  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/73f53697-475b-4b01-9598-c6a5f002d682)


- Opsi 3, akan membawa user kepada proses revisi "nama barang' yang telah di input pada step 1. Setelah user menginputkan nama item yang akan di revisi, kembali akan di berikan display berupa table agar user dapat mengecek ulang proses revisi yang di lakukan

  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/a8453055-cbc4-4141-af28-7bbdc2f47c6c)

  Andai user memberikan nama barang yang belum ada di basket, maka program akan memberikan info bahwa item tdk ada
  
  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/db89cd65-a8f8-4fd4-992b-8bc05e6c40a5)


- Opsi 4, digunakan jika user hendak merevisi qty belanjaan. Keyword untuk proses recall record yang ada, menggunakan nama item. Jika hendak mencari nama item berdasarkan keyword tertentu, gunakan opsi 2

  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/11c21590-0440-426e-a7ec-535e17069cb3)


- Opsi 5, digunakan jika user hendak merevisi harga belanjaan. Keyword untuk proses recall record yang ada, menggunakan nama item. Jika hendak mencari nama item berdasarkan keyword tertentu, gunakan opsi 2
 
  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/af83f82c-d507-40cb-8362-6b572dc0d3f9)

- Opsi 6, digunakan jika user hendak membatalkan barang tertentu yang sudah ada di dalam list (basket) belanja.
 
  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/60702308-a40a-4556-b2b4-597280088ffd)

- Opsi 7, di gunakan untuk menampilkan keranjang belanjaan (current basket) yang ada saat itu. Misal kan user telah melakukan penambahan beberapa item selain "pasta gigi" yang tersisa, maka display basket adalah sebagai berikut :

  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/98b5f4b0-4798-41fb-af14-2596ff95c43b)


- Opsi 8, digunakan jika user telah selesai berbelanja, dan akan menghitung total belanjaan nya (dan jumlah diskon, andaikan memenuhi persyaratan nominal belanja tertentu). Program juga secara otomatis meng generate file txt yang dapat di gunakan untuk keperluan print out. Data di tambahkan item mainan

  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/cacb5c14-a2b8-44a9-9053-c2aae57affaa)

  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/b939f2e2-9384-474e-8804-0de432c3be19)

- Opsi 9, akan di gunakan jika user hendak membatalkan keseluruhan pembelian yang ada.

  ![image](https://github.com/juhono/Intro_Python_Pacmann/assets/138840256/4a4e6141-9957-4692-872e-aa417dfed6db)


## Saran dan Masukkan
- Program masih bisa di extend, misal setelah user melakukan perubahan, dapat di berikan info "feature" apa yang di edit/di revisi
- Penggunaan decorator dan dataclasses bisa di pertimbangkan untuk di implementasikan agar program dapat lebih readable (lebih friendly)
- Bisa menggunakan konsep encapsulation untuk instance harga
- Program ini terbuka untuk di gunakan secara bebas untuk proses pembelajaran basic python. Silahkan di revisi dan di kembangkan lebih lanjut. Selamat berkarya.
- Akhir kata, tidak lupa mengucapkan banyak terima kasih atas bimbingan nya selama training di pacmann kepada Trainer dan Teaching Assistant pada kelas "intro to python"



