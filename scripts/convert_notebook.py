import sys
import subprocess
from pathlib import Path
import shutil


def convert_notebook(notebook_path):
    notebook_path = Path(notebook_path)
    command = ["jupyter", "nbconvert", str(notebook_path), "--to", "markdown"]

    notebook_name = notebook_path.stem
    source_folder = notebook_path.parent / f"{notebook_name}_files"
    if source_folder.exists():
        shutil.rmtree(source_folder)
        print(f"Removed existing {source_folder}")

    subprocess.run(command, check=True)
    print(f"Successfully converted {notebook_path} to Markdown.")

    markdown_file = notebook_path.with_suffix(".md")
    if markdown_file.exists():
        content = markdown_file.read_text()

        # Get the relative path of the notebook
        relative_path = notebook_path.relative_to(Path("content"))
        prefix = str(relative_path.parent)

        # Replace image references
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if "![png](" in line:
                parts = line.split("(")
                if len(parts) > 1:
                    image_path = parts[1].split(")")[0]
                    new_path = f"/{prefix}/{image_path}"
                    lines[i] = f"{parts[0]}({new_path})"

        # Write the updated content back to the file
        markdown_file.write_text("\n".join(lines))
        print(f"Updated image references in {markdown_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_notebook.py <path_to_notebook>")
        sys.exit(1)

    notebook_path = sys.argv[1]
    convert_notebook(notebook_path)
