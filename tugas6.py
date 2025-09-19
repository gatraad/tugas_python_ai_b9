# 1 Import & Setup
import numpy as np
import pandas as pd

np.random.seed(42)

# 2 NumPy – Data & Statistik
print("=== NUMPY ===")
nilai_ujian = np.random.randint(50, 100, size=10) 
print("Array nilai ujian:", nilai_ujian)

rata = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

print("Rata-rata:", rata)
print("Median:", median)
print("Standar deviasi:", std)
print("Nilai minimum:", nilai_min)
print("Nilai maksimum:", nilai_max)
print()

# 3 pandas – DataFrame
print("=== PANDAS ===")
data = {
    "nama": ["Budi", "Siti", "Andi", "Citra", "Dewi"],
    "nim": ["A001", "A002", "A003", "A004", "A005"],
    "nilai": nilai_ujian[:5]
}

df = pd.DataFrame(data)
df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

print(df.head())
print()

# 4 File I/O – Tulis Ringkasan ke .txt
ringkasan = []
ringkasan.append("=== RINGKASAN STATISTIK ===")
ringkasan.append("Rata-rata: " + str(rata))
ringkasan.append("Median: " + str(median))
ringkasan.append("Standar deviasi: " + str(std))
ringkasan.append("Nilai minimum: " + str(nilai_min))
ringkasan.append("Nilai maksimum: " + str(nilai_max))
ringkasan.append("")
ringkasan.append("=== RINGKASAN DATAFRAME ===")
ringkasan.append("Jumlah baris: " + str(len(df)))
ringkasan.append("Jumlah LULUS: " + str(len(df[df['status'] == 'LULUS'])))
ringkasan.append("Jumlah TIDAK LULUS: " + str(len(df[df['status'] == 'TIDAK LULUS'])))
ringkasan.append("")

with open("ringkasan_tugas6.txt", "w") as f:
    f.write("\n".join(ringkasan))

# 5 OOP Sederhana – Class GradeBook
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return round(self.df["nilai"].mean(), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        total = len(self.df)
        if total == 0:
            return 0.0
        lulus = len(self.df[self.df["nilai"] >= threshold])
        return round((lulus / total) * 100, 2)

    def save_summary(self, path: str):
        lines = []
        lines.append("=== GRADEBOOK SUMMARY ===")
        lines.append("Jumlah data: " + str(len(self.df)))
        lines.append("Rata-rata nilai: " + str(self.average()))
        lines.append("Persentase lulus: " + str(self.pass_rate()) + "%")
        lines.append("")
        with open(path, "a") as f:
            f.write("\n".join(lines))

    def __str__(self) -> str:
        return "GradeBook(jumlah data=" + str(len(self.df)) + ", rata-rata=" + str(self.average()) + ")"

# 6 Demo
if __name__ == "__main__":
    print("=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print("Average nilai:", gb.average())
    print("Pass rate:", gb.pass_rate(), "%")
    gb.save_summary("ringkasan_tugas6.txt")
