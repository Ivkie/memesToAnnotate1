import csv

input_file = "./qualtrics/reddit_memes/memes4.csv"
output_file = "./qualtrics/reddit_memes/memes4_clean.csv"

cleaned_rows = []

with open(input_file, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        line = line.strip()

        try:
            # Try normal parsing first
            row = next(csv.reader([line]))

        except Exception:
            # Fix broken quotes by forcing structure:
            parts = line.split(",", 1)  # split ONLY on first comma
            if len(parts) < 2:
                print(f"Skipping line {i} (too broken): {line}")
                continue

            row = [parts[0], parts[1]]

        # Ensure exactly 2 columns
        if len(row) > 2:
            row = [row[0], ",".join(row[1:])]

        if len(row) == 2:
            image = row[0].strip('"')   # remove quotes ONLY here
            text = row[1]              # keep text as-is
            cleaned_rows.append([image, text])
        else:
            print(f"Skipping line {i}: {line}")

# Write clean CSV
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # writer.writerow(["imageName", "text"])
    writer.writerows(cleaned_rows)

print("Cleaned CSV saved.")