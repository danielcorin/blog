---
title: "Cogno (2024)"
date: 2024-08-27
draft: false
tags:
- railway
- embeddings
- python
- fasthtml

project_url: https://www.cogno.fun
---

On 2024-08-08, I wrote this note

> Given a word, propose words that are as lexically similar as possible. Either try and find the closest word or get points for top N closest words.

Cogno is a daily word game that is a flip on the word game [Semantle](https://semantle.com/).
You are given a starting word and your goal is to guess as many of the top 50 words and are semantically similar to the word as possible, based on the similarity score from the [`GoogleNews-vectors-negative300`](https://code.google.com/archive/p/word2vec/) and [FastText](https://fasttext.cc/docs/en/english-vectors.html) datasets.
These values are precalculated and stored in a SQLite database.
The project is hosted on [Railway](https://railway.app/) and build with Python and [FastHTML](https://fastht.ml).
The app stores state client side.

Tech: Python, [FastHTML](https://fastht.ml/), [Railway](https://railway.app/)

![screenshot](/img/projects/cogno.png)
