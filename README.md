# pmenu

*Sleek dmenu alternative written in Python and powered by curses.*

`pip install pmenu`

<br>

[![Button Hover](https://img.shields.io/badge/Github-c9510c?style=for-the-badge)](https://github.com/Julynx/pmenu)
[![Button Hover](https://img.shields.io/badge/PyPi-006dad?style=for-the-badge)](https://pypi.org/project/pmenu/)

<br>
<p align="center">
  <img width="600" src="https://i.imgur.com/2omHG8y.png">
</p>
<br>

Comes in different flavors:

- The ```pmenu``` CLI, for your terminal and shell scripts. [[📦 PyPi]](https://pypi.org/project/pmenu/) [[📂 GitHub]](https://github.com/Julynx/pmenu)
- The ```pmenu_lib``` package, for your Python projects. [[📦 PyPi]](https://pypi.org/project/pmenu-lib/) [[📂 GitHub]](https://github.com/Julynx/pmenu_lib)

You are now looking at the ```pmenu``` command for the terminal.

<br>

## Installation

You can install ```pmenu``` via [pip](https://pip.pypa.io/en/stable/):

```bash
pip install pmenu
```

<br>

## Usage

```bash
Usage:
  pmenu  "line1\nline2\nline3..."
         "line1" "line2" "line3" ...

Bindings:
  up     Highlight previous option.
  down   Highlight next option.
  enter  Select highlighted option, will be written to "/tmp/pmenu".
  esc    Quit menu and exit with code 1.
```

<br>

## pmenu_fm: A practical use case

The [pmenu_fm](https://raw.githubusercontent.com/Julynx/pmenu/main/pmenu_fm) script included in this repository is an example of how [pmenu](https://github.com/Julynx/pmenu) can be integrated into a bash script to implement a simple file selector.

It uses [lsd](https://github.com/lsd-rs/lsd), a modern [ls](https://es.wikipedia.org/wiki/Ls) replacement, to get the list of files in the current directory and their associated icons.

The list is then passed to [pmenu](https://github.com/Julynx/pmenu), which displays a menu in the terminal window.

You can highlight a directory with the ```Up``` and ```Down``` keys, and change to the selected directory or [xdg-open](https://linux.die.net/man/1/xdg-open) the selected file with the ```Enter``` key. The menu can be closed with the ```Esc``` key.
