# INPUT: Meminta input nilai akhir dan persentase kehadiran
nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

# PROSES KEPUTUSAN: Memeriksa apakah nilai >= 60 DAN kehadiran >= 80
if nilai >= 60 and kehadiran >= 80:
    # OUTPUT: Jika kedua syarat terpenuhi
    print("Lulus")
else:
    # OUTPUT: Jika salah satu atau kedua syarat tidak terpenuhi
    print("Belum lulus")