from pathlib import Path
import datetime
import re
import html
from macnotesapp import NotesApp
from post_frontmatter import generate


class Note:
    def __init__(self, content, creation_date, modification_date):
        self.content = content
        self.creation_date = creation_date
        self.modification_date = modification_date
        self.tags = self._extract_tags()
        print(f"Created note with creation date: {creation_date}, tags: {self.tags}")

    def _extract_tags(self):
        """Extract tags prefixed with @ from the note content."""
        tags = []
        if self.content:
            # Find all words starting with @ in the content
            tags = re.findall(r"@\w+", self.content)
            print(f"Extracted tags: {tags}")
        return tags

    def clean_content(self):
        # Remove HTML tags
        cleaned = re.sub(r"<[^>]+>", "", self.content)

        # Replace HTML entities
        cleaned = html.unescape(cleaned)

        # Remove extra whitespace
        cleaned = re.sub(r"\n\s*\n", "\n\n", cleaned)
        cleaned = cleaned.strip()

        print(f"Cleaned content (first 50 chars): {cleaned[:50]}...")
        return cleaned

    def format_content(self):
        """Format the note content based on its tags."""
        print(f"Formatting content based on tags: {self.tags}")
        if "@quote" in self.tags:
            print("Formatting as quote")
            return format_quote(self.content)
        elif "@log" in self.tags:
            print("Formatting as log")
            return format_log(self.content)
        else:
            print("No special formatting applied")
            return self.clean_content()

    def __repr__(self):
        return f"Note(creation_date={self.creation_date}, tags={self.tags})"


def format_quote(content):
    print("Starting quote formatting")
    content = content.replace("“", '"').replace("”", '"')

    """Format a quote note with proper markdown blockquote formatting."""
    # Clean HTML tags and entities
    cleaned = re.sub(r"<[^>]+>", "", content)
    cleaned = html.unescape(cleaned)

    # Remove @quote tag from content
    cleaned = cleaned.replace("@quote", "").strip()

    # Extract the quote, source, date, and URL using regex
    quote_pattern = r'"(.*?)"'
    source_pattern = r"From (.*?)(?:,|\n|$)"
    date_pattern = r"(?:From .*?)?(?:,\s*)?((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})"
    url_pattern = r"(https?://\S+)"

    quote_match = re.search(quote_pattern, cleaned, re.DOTALL)
    source_match = re.search(source_pattern, cleaned)
    date_match = re.search(date_pattern, cleaned)
    url_match = re.search(url_pattern, cleaned)
    import pdb

    pdb.set_trace()

    print(
        f"Quote match: {bool(quote_match)}, Source match: {bool(source_match)}, Date match: {bool(date_match)}, URL match: {bool(url_match)}"
    )

    formatted = ""

    if quote_match:
        quote_text = quote_match.group(1).strip()
        # Format as blockquote
        formatted = "> " + quote_text.replace("\n", "\n> ")

        # Add attribution
        attribution = []
        if source_match:
            attribution.append(source_match.group(1))
        if date_match:
            attribution.append(date_match.group(1))

        if attribution:
            formatted += f"\n>\n> — {', '.join(attribution)}"

        # Add link if available
        if url_match:
            url = url_match.group(1)
            formatted += f"\n\n[Source]({url})"

    print(f"Formatted quote (first 50 chars): {formatted[:50]}...")
    return formatted


def format_log(content):
    """Format a log note as plain text."""
    print("Starting log formatting")
    # Simply clean the content without additional formatting
    cleaned = re.sub(r"<[^>]+>", "", content)
    cleaned = html.unescape(cleaned)

    # Remove @log tag from content
    cleaned = re.sub(r"@log\b", "", cleaned)

    cleaned = re.sub(r"\n\s*\n", "\n\n", cleaned)
    print(f"Formatted log (first 50 chars): {cleaned[:50]}...")
    return cleaned.strip()


def format_notes_for_day(notes, day_date):
    """
    Create a string of all notes for a specific day with triple dashes separating them.

    Args:
        notes: List of Note objects
        day_date: datetime object representing the day to filter notes for

    Returns:
        String with all notes content separated by triple dashes
    """
    print(f"Formatting notes for day: {day_date}")
    # Filter notes for the specific day
    start_of_day = day_date.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = day_date.replace(hour=23, minute=59, second=59, microsecond=999999)

    day_notes = [
        note for note in notes if start_of_day <= note.creation_date <= end_of_day
    ]

    print(f"Found {len(day_notes)} notes for {day_date}")

    # Sort notes by creation date
    day_notes.sort(key=lambda note: note.creation_date)

    # Join note contents with triple dashes
    if not day_notes:
        print("No notes found for this day")
        return ""

    formatted_content = "\n\n---\n\n".join(
        note.format_content() for note in day_notes if note.content
    )
    print(f"Formatted content length: {len(formatted_content)} characters")
    return formatted_content


def find_latest_log_date():
    """Find the most recent log file and return its date."""
    print("Finding latest log date")
    log_dir = Path("content/logs")
    log_files = list(log_dir.glob("**/*.md"))
    latest_log = None
    latest_date = datetime.datetime.min

    print(f"Found {len(log_files)} log files")

    for log_file in log_files:
        # Extract date from path (yyyy/mm/dd.md)
        match = re.search(r"(\d{4})/(\d{2})/(\d{2})\.md$", str(log_file))
        if match:
            year, month, day = map(int, match.groups())
            file_date = datetime.datetime(year, month, day)
            if file_date > latest_date:
                latest_date = file_date
                latest_log = log_file
                print(f"New latest date: {latest_date}, file: {latest_log}")

    print(f"Latest log file: {latest_log}, date: {latest_date}")
    return latest_log, latest_date


def get_recent_notes(noteslist, latest_date):
    """Get notes created after the latest log date."""
    print(f"Getting notes after {latest_date}")
    # Add time component to make it end of day
    latest_date = latest_date.replace(hour=23, minute=59, second=59)

    recent_notes = [
        Note(
            content=note,
            creation_date=creation_date,
            modification_date=modification_date,
        )
        for note, creation_date, modification_date in zip(
            noteslist.body, noteslist.creation_date, noteslist.modification_date
        )
        if creation_date > latest_date
    ]

    print(f"Found {len(recent_notes)} recent notes")
    return recent_notes


def group_notes_by_date(notes):
    """Group notes by their creation date."""
    print("Grouping notes by date")
    notes_by_date = {}
    for note in notes:
        date = note.creation_date.date()
        if date not in notes_by_date:
            notes_by_date[date] = []
        notes_by_date[date].append(note)

    print(f"Notes grouped into {len(notes_by_date)} dates")
    for date, date_notes in notes_by_date.items():
        print(f"Date {date}: {len(date_notes)} notes")

    return notes_by_date


def create_log_files(notes_by_date):
    """Create log files for each date with notes."""
    print(f"Creating log files for {len(notes_by_date)} dates")
    for date, notes in notes_by_date.items():
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")

        # Create directory if it doesn't exist
        log_path = Path(f"content/logs/{year}/{month}")
        log_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {log_path}")

        # Format the title as YYYY-MM-DD
        formatted_title = date.strftime("%Y-%m-%d")

        # Extract all tags from notes for this day
        all_tags = []
        for note in notes:
            all_tags.extend([tag[1:] for tag in note.tags])  # Remove @ prefix

        print(f"Tags for {formatted_title}: {all_tags}")

        # Generate frontmatter
        frontmatter = generate(formatted_title, all_tags)

        # Format notes content
        content = format_notes_for_day(
            notes, datetime.datetime.combine(date, datetime.time.min)
        )

        # Write to file
        file_path = log_path / f"{day}.md"
        with open(file_path, "w") as f:
            f.write(frontmatter + "\n" + content)

        print(f"Created log file: {file_path}")


def main():
    print("Starting Apple Notes parsing")
    # NotesApp() provides interface to Notes.app
    notesapp = NotesApp()
    print("Connected to Notes.app")

    # Get list of notes for one or more specific accounts
    print("Fetching notes with @quotes or @logs tags")
    noteslist = notesapp.noteslist(body=["@quotes", "@logs"])
    print(f"Found {len(noteslist.body)} notes")

    # Find the most recent log file
    latest_log, latest_date = find_latest_log_date()

    # Filter notes created after the latest log date
    if latest_log:
        print(f"Processing notes after {latest_date}")
        recent_notes = get_recent_notes(noteslist, latest_date)
        notes_by_date = group_notes_by_date(recent_notes)
        create_log_files(notes_by_date)
    else:
        print("No existing log files found")


if __name__ == "__main__":
    main()
