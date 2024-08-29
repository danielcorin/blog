---
title: "Cogno (2024)"
date: 2024-08-27
draft: false
tags:
- railway
- embeddings
- python
- fasthtml

project_url: https://cogno.up.railway.app/
---

Cogno is a daily word game that is a flip on the word game [Semantle](https://semantle.com/).
You are given a starting word and your goal is to guess as many of the top 50 words and are semantically similar to the word as possible, based on the similarity score from the `GoogleNews-vectors-negative300` dataset.
These values are precalculated and stored in sqlite.
The project is hosted on [Railway](https://railway.app/) and build with Python and [FastHTML](https://fastht.ml).
The app stores state client side.

![screenshot](/img/projects/cogno.png)
