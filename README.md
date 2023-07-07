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

  ![image](https://github.com/juhono/intro_to_python/assets/138840256/c8d0ac9c-2e92-44ad-836d-930bebb89686)

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
  
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/9f37daef-c83d-4137-b8e4-5bacee4f21bd)
  
  Misalkan user salah memilih, maka akan di tampilkan info bahwa pilihan di luar range yang di tetapkan :
  
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/dd8b0370-2228-484d-825f-d1871a262e60)

- Opsi 1, akan membawa user kepada proses input pembelian barang.
  Guna mempermudah pemeriksaan, maka setelah user selesai meng input data pembelian maka akan di berikan list dalam bentuk table hasil inputan (basket)
  
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/371264dc-5d85-4a24-83dd-7c261923bf13)
  
  Andai user menginput di "Nama Barang" berupa Digit (int or float), maka sebagai proses "error proofing", program akan menampilkan pesan kesalahan, dan me request utk input ulang
  
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/49a2ffb7-a12d-4046-8c81-ba4deac0e953)
  
  Demikian juga untuk input qty
  
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/3db19451-24c7-4216-b12c-fb7b73198920)

- Opsi 2, di gunakan jika pada saat user memerlukan "hint" untuk melakukan revisi (misal qty atau nama barang). User cukup memberikan  "partial words" dari nama item. Program akan memberikan rekomendasi item yg mengandung sebagian/keseluruhan kata tsb.
  Misal terdapat data pembelian seperti gambar di bawah, user hendak merubah item dengan keyword "ayam" :
  
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/1a0c4a2f-3917-4f7b-b640-7a91dbe1c9e4)

  ![image](https://github.com/juhono/intro_to_python/assets/138840256/a0972d3c-2c50-4b7f-b2e5-21afc4f9d35f)

- Opsi 3, akan membawa user kepada proses revisi "nama barang' yang telah di input pada step 1. Setelah user menginputkan nama item yang akan di revisi, kembali akan di berikan display berupa table agar user dapat mengecek ulang proses revisi yang di lakukan

  ![image](https://github.com/juhono/intro_to_python/assets/138840256/9fda156e-74f9-4eb5-84d6-c2a367096284)

  Andai user memberikan nama barang yang belum ada di basket, maka program akan memberikan info bahwa item tdk ada
  
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/dca2ccf7-2892-4eb5-9c2b-821f98cf9fbe)

- Opsi 4, digunakan jika user hendak merevisi qty belanjaan. Keyword untuk proses recall record yang ada, menggunakan nama item. Jika hendak mencari nama item berdasarkan keyword tertentu, gunakan opsi 2

  ![image](https://github.com/juhono/intro_to_python/assets/138840256/35246387-1494-4617-b880-56aa47934743)


- Opsi 5, digunakan jika user hendak merevisi harga belanjaan. Keyword untuk proses recall record yang ada, menggunakan nama item. Jika hendak mencari nama item berdasarkan keyword tertentu, gunakan opsi 2
 
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/81981646-45b0-41b8-9547-f7cd1974fe1b)

  
- Opsi 6, digunakan jika user hendak membatalkan barang tertentu yang sudah ada di dalam list (basket) belanja.
 
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/2984f829-7569-4e78-a9be-c5b3eca6eab7)

- Opsi 7, di gunakan untuk menampilkan keranjang belanjaan (current basket) yang ada saat itu. Misal kan user telah melakukan penambahan beberapa item selain "pasta gigi" yang tersisa, maka display basket adalah sebagai berikut :

  ![image](https://github.com/juhono/intro_to_python/assets/138840256/43d24b78-ad51-4798-805b-21f28a3b8637)

- Opsi 8, digunakan jika user telah selesai berbelanja, dan akan menghitung total belanjaan nya (dan jumlah diskon, andaikan memenuhi persyaratan nominal belanja tertentu). Program juga secara otomatis meng generate file txt yang dapat di gunakan untuk keperluan print out.
  
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/4208dad1-1d9f-4916-8885-65d9ff1d94d0)

  ![image](https://github.com/juhono/intro_to_python/assets/138840256/3e438081-cece-4ca9-b5bf-682125a0dcec)

- Opsi 9, akan di gunakan jika user hendak membatalkan keseluruhan pembelian yang ada.
 
  ![image](https://github.com/juhono/intro_to_python/assets/138840256/23c8f087-306a-4397-ace5-baeec3cbe028)

  ![image](https://github.com/juhono/intro_to_python/assets/138840256/eadffa4b-3a99-40df-9ef4-aca1719a8312)

## Saran dan Masukkan
- Program masih bisa di extend, misal setelah user melakukan perubahan, dapat di berikan info "feature" apa yang di edit/di revisi
- Penggunaan decorator dan dataclasses bisa di pertimbangkan untuk di implementasikan agar program dapat lebih readable (lebih friendly)
- Bisa menggunakan konsep encapsulation untuk instance harga
- Program ini terbuka untuk di gunakan secara bebas untuk proses pembelajaran basic python. Silahkan di revisi dan di kembangkan lebih lanjut. Selamat berkarya.
- Akhir kata, tidak lupa mengucapkan banyak terima kasih atas bimbingan nya selama training di pacmann kepada Trainer dan Teaching Assistant pada kelas "intro to python"



