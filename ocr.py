import pytesseract
import cv2
import os

# Path ke executable Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\ACER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

crop_folder = r"D:\IPB\SEMESTER 6\Viskom\bib detection project\crops"
ocr_results = {}

for filename in os.listdir(crop_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        path = os.path.join(crop_folder, filename)
        image = cv2.imread(path)

        # === Preprocessing OCR ===
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Threshold
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Morphological ops - dilate to merge characters
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        dilated = cv2.dilate(thresh, kernel, iterations=1)

        # Config Tesseract
        config = r'--psm 7 -c tessedit_char_whitelist=0123456789'

        # OCR
        text = pytesseract.image_to_string(dilated, config=config)
        nomor = ''.join(filter(str.isdigit, text))

        if nomor:
            ocr_results[nomor] = path
            print(f"[OCR] {filename} → {nomor}")
        else:
            print(f"[!] Tidak terbaca: {filename}")

# Simpan hasil ke file
with open("ocr_results.txt", "w") as f:
    for nomor, path in ocr_results.items():
        f.write(f"{nomor}:{path}\n")
