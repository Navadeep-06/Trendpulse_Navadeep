# MAKE THE API CALLS (8 MARKS)
import requests
import time
import os
import json
from datetime import datetime

headers = {"User-Agent": "TrendPulse/1.0"}

# Categories (5 categories → 25 each = 125 stories)
categories = {
    "top": "https://hacker-news.firebaseio.com/v0/topstories.json",
    "new": "https://hacker-news.firebaseio.com/v0/newstories.json",
    "best": "https://hacker-news.firebaseio.com/v0/beststories.json",
    "ask": "https://hacker-news.firebaseio.com/v0/askstories.json",
    "show": "https://hacker-news.firebaseio.com/v0/showstories.json"
}

all_stories = []

# Loop through each category
for cat_name, url in categories.items():
    print(f"\nFetching {cat_name} stories...")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch {cat_name}")
        continue

    story_ids = response.json()

    # Take 25 stories per category
    for story_id in story_ids[:25]:
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        item_response = requests.get(item_url, headers=headers)

        if item_response.status_code != 200:
            print("Failed to fetch story")
            continue

        data = item_response.json()

        if not data:  # skip if None
            continue

        title = data.get("title", "").lower()

        # CATEGORY LOGIC (based on keywords)
        if "ai" in title or "machine learning" in title:
            category = "AI"
        elif "startup" in title:
            category = "Startup"
        elif "python" in title or "code" in title:
            category = "Programming"
        elif "data" in title:
            category = "Data"
        else:
            category = "Other"

        # EXTRACT FIELDS
        story = {
            "post_id": data.get("id"),
            "title": data.get("title"),
            "category": category,
            "score": data.get("score"),
            "num_comments": data.get("descendants"),
            "author": data.get("by"),
            "collected_at": datetime.now().isoformat()
        }

        all_stories.append(story)

    # WAIT 2 seconds per category (IMPORTANT)
    time.sleep(2)


# SAVE TO JSON FILE (5 MARKS)

os.makedirs("data", exist_ok=True)

date_str = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{date_str}.json"

with open(filename, "w") as f:
    json.dump(all_stories, f, indent=4)

# FINAL OUTPUT
print(f"\nCollected {len(all_stories)} stories. Saved to {filename}")