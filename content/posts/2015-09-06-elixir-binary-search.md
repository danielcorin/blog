---
categories: code
date: "2015-09-06T19:08:00Z"
title: Elixir binary search
aliases:
    - /code/2015/09/06/elixir-binary-search.html
tags:
    - code
    - elixir
---

A few days ago, I saw a Guess my word game on the front page of Hacker News. Before spoiling the fun for myself by checking out the comments, I decided to try my hand at writing a solution in Elixir. Afterwards, I generalized the code to choose its own word from the UNIX dictionary and then "guess" it, applying a binary search based on the feedback of whether each guess was alphabetically greater or less than the word itself.

{{< gist danielcorin ab458ec544178fb86076 >}}

Example output:

{{< highlight sh >}}

$ iex words.exs 

Word is: barruly
Less than: modificatory
Less than: eagerness
Less than: canari
Greater than: asthenosphere
Less than: bifoliolate
Greater than: barad
Less than: beguilement
Less than: batzen
Less than: basaltic
Greater than: barmbrack
Greater than: barreler
Less than: bartholomew
Greater than: barrio
Found word: barruly

{{< / highlight >}}

Something I encountered worth mentioning is how Elixir compares strings that have different capitalization. Capital letters are "less than" their lower case versions:

{{< highlight elixir >}}

iex> "B" < "b"
true

{{< / highlight >}}

Knowing this, we use `String.downcase` in our implementation to avoid comparison issues in the binary search. Binary search has a time complexity of log₂(N).

Given that the UNIX dictionary has 235,886 words

{{< highlight sh >}}
$ cat /usr/share/dict/words | wc -l
235886
{{< / highlight >}}

the fact the our algorithm took 14 steps to "guess" the word is plausible given

O(log₂(235886)) ≈ O(17.85)

which is the number of steps we would expect it to take to guess our word.


