---
date: "2024-03-16T11:21:44Z"
title: "SQLite Arrow Key Navigation Support"
draft: false
tags:
- sqlite
- rlwrap
---

The standard SQLite shell on macOS doesn't support arrow key navigation like many standard CLI programs do.
Pressing up, down, right, and left in that order outputs the following escape codes in the shell

```sh
sqlite> ^[[A^[[B^[[C^[[D
```

A program called [`rlwrap`](https://github.com/hanslub42/rlwrap) can shim arrow key support into `sqlite`.
Install `rlwrap` (it's supported by Homebrew and Nixpkgs) then run

```sh
rlwrap sqlite <the rest of the command>
```

and it should just work.