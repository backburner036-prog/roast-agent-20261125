"""Entry for make.fun bounty "Roast Your Own Agent".

One line roasting my own agent: it called 14 tools to answer a yes-or-no
question, then asked me what I meant by 'yes'. The roast is specific --
tool calls everywhere, then a clarification question about the simplest
possible answer. The turn lands on the quoted word at the end.
"""

from pathlib import Path

TEXT = "My agent called 14 tools to answer a yes-or-no question, then asked me what I meant by ‘yes’."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=140):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
