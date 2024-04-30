---
title: "Write Partner (2023)"
date: 2023-12-09
draft: false
tags:
- react
- nextjs
- openai
- vercel
github_url: https://github.com/danielcorin/write-partner/
project_url: https://write-partner.vercel.app/
---

I've found language models can be effective thought partners to help you deepen your ideas by generating questions that make you think and reflect.
While I'd seen many projects attempt to use language models to remove the human from the loop in content generation, in this [project](https://write-partner.vercel.app/) I'm using a language model to prompt the user to communicate the content in a conversational way.
You chat with a language model and present your ideas.
The language model asks follow-up questions with the aim of deepening your idea.
The prompt does not instruct the model to fill in gaps, but rather to find out more about what you mean and playback what you've said to clarify ambiguities.
In addition to this chat, another language model separately analyzes the conversation log and is instructed to augment and edit a document based on the new ideas you articulate in the chat.
It proposes these edits in a shared editor, akin to collaborating with someone in a google doc.
The user can accept or pass on these edits or make their own.
The result is a document, written in the users tone that captures the ideas they've articulated in a well structured form.

I've written React for several projects before this one but this project has helped me bring together many concepts to build something more complex.

Tech: React, Next.js, OpenAI, Vercel

[Source Code](https://github.com/danielcorin/write-partner/)

![screenshot](/img/projects/write-partner.png)
