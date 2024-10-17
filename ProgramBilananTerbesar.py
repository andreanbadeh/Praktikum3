def bilangan_terbesar(a, b, c):
    if a > b:
        terbesar = a
    else:
        terbesar = b

    if terbesar < c:
        terbesar = c

    return terbesar

# Inputkan 3 buah bilangan
a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

# Cetak bilangan terbesar
print("Bilangan terbesar adalah:", bilangan_terbesar(a, b, c))