import glob
import os
import frontmatter

# Get all markdown files with the year in the name
markdown_files = glob.glob("content/posts/**/*[0-9][0-9][0-9][0-9]*.md", recursive=True)

# Iterate over each markdown file
for file_path in markdown_files:
    with open(file_path, "r+") as file:
        content = file.read()

        # Read the frontmatter of the file
        fm = frontmatter.load(file_path)

        # Get the filename excluding the .md extension
        filename = os.path.splitext(os.path.basename(file_path))[0]

        # Check if the alias exists in the frontmatter
        if "aliases" not in fm or f"/posts/{filename}" not in fm["aliases"]:
            if "aliases" not in fm:
                fm["aliases"] = []
            fm["aliases"].append(f"/posts/{filename}")

        # Update the file with the modified frontmatter
        file.seek(0)
        file.write(frontmatter.dumps(fm))
        file.truncate()
        
