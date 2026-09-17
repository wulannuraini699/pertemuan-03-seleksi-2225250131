# INPUT: Meminta pengguna memasukkan dua bilangan (bisa desimal)
a = float(input("Bilangan pertama: "))
b = float(input("Bilangan kedua: "))

# PROSES KEPUTUSAN & OUTPUT: Menggunakan nested if untuk membandingkan
if a >= b:
    if a == b:
        print("Kedua bilangan sama.")
    else:
        print("Bilangan pertama lebih besar.")
else:
    print("Bilangan pertama lebih kecil.")