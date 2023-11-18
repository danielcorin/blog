---
date: "2023-11-04T12:20:22Z"
title: "Including source files in a Bazel build"
description: "Making IDL files in builds with Bazel to use in language models"
draft: true
tags:
- bazel
- filegroup
- java
---

[Bazel](https://bazel.build/) is a highly configurable tool for building and testing software projects.
When using Bazel to build a Java app, the compiled Java classes often will not include the many of the source files used to produce the build itself.
Most of the time this approach makes sense, since a Java app doesn't need the Java or IDL source files at runtime.
However, when using language models, having the raw source available (particularly IDL files) becomes useful as I explored in [this post]({{< ref "posts/2023/protobuf-contracts-with-llms.md" >}}).
The following `BUILD` file configuration, adds all the `.proto` files the directory and subdirectories of the outputted build artifacts at their existing paths.

```starlark
filegroup(
    name = "proto_srcs",
    srcs = glob(["**/*"]),
)
```

With these files included in the build, we can now read a .proto file from the file system at runtime and use it in a prompt to a language model to shape its output.

Note: this approach only seems to works if the subdirectories *do not* contain their own `BUILD` files.