# TIPE-DATA-VARIABLE-DAN-OPERATOR
Nama: ANDREAN PUTRA ARYA

Kelas: TI.24.A4

NIM: 312410341

Matkul: Bahasa Pemrograman

# LATIHAN1
![gambar](https://github.com/andreanbadeh/fotoo/blob/b7f3e037371e3220864e809559de3a357e404c7b/Screenshot%202024-10-15%20143542.png)
```python
#penggunaan end
print('A', end='')
print('B', end='')
print('C', end='')
print()
print('X')
print('Y')
print('z')

#penggunaan separator
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='.....')
````

Penggunaan END Penggunaan end digunakan untuk menambahkan karakter yang dicetak di akhir baris. secara default penggunaan end adalah untuk ganti baris.

```python
print('A', end='')
print('B', end='')
print('C', end='')
```
Penggunaan print () digunakan untuk mencetak output, seperti syntax dibawah ini :
```python
print()
```
Syntax dibawah ini digunakan untuk menampilkan output berupa string
```python
print('X')
print('Y')
print('z')
```
Hasil dari source code tersebut seperti gambar dibawah ini :

![gambar](https://github.com/andreanbadeh/fotoo/blob/5897a8fe928d65b7b12aa3a8408391ca3dfd490c/Screenshot%202024-10-15%20133640.png)

Penggunaan separator
Pendeklarasian beberapa variable beserta nilainya
```python
w,x,y,z=10,15,20,25
```
Menampilkan hasil dari variable tiap-tiap variable
```python
print(w,x,y,z)
```
Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemirsah : (koma)
```python
print(w,x,y,z,sep=",")
```
Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemirsah

```python
print(w,x,y,z,sep="")
```
Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemirsah : (titik dua)
```python
print(w,x,y,z,sep=":")
```
Menampilkan hasil dari tiap-tiap variable dengan menggunakan pemirsah -----
```python
print(w,x,y,z,sep="-----")
```
hasil dari syntax / source code diatas adalah seperti berikut ini :

![gambar](https://github.com/andreanbadeh/fotoo/blob/5897a8fe928d65b7b12aa3a8408391ca3dfd490c/Screenshot%202024-10-15%20133703.png)

## LATIHAN 2

![gambar](https://github.com/andreanbadeh/fotoo/blob/9b329a799a6e999ad0d62d0fa79e00a0392c3a39/Screenshot%202024-10-15%20135657.png)
```python
a=int(input("masukkan nilai a:"))
b=int(input("masukkan nilai b:"))
print("variable a=",a)
print("variable b=",b)
print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("hasil pejumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))
```
Kita akan coba lagi untuk run file tersebut, maka akan muncul seperti gambar dibawah ini :

![gambar](https://github.com/andreanbadeh/fotoo/blob/2c18a50361f6617ac1c5624ae6ca16c2449b0885/Screenshot%202024-10-15%20140328.png)

String Format
String formatting atau pemformatan string memungkinan kita menyuntikkan item kedalam string dari pada kita mencoba menggabungkan string menggunakan koma atau string concatenation.
Penggunaan source code yang di berikan oleh dosen seperti berikut :

![gambar](https://github.com/andreanbadeh/fotoo/blob/2c18a50361f6617ac1c5624ae6ca16c2449b0885/Screenshot%202024-10-15%20140431.png)

```python
#string format 1
print(0, 10**0)
print(1, 10**1)
print(2, 10**2)
print(3, 10**3)
print(4, 10**4)
print(5, 10**5)
print(6, 10**5)
print(8, 10**8)
print(9, 10**9)
print(10, 10**10)

#string format 2
print('{0:>3} {1:>16}'.format(0, 10**0))
print('{0:>3} {1:>16}'.format(1, 10**1))
print('{0:>3} {1:>16}'.format(2, 10**2))
print('{0:>3} {1:>16}'.format(3, 10**3))
print('{0:>3} {1:>16}'.format(4, 10**4))
print('{0:>3} {1:>16}'.format(5, 10**5))
print('{0:>3} {1:>16}'.format(6, 10**6))
print('{0:>3} {1:>16}'.format(7, 10**7))
print('{0:>3} {1:>16}'.format(8, 10**8))
print('{0:>3} {1:>16}'.format(9, 10**9))
print('{0:>3} {1:>16}'.format(10, 10**10))
```
String Format 1
Pada syntax / source code strring format satu akan menampilkan output berupa 2 outputan.
Yang pertama (sebelah kiri) akan menampilkan angka urut dari angka 0 hingga 10, sedangkan untuk sebelah kanan akan menampilkan Operasi Aritmatika Pangkat.
Dengan ketentuan sebagai berikut, Operasi pangkat dengan angka kiri sebagai pokok (Rumus : ** [bintang dua] )
Hasil dari syntax tersebut adalah 10 pangkat 0, hingga 10 pangkat 10, dengan output sebagai berikut :

![gambar](https://github.com/andreanbadeh/fotoo/blob/77df8a18e59b99556aa69a5514bbdc67d555516d/Screenshot%202024-10-15%20141036.png)

2 * String Format 2*
Pada syntax atau source code string format dua akan menampilkan output berupa 2 output'an juga (seperti String Format 1, yaitu kanan dan kiri )
Dengan ketentuan sebagai berikut :

secara Default, .format() menggunakan rata kiri, angka ke kanan. kita dapat menggunakan opsi opsional <,^, atau > untuk mengatur perataan kiri, tengah, atau kanan. Contoh lain dalam penggunaan .format() sebagai berikut :

![gambar](https://github.com/andreanbadeh/fotoo/blob/deb296e96f491981b8dede207ba1eb8456c03837/Screenshot%202024-10-15%20141347.png)

Untuk hasil dari String Format 2 adalah :

## Tugas Latihan
![gambar](https://github.com/andreanbadeh/fotoo/blob/fee7f554ebd75304da4d93e6eef690efad8d7166/Screenshot%202024-10-15%20142113.png)

# Flowchart Bilangan terbesar dari 3 buah bilangan
![gambar](https://github.com/andreanbadeh/fotoo/blob/bd9e3adde0f5631af42bdff66f2ec22c17f9056e/Gambar%20WhatsApp%202024-10-17%20pukul%2000.34.59_95aec777.jpg)

# Program bilangan terbesar dari 3 buah yg di inputkan
![gambar](https://github.com/andreanbadeh/fotoo/blob/5d260e088cd8f193f1e60434f5cd10c240a56f19/Screenshot%202024-10-17%20222816.png)

melalui pernyataan kondisi if-else, program membandingkan bilangan pertama dengan bilangan kedua dan ketiga, dan seterusnya.

Hasil output

![gambar](https://github.com/andreanbadeh/fotoo/blob/5d260e088cd8f193f1e60434f5cd10c240a56f19/Screenshot%202024-10-17%20222919.png)

untuk meminta pengguna untuk memasukkan tiga bilangan, 

# Flowchart Bilangan terbesar N
![gambar](https://github.com/andreanbadeh/fotoo/blob/ce18dadba5891432472b0e35fe65ac9f347d661d/Gambar%20WhatsApp%202024-10-17%20pukul%2012.53.34_cd402e92.jpg)

# Program bilangan terbesar N 
![gambar](https://github.com/andreanbadeh/fotoo/blob/8b14639ecd89e396334a53319be6fefe84e6666c/Screenshot%20From%202024-10-21%2022-40-07.png)

setiap angka yang diinputkan diperiksa apakah lebih besar dari angka terbesar yang saat ini di simpan

Hasil output

![gambar](https://github.com/andreanbadeh/fotoo/blob/8b14639ecd89e396334a53319be6fefe84e6666c/Screenshot%20From%202024-10-21%2022-41-55.png)

jika pengguna memasukkan angka 0, program akan memberi tahu bahwa tidak ada bilangan yang dimasukkan dan tidak akan melanjutkan untuk meminta bilangan lebih lanjut
