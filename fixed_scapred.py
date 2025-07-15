import pandas as pd

# Step 1: Load with loose parsing
df = pd.read_csv("scraped.csv", dtype=str, engine="python", on_bad_lines='skip')

# Step 2: Detect the actual text columns that belong to pitch
df["pitch"] = df[df.columns[7:]].astype(str).agg(' '.join, axis=1)

# Step 3: Keep only expected columns
df = df[["title", "location", "revenue", "cashflow", "link", "description", "pitch"]]

# Step 4: Clean pitch text
df["pitch"] = df["pitch"].str.replace(r'content="?', '', regex=True).str.strip('"')

# Step 5: Save clean file
df.to_csv("scraped_clean.csv", index=False, quoting=1)  # quoting=1 = QUOTE_ALL
print("✅ Saved cleaned CSV as scraped_clean.csv")
