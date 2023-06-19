import datetime
import os
import sys

# Get current date and time
now = datetime.datetime.utcnow()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
formatted_date = now.strftime("%Y-%m-%dT%H:%M:%SZ")
formatted_title = now.strftime("%Y-%m-%d")

directory = f"content/logs/{year}/{month}"
os.makedirs(directory, exist_ok=True)

file_path = f"{directory}/{day}.md"

file_content = f"""---
date: "{formatted_date}"
title: "{formatted_title}"
draft: true
tags:
---

"""

if os.path.isfile(file_path):
    print(f"File already exists at {file_path}")
    sys.exit(1)

# Create the file
with open(file_path, "w") as file:
    file.write(file_content)

print(f"File created successfully at {file_path}")
