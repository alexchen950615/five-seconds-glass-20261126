"""Five Seconds to Explain the Glass.

Writes the house cat's one-sentence defence to /output/entry.txt
and prints it to stdout.
"""

import os

ENTRY = (
    "That glass was squatting in my sunbeam rent-free, "
    "so I served it an eviction notice \u2014 one push, no appeal."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
