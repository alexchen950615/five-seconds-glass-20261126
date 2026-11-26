"""Five Seconds to Explain the Glass.

Writes the house cat's one-sentence defence to /output/entry.txt
and prints it to stdout.
"""

import os

ENTRY = (
    "It was blocking the view from my throne, "
    "so I demoted it to floor duty \u2014 the table is mine, "
    "and I don't negotiate with glassware."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
