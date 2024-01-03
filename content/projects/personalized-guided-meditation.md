---
title: Personalized Guided Meditation (2023, unpublished)
date: 2023-11-18
draft: false
tags:
- python
- telegram
- openai
- render
---

I've experimented on and off with guided meditations to practice mindfulness.
One area that was a challenge for me in this practice was that the script was often not quite relevant to what I was experiencing or didn't really resonate with me.
Using a language model and text to speech model, I built a Telegram bot that would take a prompt message and use that message as the topic to generate a personalized guided meditation.
I generated the script with a language model, then created the audio track with a Python app and text to speech API to return the full meditation as an audio track in a response message from the bot.
I learned a lot about using the Python event loop doing this project.

Tech: Python, [Telegram](https://telegram.org/), OpenAI, [Render](https://render.com/)

![screenshot](/images/projects/personalized-guided-meditation.png)
