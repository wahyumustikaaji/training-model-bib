import cv2
import os
from ultralytics import YOLO
import easyocr

# Path ke model dan folder
model_path = r"D:\IPB\SEMESTER 6\Viskom\bib detection project\runs\detect\train\weights\best.pt"
image_folder = r"D:\IPB\SEMESTER 6\Viskom\bib detection project\test\images"
output_full_folder = r"D:\IPB\SEMESTER 6\Viskom\bib detection project\output_full_images"

# Buat folder output
os.makedirs(output_full_folder, exist_ok=True)

# Load model deteksi & OCR
model = YOLO(model_path)
reader = easyocr.Reader(['en'])

# Loop gambar
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_folder, filename)
        image = cv2.imread(image_path)

        results = model(image_path)[0]

        bib_numbers = []

        for box in results.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            crop = image[y1:y2, x1:x2]

            # OCR untuk mengenali nomor bib
            ocr_result = reader.readtext(crop, detail=0)
            bib_numbers.extend(ocr_result)

        # Gunakan hasil OCR untuk penamaan file
        bib_text = "_".join(bib_numbers) if bib_numbers else "unknown"
        output_path = os.path.join(output_full_folder, f"{filename[:-4]}_bib_{bib_text}.jpg")

        # Simpan gambar utuh
        cv2.imwrite(output_path, image)
        print(f"[✓] Gambar utuh disimpan dengan nama bib: {output_path}")
