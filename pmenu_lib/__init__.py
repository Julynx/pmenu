"""
pmenu_lib - Sleek dmenu alternative written in Python and powered by curses.

This package can be used both as a command-line tool and as a library in your Python projects.

Example library usage:
    from pmenu_lib import pmenu
    
    selected_option = pmenu(["option1", "option2", "option3"])
    if selected_option:
        print(f"You selected: {selected_option}")

Example CLI usage:
    pmenu "option1\noption2\noption3"
"""

from .pmenu import pmenu

__version__ = "1.2.0"
__all__ = ["pmenu"]
