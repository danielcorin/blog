import datetime
import pytz
from datetime import timezone


def generate(title, tags=[]):
    tags = list(set(tags))
    tags_str = ""
    if tags:
        tags_str += "\n"
        tags_str += "\n".join([f"- {tag}" for tag in tags])
    utc_dt = datetime.datetime.now(timezone.utc)
    tz = pytz.timezone("US/Eastern")
    now = utc_dt.astimezone(tz)
    formatted_date = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    return f"""---
date: "{formatted_date}"
title: "{title}"
draft: false
tags:{tags_str}
---
"""
