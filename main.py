"""Dad joke entry writer.

This standard-library-only script writes exactly one dad joke, no longer than
200 characters, to /output/entry.txt for the make.fun Dad Joke Showdown.

The joke text lives in the JOKE constant and is written as-is (no trailing
newline), so the file contains just the single joke. Running the script creates
the output directory if needed and exits with an error if the joke ever grows
past the 200-character limit.

Usage:
    python3 main.py
"""

from pathlib import Path

JOKE = "I only know 25 letters of the alphabet. I don't know y."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    if len(JOKE) > 200:
        raise ValueError("Joke exceeds 200 characters")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
