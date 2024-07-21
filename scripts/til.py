import os
import sys
import argparse

from post_frontmatter import generate

parser = argparse.ArgumentParser(description="Create TIL post.")
parser.add_argument("path", type=str, help="the path to the file to create")
args = parser.parse_args()

path = args.path.replace(".md", "")
# Make the file name human readable with sensible capitalization
path_parts = path.split("/")
formatted_title = " ".join(
    [part.capitalize().replace("-", " ") for part in path_parts[-1].split("-")]
)
file_path = f"content/til/{path}.md"
directory = os.path.dirname(file_path)
os.makedirs(directory, exist_ok=True)


file_content = generate(formatted_title)

if os.path.isfile(file_path):
    print(f"File already exists at {file_path}")
    sys.exit(1)

# Create the file
with open(file_path, "w") as file:
    file.write(file_content)

print(f"File created successfully at {file_path}")
