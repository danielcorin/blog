---
title: "Rowing Vue (2018, deprecated)"
date: 2018-12-05
draft: false
tags:
- vue
- python
- mysql
- flask
- scrapy
- docker
---

I created a project to scrape https://log.concept2.com rowing data and store in a database.
From this, I built a leaderboard site to show rowing activity for several athletes for the month and a summary page to display personal bests across common distances and times (for example, 2,000 meters, or 60 minutes).
A cron triggered the scraper to pull new changes daily.

Tech: Python, [Vue](https://vuejs.org/), MySQL, Flask [Scrapy](https://scrapy.org/), Docker
