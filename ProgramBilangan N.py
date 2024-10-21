max=0

while True:
    N = int(input("Masukkan angka: "))
    
    if N == 0:
        print(f"angka terbesar adalah: {max}")
        break
    if N > max:
        max = N