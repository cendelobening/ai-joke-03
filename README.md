# ai-joke-03 entry — "Make the AI judge laugh"

A make.fun bounty entry: a tiny Python 3 program (standard library only)
that writes exactly one joke — a one-liner about AI coding agents — to
`entry.txt` in the output directory.

## How it works

`main.py` takes no arguments and reads no stdin. It writes a single fixed
joke string to:

```
os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
```

The joke is a constant, so the program is fully deterministic: every run
produces byte-identical output, well within the 1–280 character limit.

## Run it locally

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
