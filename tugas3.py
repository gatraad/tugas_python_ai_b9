# 1 Deklarasi Variabel dan Tipe Data
nama = "Gatra"  # string
umur = 20   # integer
beratBadan = 49.5   # float
mahasiswa = True    # boolean
hobi = ["ngoding", "desain 3d", "main gitar", "gaming", "tidur"]  # list


# 2 Manipulasi String
print("=== Manipulasi String ===")
print("Gabungan string:" + nama + " suka " + hobi[0])

print("Panjang string nama:", len(nama))
print("Nama huruf besar:", nama.upper())
print("Nama huruf kecil:", nama.lower())
print()


# 3 Operasi Matematika
print("=== Operasi Matematika ===")
angka1 = 10
angka2 = 2

print("Penjumlahan:", angka1 + angka2)
print("Pengurangan:", angka1 - angka2)
print("Perkalian:", angka1 * angka2)
print("Pembagian:", angka1 / angka2)
print("Pembagian bulat:", angka1 // angka2)
print("Sisa bagi:", angka1 % angka2)
print()


# 4 List dan Akses Elemen
print("=== Operasi List ===")
print("List hobi:", hobi)
print("Tampilkan elemen tertentu:", hobi[0:1])

hobi.append("traveling")
print("Setelah ditambah:", hobi)

hobi.remove("tidur")
print("Setelah dihapus:", hobi)
print()


# 5 Input dari User
print("=== Input dari User ===")
user_nama = input("Masukkan nama Anda: ")
user_umur = int(input("Masukkan umur Anda: "))

print("Halo, nama saya", user_nama, "dan umur saya", user_umur, "tahun.")
