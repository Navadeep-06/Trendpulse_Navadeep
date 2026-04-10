import pandas as pd
import matplotlib.pyplot as plt
import os

# 1 — SETUP
file_path = "data/cleaned_trends_20260410.csv"  # change if needed
df = pd.read_csv(file_path)
df["is_popular"]=df["score"]>100

# Create outputs folder
os.makedirs("outputs", exist_ok=True)


# 2 — CHART 1: Top 10 Stories

top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles
top10["short_title"] = top10["title"].str[:50]

plt.figure(figsize=(10,6))
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# 3 — CHART 2: Stories per Category

category_counts = df["category"].value_counts()

plt.figure(figsize=(8,5))
category_counts.plot(kind="bar", color=["skyblue","orange","green","red","purple"])

plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()


# 4 — CHART 3: Score vs Comments

plt.figure(figsize=(8,6))

popular = df[df["is_popular"] == True]
non_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], color="green", label="Popular")
plt.scatter(non_popular["score"], non_popular["num_comments"], color="red", label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()


# 5 — DASHBOARD (ALL IN ONE)

fig, axes = plt.subplots(3, 1, figsize=(10,15))

# Chart 1
axes[0].barh(top10["short_title"], top10["score"])
axes[0].set_title("Top 10 Stories by Score")

# Chart 2
category_counts.plot(kind="bar", ax=axes[1])
axes[1].set_title("Stories per Category")

# Chart 3
axes[2].scatter(popular["score"], popular["num_comments"], color="green", label="Popular")
axes[2].scatter(non_popular["score"], non_popular["num_comments"], color="red", label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].legend()

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs/ folder ")