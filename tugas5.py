# 1. Functions

def greet(nama: str) -> str:
    return "Halo, " + nama + "!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if len(angka) == 0:
        return 0.0
    else:
        return round(sum(angka) / len(angka), 2)


# 2. Class Student

class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def __str__(self) -> str:
        return "Student(nama='" + self.nama + "', nim='" + self.nim + "', rata=" + str(self.rata_nilai()) + ", status=" + self.status() + ")"


# 3. Demo
if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Gatra Adi Wirya"))
    print("tambah(5, 7) =", tambah(5, 7))
    print("tambah(10) =", tambah(10))
    print("rata_rata([80, 90, 100]) =", rata_rata([80, 90, 100]))
    print("rata_rata([]) =", rata_rata([]))
    print()

    print("=== CLASS STUDENT ===")
    mhs1 = Student("Gatra", "06224072")
    mhs1.tambah_nilai(82)
    mhs1.tambah_nilai(86)
    mhs1.tambah_nilai(95)

    mhs2 = Student("Budi", "06224073")
    mhs2.tambah_nilai(66)
    mhs2.tambah_nilai(55)
    mhs2.tambah_nilai(80)

    print(mhs1)
    print("Rata-rata:", mhs1.rata_nilai())
    print("Status:", mhs1.status())
    print()

    print(mhs2)
    print("Rata-rata:", mhs2.rata_nilai())
    print("Status:", mhs2.status())
