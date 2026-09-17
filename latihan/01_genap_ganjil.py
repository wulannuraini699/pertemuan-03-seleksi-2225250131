# INPUT: Meminta pengguna memasukkan satu bilangan bulat
bilangan = int(input("Masukkan bilangan bulat: "))

# PROSES KEPUTUSAN: Memeriksa apakah sisa hasil bagi dengan 2 adalah 0
if bilangan % 2 == 0:
    # OUTPUT: Ditampilkan jika bilangan genap
    print(f"{bilangan} adalah bilangan genap.")
else:
    # OUTPUT: Ditampilkan jika bilangan ganjil
    print(f"{bilangan} adalah bilangan ganjil.")