import frontmatter
from pathlib import Path


def get_tags_from_frontmatter(file_path):
    with open(file_path, "r") as file:
        post = frontmatter.load(file)
        return post.get("tags", []) or []


def list_unique_tags():
    content_dir = Path("content")
    all_tags = set()

    for markdown_file in content_dir.rglob("*.md"):
        tags = get_tags_from_frontmatter(markdown_file)
        all_tags.update(tags)

    return sorted(list(all_tags))


if __name__ == "__main__":
    unique_tags = list_unique_tags()
    for tag in unique_tags:
        print(tag)
