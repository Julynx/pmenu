# pmenu

*Sleek dmenu alternative written in Python and powered by curses.*

`pip install pmenu-lib`

<br>

[![Button Hover](https://img.shields.io/badge/Github-c9510c?style=for-the-badge)](https://github.com/Julynx/pmenu)
[![Button Hover](https://img.shields.io/badge/PyPi-006dad?style=for-the-badge)](https://pypi.org/project/pmenu-lib)

<br>
<p align="center">
  <img width="600" src="https://i.imgur.com/2omHG8y.png">
</p>
<br>

This package provides both a **command-line tool** and a **Python library** for creating interactive terminal menus.

## Usage

### Library Usage

The `pmenu(list_of_options)` function displays a menu and returns the selected option as a `str`, or `None` if the menu is closed without selecting an option.

```python
from pmenu_lib import pmenu

options = ["Option 1", "Option 2", "Option 3"]
selected_option = pmenu(options)

if selected_option:
    print(f"You selected: {selected_option}")
else:
    print("No option selected")
```

### CLI Usage

After installation, you can use `pmenu` from the command line:

```bash
pmenu "line1\nline2\nline3..."
```

Or pass multiple arguments:

```bash
pmenu "option1" "option2" "option3"
```

The selected option will be written to `/tmp/pmenu` (or equivalent temp directory on Windows).

## Exit Codes

- `0`: Option selected successfully
- `1`: Menu closed without selection (ESC pressed)
- `2`: Invalid usage (no arguments provided)

## Menu Bindings

- **Up arrow**: Highlight the previous menu entry
- **Down arrow**: Highlight the next menu entry
- **Type to search**: Filter options in real-time
- **Backspace**: Delete search characters
- **Enter**: Select the highlighted entry
- **Esc**: Close the menu without selecting

## pmenu_fm: A Practical Use Case (Linux)

The [`pmenu_fm`](https://raw.githubusercontent.com/Julynx/pmenu/main/pmenu_fm) script included in this repository is an example of how `pmenu` can be integrated into a bash script to implement a simple file selector.

It uses [lsd](https://github.com/lsd-rs/lsd), a modern [ls](https://es.wikipedia.org/wiki/Ls) replacement, to get the list of files in the current directory and their associated icons. The list is then passed to `pmenu`, which displays a menu in the terminal window.

You can highlight a directory with the **Up** and **Down** keys, and change to the selected directory or [xdg-open](https://linux.die.net/man/1/xdg-open) the selected file with the **Enter** key. The menu can be closed with the **Esc** key.
