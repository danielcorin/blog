---
categories: code
date: "2019-01-06T00:00:00Z"
title: Go and Unix files
aliases:
    - /code/2019/01/06/unix-files-with-spaces.html
tags:
    - code
    - unix
    - go
---

I ran into an odd Unix filename issue while writing Go code the other day.

Here's a simplified example:

Let's read a json file and unmarshall its contents into a struct in go. First, let's set an environment variable with our file name to avoid hardcoded constants in our program.

    export MY_FILE="/Users/dancorin/Desktop/test.json "

Now, let's read the file into our struct:

{{< highlight go >}}
package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
)

// Stuff struct holds the json contents
type Stuff struct {
    Test string `json:"test"`
}

func main() {
    stuff := Stuff{}
    place := os.Getenv("MY_FILE")
    data, err := ioutil.ReadFile(place)
    if err != nil {
        panic(err)
    }
    json.Unmarshal(data, &stuff)
    fmt.Printf("%+v\n", stuff)
}
{{< / highlight >}}

    ❯ go run program.go
    panic: open /Users/dancorin/Desktop/test.json : no such file or directory

    goroutine 1 [running]:
    main.main()
        /Users/dancorin/Desktop/program.go:20 +0x156
    exit status 2

Looks like Go couldn't find my file.

    ❯ pwd
    /Users/dancorin/Desktop
    ❯ ls test*
    test.json

The file definitely exists. What about its permissions?

    ❯ ls -ltrah test*
    -rw-r--r--  1 dancorin  staff    18B May  9 15:56 test.json

Looks like the file is readable by my program too. So, what is happening?

    ❯ cat test.json
    {"test": "stuff"}

I can see the file contents too.

    ❯ cat /Users/dancorin/Desktop/test.json
    {"test": "stuff"}

And I am using the proper path. Let's check that Go is trying to read the correct file path.

{{< highlight go >}}
package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
)

// Stuff struct holds the json contents
type Stuff struct {
    Test string `json:"test"`
}

func main() {
    stuff := Stuff{}
    place := os.Getenv("MY_FILE")
    fmt.Printf("PLACE: %s\n", place)
    data, err := ioutil.ReadFile(place)
    if err != nil {
        panic(err)
    }
    json.Unmarshal(data, &stuff)
    fmt.Printf("%+v\n", stuff)
}
{{< / highlight >}}

Running the code:

    ❯ go run program.go
    PLACE: /Users/dancorin/Desktop/test.json
    panic: open /Users/dancorin/Desktop/test.json : no such file or directory

    goroutine 1 [running]:
    main.main()
        /Users/dancorin/Desktop/program.go:21 +0x202
    exit status 2

The value of the environment variable appears to be correct.

Let see if we can find any weird characters hiding in the string:

{{< highlight go >}}
package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "os"
)

// Stuff struct holds the json contents
type Stuff struct {
    Test string `json:"test"`
}

func main() {
    stuff := Stuff{}
    place := os.Getenv("MY_FILE")
    fmt.Printf(">%s<\n", place)
    data, err := ioutil.ReadFile(place)
    if err != nil {
        panic(err)
    }
    json.Unmarshal(data, &stuff)
    fmt.Printf("%+v\n", stuff)
}
{{< / highlight >}}

    ❯ go run program.go
    >/Users/dancorin/Desktop/test.json <
    panic: open /Users/dancorin/Desktop/test.json : no such file or directory

    goroutine 1 [running]:
    main.main()
        /Users/dancorin/Desktop/program.go:21 +0x202
    exit status 2

Looks like there is an expected space showing up in ` >/Users/dancorin/Desktop/test.json <`. Where is it coming from?

Back when we set our environment variable it looks like we accidentally added a trailing space.

    export MY_FILE="/Users/dancorin/Desktop/test.json "

Go tries to tell us this:

    panic: open /Users/dancorin/Desktop/test.json : no such file or directory

It's just not _that_ obvious that there is a space in there. Something like the follow could have helped:

    panic: open "/Users/dancorin/Desktop/test.json ": no such file or directory

Unix makes this issue a little nastier because it has no problem allowing you to create file names with trailing spaces. We can fix our issue by running:

    ❯ cp test.json "test.json "

    ❯ go run program.go
    >/Users/dancorin/Desktop/test.json <
    {Test:stuff}


Or, more correctly, by fixing our `export` command"

    export MY_FILE="/Users/dancorin/Desktop/test.json"

Hope you never run into this one!
