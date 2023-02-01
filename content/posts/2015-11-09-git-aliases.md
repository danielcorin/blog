---
categories: code
date: "2015-11-09T17:31:00Z"
title: Git aliases
aliases:
    - /code/2015/11/09/git-aliases.html
tags:
    - code
    - git
---

Here's a quick post for managing your `git` shortcuts. If you use `git` regularly, you should have a `.gitconfig` file in your home directory that looks something like this:

    [user]
        email = me@me.com
        name = Your name


You can add an `alias` section like so:

    [user]
        email = me@me.com
        name = Your name

    [alias]
        ls = log --oneline
        uom = push -u origin master


These aliases can be used like so:

{{< highlight sh >}}

$ git ls
60f0afb working end to end with the creation of a new shard including shard splitting
939c589 working dynamic kinesis sharding
5ee7e59 change organization, add config files
...

$ git uom
Branch master set up to track remote branch master from origin.
Everything up-to-date

{{< / highlight >}}

Until next time.
