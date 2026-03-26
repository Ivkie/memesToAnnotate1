import os
import easyocr
import pandas as pd
from PIL import Image
import csv

# === CONFIG ===
folder = "./memes6"
output_csv = "./qualtrics/reddit_memes/memes6.csv"

# Initialize EasyOCR (GPU=True if you have CUDA)
reader = easyocr.Reader(['en'], gpu=False)


def extract_text_to_csv(folder_path, output_csv):
    data = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)

            try:
                # Run OCR
                results = reader.readtext(img_path, detail=0)

                # Join detected text
                text = " ".join(results)

                # Clean text
                text = text.strip().replace('\n', ' ')

                data.append({
                    "imageName": filename,
                    "text": text
                })

                print(f"Processed: {filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    df = pd.DataFrame(data)

    # Safer CSV (important for OCR text)
    df.to_csv(output_csv, index=False, quoting=csv.QUOTE_ALL)

    print(f"\nSaved CSV to: {output_csv}")


extract_text_to_csv(folder, output_csv)