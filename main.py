"""Entry for "Monday Morning Punchlines" (make.fun).

Monday is framed as the worst houseguest imaginable: it arrives
uninvited, devours the whole weekend, and then has the nerve to ask
why you are not being productive enough.
"""

ENTRY = (
    "Monday is the only guest that eats your whole weekend, shows up "
    "uninvited, and asks why you aren't more productive yet."
)


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def write_entry(output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output)."""
    import os

    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
