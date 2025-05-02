import json
import os

# Path ke file JSON dan folder gambar
output_json_path = r"D:\IPB\SEMESTER 6\Viskom\bib detection project\data\data_bib.json"
folder_gambar = r"D:\IPB\SEMESTER 6\Viskom\bib detection project\output_full_images"

# Baca data JSON
with open(output_json_path, "r") as f:
    data = json.load(f)

# Fungsi pencarian
def cari_gambar_bib(bib_number: str, data_json):
    return [item["image_path"] for item in data_json if bib_number in item["bib_number"]]

# Input dari user
nomor_bib_input = input("Masukkan nomor BIB yang ingin dicari: ").strip()
hasil = cari_gambar_bib(nomor_bib_input, data)

# Tampilkan hasil
if hasil:
    print(f"[✓] Ditemukan {len(hasil)} gambar untuk bib {nomor_bib_input}:")
    for path in hasil:
        print(" -", path)
        full_path = os.path.join(folder_gambar, os.path.basename(path))  # Gabungkan path folder dengan nama file

        if os.path.exists(full_path):
            print(f"[✓] Membuka gambar: {full_path}")
            os.startfile(full_path)  # Buka gambar dengan aplikasi default (Photos, dll)
        else:
            print(f"[!] Gambar tidak ditemukan: {full_path}")
else:
    print(f"[✗] Tidak ditemukan gambar untuk bib {nomor_bib_input}.")
