import json
import os

output_data = []
output_json_path = r"D:\IPB\SEMESTER 6\Viskom\bib detection project\data\data_bib.json"
folder_output = r"D:\IPB\SEMESTER 6\Viskom\bib detection project\output_full_images"

# Loop semua file hasil
for filename in os.listdir(folder_output):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        # Coba ekstrak nomor bib dari nama file
        parts = filename.split("_bib_")
        if len(parts) == 2:
            bibs_raw = parts[1].split(".")[0]
            bib_numbers = bibs_raw.split("_")

            data_entry = {
                "bib_number": bib_numbers,
                "image_path": f"/images/{filename}"  # bisa diubah ke sesuai path di server
            }
            output_data.append(data_entry)

# Simpan ke file JSON
with open(output_json_path, 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"[✓] Data JSON disimpan di: {output_json_path}")
