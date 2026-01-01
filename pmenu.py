#!/usr/bin/env python3

"""
@file     pmenu
@brief    Sleek dmenu alternative written in Python and powered by curses.
@date     02/08/2023
@author   Julio Cabria
"""

import sys
import curses
import tempfile
from pathlib import Path
from contextlib import suppress

MAX_QUERY_LENGTH = 60
TMP_FILE = Path(tempfile.gettempdir()) / "pmenu"

YELLOW = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0;0m"

PRINTABLE_CHARS = range(32, 127)
ESC = 27


def main():
    """
    Main function.
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


def pmenu(lines):
    """
    Display a menu with the given lines and return the selected option.

    Args:
        lines (list): The lines to display in the menu.

    Returns:
        str: The selected option or None if the user quit the menu.
    """
    try:
        return curses.wrapper(_display_menu, lines)
    except KeyboardInterrupt:
        return None


def _display_menu(stdscr, lines):
    """
    Display a menu with the given lines and return the selected option.
    Don't call this function directly, use curses.wrapper(_display_menu, ...)
    instead.

    Args:
        stdscr (screen): The curses screen.
        lines (list): The lines to display in the menu.

    Returns:
        str: The selected option or None if the user quit the menu.
    """
    curses.curs_set(1)
    curses.use_default_colors()
    if hasattr(curses, "set_escdelay"):
        curses.set_escdelay(20)

    current_row = 0
    query = ""

    while True:
        stdscr.clear()
        filtered_lines = _filter_lines(lines, query)
        start_row, max_display_rows = _populate_screen(
            screen=stdscr, lines=filtered_lines, row=current_row, query=query
        )
        stdscr.refresh()
        key = stdscr.getch()

        if key == ord("\n"):
            with suppress(IndexError):
                return filtered_lines[current_row]

        elif key == curses.KEY_UP:
            if current_row > 0:
                current_row -= 1
            elif start_row > 0:
                start_row -= 1

        elif key == curses.KEY_DOWN:
            if current_row >= len(filtered_lines) - 1:
                continue
            current_row += 1
            if current_row == max_display_rows - 1:
                start_row += 1

        elif key == curses.KEY_BACKSPACE:
            current_row = 0
            query = query[:-1]

        elif key in PRINTABLE_CHARS:
            current_row = 0
            if len(query) < MAX_QUERY_LENGTH:
                query += chr(key)

        elif key == ESC:
            return None


def _filter_lines(lines, query):
    """
    Filter the given lines by the given query.

    Args:
        lines (list): The lines to filter.
        query (str): The query to filter the lines by.

    Returns:
        list: The filtered lines.
    """
    return [line for line in lines if query.lower() in line.lower()]


def _populate_screen(*, screen, lines, row, query):
    """
    Populate the given screen with the given lines.

    Args:
        screen (screen): The screen to populate.
        lines (list): The lines to populate the screen with.
        row (int): The index of the row to highlight.
        query (str): The query to display.

    Returns:
        tuple: The start row and the max display rows.
    """
    max_rows, _ = screen.getmaxyx()
    max_display_rows = min(max_rows - 1, len(lines))

    start_row = max(0, row - max_display_rows + 1)
    end_row = min(start_row + max_display_rows, len(lines))

    for line_number, line in enumerate(lines[start_row:end_row], start=start_row):
        with suppress(curses.error):
            if line_number == row:
                screen.addstr(line_number - start_row + 1, 0, line, curses.A_REVERSE)
                continue
            screen.addstr(line_number - start_row + 1, 0, line)

    screen.addstr(0, 0, "[Search]: " + query, curses.A_BOLD)

    return start_row, max_display_rows


if __name__ == "__main__":
    main()
