import pandas as pd
import os
from datetime import datetime

# Load JSON file
date_str = datetime.now().strftime("%Y%m%d")
file_path = f"data/trends_{date_str}.json"

df = pd.read_json(file_path)

# Print initial rows count
print("Rows before cleaning:", len(df))


# 1. REMOVE DUPLICATES (based on post_id)
df = df.drop_duplicates(subset="post_id")


# 2. HANDLE MISSING VALUES
df = df.dropna(subset=["post_id", "title", "score"])


# 3. FIX DATA TYPES
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

#4.REMOVE STORIES LESS THAN 5
df=df[df["score"]>=5]

# Drop rows if conversion failed
df = df.dropna(subset=["score", "num_comments"])

# Convert to integer
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# 4. REMOVE LOW QUALITY STORIES (score < 5)
df = df[df["score"] >= 5]


# 5. CLEAN WHITESPACE (title column)
df["title"] = df["title"].str.strip()


# Final row count
print("Rows after cleaning:", len(df))


#Save as CSV (6 marks)
os.makedirs("data", exist_ok=True)
output_file = f"data/cleaned_trends_{date_str}.csv"
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")



#FINAL REPORT
# Initial load
print(f"Loaded {len(df)} stories from {file_path}")

# Remove duplicates
print("After removing duplicates:", len(df))

# Remove nulls
print("After removing nulls:", len(df))

# Convert types
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")
df = df.dropna(subset=["score", "num_comments"])

# Remove low scores
print("After removing low scores:", len(df))

#TOTAL EACH CAT COUNT
print("\nStories per category:")
print(df["category"].value_counts())