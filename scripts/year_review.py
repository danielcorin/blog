from pathlib import Path
import datetime
from frontmatter import load


def get_post_stats(md_file):
    with md_file.open() as f:
        post = load(f)
        return {
            "title": post.metadata.get("title", "Untitled"),
            "date": post.metadata["date"],
            "file": md_file,
            "word_count": len(post.content.split()),
        }


def is_current_year_post(post_date, year):
    return f"{year}-" in str(post_date)


def get_posts_for_year(year):
    content_dir = Path("content")
    posts_by_category = {}

    for md_file in content_dir.rglob("*.md"):
        relative_path = md_file.relative_to(content_dir)
        category = relative_path.parts[0] if relative_path.parts else "uncategorized"

        try:
            post_stats = get_post_stats(md_file)
            if not is_current_year_post(post_stats["date"], year):
                continue

            if category not in posts_by_category:
                posts_by_category[category] = []
            posts_by_category[category].append(post_stats)

        except (ValueError, AttributeError, KeyError):
            continue

    return posts_by_category


def get_category_stats(category_posts):
    post_count = len(category_posts)
    word_count = sum(post["word_count"] for post in category_posts)
    return post_count, word_count


def generate_year_review(year=None):
    if year is None:
        year = datetime.datetime.now().year

    posts = get_posts_for_year(year)

    output = f"# Year in Review: {year}\n\n"
    total_posts = 0
    total_words = 0

    output += "| Category | Posts | Words |\n"
    output += "|----------|-------|-------|\n"

    for category, category_posts in posts.items():
        post_count, word_count = get_category_stats(category_posts)
        total_posts += post_count
        total_words += word_count
        output += f"| {category.title()} | {post_count} | {word_count} |\n"

    output += f"| **Total** | **{total_posts}** | **{total_words}** |\n"

    out_path = f"content/posts/{year}-year-in-review.md"
    output_file = Path(out_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    generate_year_review()
