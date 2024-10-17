def find_largest_number():
    largest = None  # Inisialisasi variabel untuk menyimpan bilangan terbesar
    while True:
        try:
            number = int(input("Masukkan angka (masukkan 0 untuk berhenti): "))
            if number == 0:  # Jika pengguna memasukkan 0, keluar dari loop
                break
            if largest is None or number > largest:  # Periksa apakah number lebih besar dari largest
                largest = number
        except ValueError:
            print("Tolong masukkan angka yang valid.")  # Menangani input yang tidak valid

    if largest is not None:
        print(f"Bilangan terbesar yang dimasukkan adalah: {largest}")
    else:
        print("Tidak ada bilangan yang dimasukkan.")

# Panggil fungsi
find_largest_number()