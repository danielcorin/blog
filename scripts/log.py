import datetime
import os
import sys
import pytz
import subprocess
from datetime import timezone

from post_frontmatter import generate

utc_dt = datetime.datetime.now(timezone.utc)

tz = pytz.timezone("US/Eastern")
now = utc_dt.astimezone(tz)
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
formatted_title = now.strftime("%Y-%m-%d")

directory = f"content/logs/{year}/{month}"
os.makedirs(directory, exist_ok=True)

file_path = f"{directory}/{day}.md"

file_content = generate(formatted_title)

if os.path.isfile(file_path):
    print(f"File already exists at {file_path}")
    subprocess.call(['cursor', file_path])
    sys.exit(0)

# Create the file
with open(file_path, "w") as file:
    file.write(file_content)

print(f"File created successfully at {file_path}")
subprocess.call(['cursor', file_path])