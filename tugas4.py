# 1 List – akses & manipulasi
dataList = [10, "Python", 3.14, "AI", True, 2025]  # campuran string, angka, float, boolean

print("=== List ===")
print("List awal:", dataList)
print("Elemen pertama:" , dataList[0:1])
print("Elemen terakhir:" , dataList[5:6])

dataList.append("Baru")
print("Setelah append:" , dataList)

dataList.insert(2, "Disisipkan")
print("Setelah insert:" , dataList)

dataList.extend(["ini", "adalah", "Extend"])
print("Setelah extend:" , dataList)

dataList.pop(3)
print("Setelah pop index 3:" , dataList)

dataList.remove(2025)
print("Setelah remove 2025:" , dataList)
print()


# 2 Tuple – immutability & unpacking
dataTuple = ("apel", "pisang", "mangga", "jeruk", "melon")

print("=== Tuple ===")
print("Tuple:" , dataTuple)
print("Panjang tuple:" , len(dataTuple))
print("Akses indeks ke-2:" , dataTuple[2])

buah1, buah2, *buahSisa = dataTuple
print("Unpacking:" , buah1, buah2, buahSisa)
print()


# 3 Set – keunikan & operasi himpunan
setA = {1, 3, 9, 6, 5}
setB = {7, 5, 2, 4, 3}

print("=== Set ===")
print("Set A:" , setA)
print("Set B:" , setB)
print("Union:" , setA | setB)
print("Intersection:" , setA & setB)
print("Difference A-B:" , setA - setB)
print("Symmetric Difference:" , setA ^ setB)

setC = {1, 1, 2, 2, 3}
print("Set dengan duplikat otomatis hilang:" , setC)
print()


# 4 Dictionary – key/value dasar
mahasiswa = {
    "nama": "Gatra",
    "nim": "062240722994",
    "angkatan": 2022,
    "kota": "Palembang"
}

print("=== Dictionary ===")
print("Dictionary awal:" , mahasiswa)

mahasiswa["jurusan"] = "Teknik Komputer"
print("Setelah tambah key:" , mahasiswa)

mahasiswa["kota"] = "Jakarta"
print("Setelah ubah nilai key:" , mahasiswa)

del mahasiswa["angkatan"]
print("Setelah hapus key:" , mahasiswa)

print("Keys:" , mahasiswa.keys())
print("Values:" , mahasiswa.values())
print("Items:" , mahasiswa.items())

print("Iterasi dictionary:")
for key, value in mahasiswa.items():
    print(key , ":" , value)
print()


# 5 Nested structures
bukuList = [
    {"judul": "Python Dasar", "penulis": "Andi", "tahun": 2020},
    {"judul": "AI untuk Pemula", "penulis": "Budi", "tahun": 2023},
    {"judul": "Data Science", "penulis": "Cici", "tahun": 2021},
    {"judul": "Machine Learning", "penulis": "Dedi", "tahun": 2022}
]

print("=== Nested Structures ===")
print("Judul semua buku:")
for buku in bukuList:
    print(buku["judul"])

print("Filter buku tahun >= 2022:")
bukuBaru = [b["judul"] for b in bukuList if b["tahun"] >= 2022]
print(bukuBaru)
print()


# 6 Comprehension & utilitas
print("=== Comprehension ===")
angkaList = list(range(1, 21))
genap = [x for x in angkaList if x % 2 == 0]
kuadrat = [x**2 for x in angkaList]

print("List angka genap:" , genap)
print("List kuadrat:" , kuadrat)

statusAngka = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print("Dict comprehension:" , statusAngka)

kalimat = "Ayo Belajar Python"
hurufUnik = {c.lower() for c in kalimat if c.isalpha()}
print("Set comprehension huruf unik:" , hurufUnik)
print()


# 7 Keanggotaan & pencarian sederhana
print("=== Keanggotaan & Pencarian ===")
print("Apakah 'Python' ada di dataList?" , "Python" in dataList)
print("Apakah angka 4 ada di setA?" , 4 in setA)

cariAngka = "AI"
if cariAngka in dataList:
    print(str(cariAngka) + " ditemukan pada index " + str(dataList.index(cariAngka)))
else:
    print(str(cariAngka) + " tidak ditemukan di list")
