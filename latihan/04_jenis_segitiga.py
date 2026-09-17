# INPUT: Meminta pengguna memasukkan tiga panjang sisi segitiga (konversi ke float)
a = float(input("Sisi a: "))
b = float(input("Sisi b: "))
c = float(input("Sisi c: "))

# PROSES KEPUTUSAN: Memeriksa syarat validitas terbentuknya segitiga (pertidaksamaan segitiga)
if a + b > c and a + c > b and b + c > a:
    # NESTED IF: Menentukan jenis segitiga berdasarkan panjang sisinya
    if a == b and b == c:
        # OUTPUT: Jika ketiga sisi sama panjang
        print("Segitiga sama sisi")
    else:
        if a == b or a == c or b == c:
            # OUTPUT: Jika dua sisi sama panjang
            print("Segitiga sama kaki")
        else:
            # OUTPUT: Jika ketiga sisi berbeda panjangnya
            print("Segitiga sembarang")
else:
    # OUTPUT: Jika kombinasi sisi tidak memenuhi syarat segitiga
    print("Ketiga sisi tidak membentuk segitiga")