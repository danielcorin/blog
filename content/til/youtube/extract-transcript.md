---
date: "2024-05-11T13:59:05Z"
title: "Extract Youtube Video Transcript"
draft: false
tags:
- yt-dlp
---

You can download a Youtube video transcript with
[`yt-dlp`](https://github.com/yt-dlp/yt-dlp).

```sh
yt-dlp --write-auto-sub --skip-download --sub-format vtt --output transcript "<video_url>"
```

This will output a file called `transcript.en.vtt`. That file can be cleaned
like this, to remove all formatting and metadata except the transcript text.

```sh
cat transcript.en.vtt | grep : -v | awk '!seen[$0]++'
```

This approach is useful for simple way to pipe the contents of a Youtube video
into an LLM, my motivation for finding a way to accomplish this task.

Here is a script that pulls the transcript of a video then summarizes it using
[`llm`](https://github.com/simonw/llm).

```sh
#!/bin/zsh

if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Please provide a YouTube URL as an argument."
    exit 1
fi
yt-dlp --write-auto-sub --skip-download --sub-format vtt --output transcript "$1" >/dev/null 2>&1
cat transcript.en.vtt | grep : -v | awk '!seen[$0]++' | llm "write a short summary of the contents of this youtube video transcript"
rm transcript.en.vtt
```
