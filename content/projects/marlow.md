---
title: "Marlow (2023)"
date: 2023-03-20
draft: false
tags:
- react
- nextjs
- vercel
---

I built a [site](https://marlow-ai.vercel.app/) that you can use to manage a list of books you’ve read and your ratings for them.
From this reading history, you can use a language model backed approach to generate book recommendations based on your ratings and a small summary justifying the recommendation in the context of your reading history.
It was a hard concept to validate, since it takes a while to read a book and determine if it was a good recommendation.
I didn't come up with a mechanism to reinforce good or bad recommendations once you’ve read a book and have feedback.
I experimented with several different prompt engineering approaches to increase the quality and variety of the recommendations.
Because I was relying on a language model, there was a cutoff date in my knowledge of books.
I learned a lot about prompt engineering from this project and a good bit more about React as well.

tech: React, Next.js, Vercel

![screenshot](/images/projects/marlow.png)
