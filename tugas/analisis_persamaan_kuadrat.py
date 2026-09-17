import math

print("Analisis Persamaan Kuadrat")

# 1. Baca koefisien a, b, dan c sebagai float
a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

# 2. Periksa apakah a sama dengan 0
if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    # 3. Hitung diskriminan D
    diskriminan = b ** 2 - 4 * a * c
    print(f"Diskriminan = {diskriminan:.2f}")
    
    # 4 & 5. Nested if untuk tiga kemungkinan diskriminan
    if diskriminan > 0:
        # Menghitung dua akar real berbeda
        x1 = (-b + diskriminan ** 0.5) / (2 * a)
        x2 = (-b - diskriminan ** 0.5) / (2 * a)
        print(f"Dua akar real: {x1:.2f} dan {x2:.2f}")
    else:
        if diskriminan == 0:
            # Menghitung satu akar real kembar
            x = -b / (2 * a)
            print(f"Akar kembar: {x:.2f}")
        else:
            # Jika D < 0
            print("Tidak ada akar real")