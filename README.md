# blog

My personal website

## Production

Deployed with Vercel, via Github commit hooks.

Build command

```sh
hugo --gc --minify --ignoreCache --verbose
```

## Dev

After fresh git clone

```sh
git submodule update --init --recursive
```

To run

```sh
make serve
```

```sh
open http://localhost:1313
```

## Content scaffolds

### Log

```sh
make log
```

### TIL

```sh
make til p={category}/{title}
```
