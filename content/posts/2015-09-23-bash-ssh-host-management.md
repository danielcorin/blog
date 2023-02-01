---
categories: code
date: "2015-09-23T18:03:00Z"
title: Bash SSH host management
aliases:
    - /code/2015/09/23/bash-ssh-host-management.html
tags:
    - code
    - ssh
    - awk
---

If you have a lot of servers to which you frequently connect, keeping track of IP addresses, pem files, and credentials can be tedious. SSH `config` files are great for this problem, but they don't play well with bash. I wanted to store all of my hosts' info in a `config` file but still have access to the `HostName`s since sometimes I just need the IP address of a server to use elsewhere.

An example ssh `config` file might look like this:

`~/.ssh/config`

    Host myserver
        HostName x.x.x.x
        User ubuntu
        IdentityFile ~/.ssh/mypem.pem

We can use AWK to parse the `~/.ssh/config` file and create bash variables with the name of the `Host`s and the values of the `HostName` respectively.

{{< highlight sh >}}

    $ cat ~/.ssh/config  | awk '$1 ~ /Host/ { print $2 }' | awk 'BEGIN {OFS = ""}!(NR%2){print p,"=\"", $0, "\"" }{p=$0}'

{{< / highlight >}}

First, `cat ~/.ssh/config` creates a stream of our `config` file. Next, `awk '$1 ~ /Host/ { print $2 }'` finds all lines that start with "Host" and prints the value after them seperated (by default) by any type of whitespace. The last bit does most of the work:

    awk 'BEGIN {
        OFS = "" # set Output Field Separator to empty string
    }
    !(NR%2){ # if the line number mod two is zero (AWK is 1-indexed)
        print p,"=\"", $0, "\"" # print the alias line
    }
    {
        p=$0 # store the current line to be printed on the next iteration
    }'

The output of the command is:
    
    myserver="x.x.x.x"

for each of your `Host`s in your `config` file. *NOTE*: I recommend only using this trick for server names with exclusively alphanumeric characters. Otherwise, you may see strange errors like `-bash: <server_name>=<host_name>: command not found` when the shell initializes.


You can add this to your bash initialization to get access to all your `HostName`s as variables from your ssh `config`.

`.bashrc`

    cat ~/.ssh/config  | awk '$1 ~ /Host/ { print $2 }' | awk 'BEGIN {OFS = ""}!(NR%2){print "alias ", p,"=\"", $0, "\"" }{p=$0}' > ~/.servers

    source ~/.servers

Cheers!
