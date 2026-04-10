import pandas as pd
import numpy as np
import os
from datetime import datetime


# 1. LOAD DATA

# Create date string
date_str = datetime.now().strftime("%Y%m%d")

# Load cleaned file
file_path = f"data/cleaned_trends_{date_str}.csv"
df = pd.read_csv(file_path)

print(df.head())

print(f"Loaded data: {df.shape}")

print("\nFirst 5 rows:")
print(df.head())

print("\nAverage score:", int(df["score"].mean()))
print("Average comments:", int(df["num_comments"].mean()))


# 2. NUMPY ANALYSIS

print("\n--- NumPy Stats ---")

scores = df["score"].values

print("Mean score :", int(np.mean(scores)))
print("Median score :", int(np.median(scores)))
print("Std deviation :", int(np.std(scores)))
print("Max score :", int(np.max(scores)))
print("Min score :", int(np.min(scores)))


# 3. CATEGORY ANALYSIS

category_counts = df["category"].value_counts()

top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")


# 4. MOST COMMENTED STORY

top_story = df.loc[df["num_comments"].idxmax()]

print(f'\nMost commented story: "{top_story["title"]}" - {top_story["num_comments"]} comments')


# 5. ADD NEW COLUMNS

# Engagement = comments per score
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Popular if score > average score
avg_score = df["score"].mean()
df["is_popular"] = df["score"] > avg_score


# 6. SAVE FINAL FILE

os.makedirs("data", exist_ok=True)

df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved to data/trends_analysed.csv")