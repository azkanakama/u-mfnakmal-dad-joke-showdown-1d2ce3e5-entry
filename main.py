"""Write this entry's dad joke to /output/entry.txt."""

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
