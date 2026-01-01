#!/usr/bin/env python3

"""
@file     cli.py
@brief    Command-line interface for pmenu.
@date     02/08/2023
@author   Julio Cabria
"""

import sys
import tempfile
from pathlib import Path
from .pmenu import pmenu

TMP_FILE = Path(tempfile.gettempdir()) / "pmenu"

YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0;0m"


def main():
    """
    Main function for CLI usage.
    """
    if len(sys.argv) == 2:
        text = sys.argv[1].split("\n")
    elif len(sys.argv) > 2:
        text = sys.argv[1:]
    else:
        print(
            f"\nUsage:\n"
            f"  {CYAN}pmenu  "
            f'{YELLOW}"line1{CYAN}\\n'
            f"{YELLOW}line2{CYAN}\\n"
            f'{YELLOW}line3..."{RESET}\n'
            f'         {YELLOW}"line1" "line2" "line3" ...{RESET}'
        )

        print(
            "\nBindings:\n"
            f"  {CYAN}up     {RESET}Highlight previous option.\n"
            f"  {CYAN}down   {RESET}Highlight next option.\n"
            f"  {CYAN}enter  {RESET}Select highlighted option, "
            f'will be written to {YELLOW}"{TMP_FILE}"{RESET}.\n'
            f"  {CYAN}esc    {RESET}Quit menu and exit with code 1.\n"
        )

        sys.exit(2)

    text = [line for line in text if line != ""]

    selected_option = pmenu(text)
    if selected_option is not None:
        TMP_FILE.write_text(selected_option, encoding="utf-8")
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
