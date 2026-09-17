# Pertemuan 03 Seleksi Python
Nama: Wulan Nur'aini  
NIM: 2225250131  
Kelas: 3E  

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan
python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
1. Meminta pengguna memasukkan nilai koefisien `a`, `b`, dan `c` bertipe data `float`.
2. Mengecek apakah nilai `a` sama dengan `0`:
   - Jika `a == 0`, tampilkan pesan bahwa input bukan merupakan persamaan kuadrat.
   - Jika `a != 0`, lanjut ke perhitungan diskriminan.
3. Menghitung nilai diskriminan $D$ menggunakan rumus $D = b^2 - 4ac$ dan menampilkan hasilnya dengan pembulatan dua angka di belakang koma.
4. Mengecek kondisi diskriminan menggunakan *nested if*:
   - Jika $D > 0$, hitung dua akar real berbeda ($x_1$ dan $x_2$) dengan rumus $x = \frac{-b \pm \sqrt{D}}{2a}$, lalu tampilkan nilainya.
   - Jika $D = 0$, hitung satu akar kembar dengan rumus $x = \frac{-b}{2a}$, lalu tampilkan nilainya.
   - Jika $D < 0$, tampilkan pesan bahwa persamaan tidak memiliki akar real.

## Hasil Pengujian

| No | Input (a, b, c) | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | 1, -5, 6 | Diskriminan = 1.00<br>Dua akar real: 3.00 dan 2.00 | Diskriminan = 1.00<br>Dua akar real: 3.00 dan 2.00 | BENAR |
| 2 | 1, 2, 1 | Diskriminan = 0.00<br>Akar kembar: -1.00 | Diskriminan = 0.00<br>Akar kembar: -1.00 | BENAR |
| 3 | 1, 0, 1 | Diskriminan = -4.00<br>Tidak ada akar real | Diskriminan = -4.00<br>Tidak ada akar real | BENAR |
| 4 | 0, 2, 3 | Bukan persamaan kuadrat. | Bukan persamaan kuadrat. | BENAR |

## Refleksi
Salah satu kesalahan logika yang umum terjadi saat penulisan rumus perhitungan akar adalah lupa menambahkan tanda kurung pada pembagi `(2 * a)`. Jika ditulis `-b + D**0.5 / 2 * a`, Python akan melakukan pembagian terlebih dahulu sebelum perkalian, sehingga hasilnya menjadi tidak akurat. 

Cara memperbaikinya adalah dengan membungkus seluruh bagian penyebut menggunakan tanda kurung `(2 * a)` agar proses perkalian dilakukan sebelum pembagian.
