import os
import pytesseract
from PIL import Image
import pandas as pd

# Extract text from (reddit) images in specified folder to a csv file with columns: imageName, text

# use tesseract ocr to extract text.
# If Tesseract is not in PATH, set it manually like:
# pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"
# (Windows example: r"C:\Program Files\Tesseract-OCR\tesseract.exe")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# === USAGE ===
folder = "./memes4"
output_csv = "./qualtrics/reddit_memes/memes4.csv"

def extract_text_to_csv(folder_path, output_csv):
    data = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            
            try:
                img = Image.open(img_path)
                text = pytesseract.image_to_string(img)

                # Clean text (optional but useful)
                text = text.strip().replace('\n', ' ')

                data.append({
                    "imageName": filename,
                    "text": text
                })

                print(f"Processed: {filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)
    print(f"\nSaved CSV to: {output_csv}")


extract_text_to_csv(folder, output_csv)