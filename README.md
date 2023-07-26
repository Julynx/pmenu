# pmenu
*Sleek dmenu alternative written in Python and powered by curses.*

<br>

<p align="center">
  <img width="600" src="https://i.imgur.com/SOZXGTS.png">
</p>
<br>

<p align="center">  
  <img width="600" src="https://i.imgur.com/2omHG8y.png">
</p>
<br>

## Installation
The following commands will download the latest version of [pmenu](https://github.com/Julynx/pmenu) from this repository
and install it in your `/usr/bin/` directory:
```
git clone https://github.com/Julynx/pmenu
cd pmenu
```
```
sudo chmod +x pmenu
sudo cp pmenu /usr/bin/
```
<br>

## Usage
```
Usage:
  pmenu  "line1\nline2\nline3..."
         "line1" "line2" "line3" ...

Bindings:
  up     Highlight previous option.
  down   Highlight next option.
  enter  Select highlighted option, will be written to "/tmp/pmenu".
  q      Quit menu and exit with code 1.
```
<br>

## pmenu_fm: A practical use case
The [pmenu_fm](https://raw.githubusercontent.com/Julynx/pmenu/main/pmenu_fm) script included in this repository is an example of how [pmenu](https://github.com/Julynx/pmenu) can be 
integrated into a bash script to implement a simple file selector. 

It uses [lsd](https://github.com/lsd-rs/lsd), a modern [ls](https://es.wikipedia.org/wiki/Ls) replacement, to get the list of files in the current directory and their associated icons.
The list is then passed to [pmenu](https://github.com/Julynx/pmenu), which displays a menu in the terminal window.

You can highlight a directory with the ```Up``` and ```Down``` keys, and change to the selected directory or [xdg-open](https://linux.die.net/man/1/xdg-open) the selected file with the ```Enter``` key. The menu can be closed with the ```Q``` key.

<br>

## Python integration
To use [pmenu](https://github.com/Julynx/pmenu) from your Python scripts, install the ```pmenu-lib``` package from [PyPi](https://pypi.org/project/pmenu-lib/):
```
pip install pmenu-lib
```
The ```pmenu(options)``` function will return the selected option as a string, or None if the menu is closed without selecting an option.
```python
from pmenu_lib import pmenu

selected_option = pmenu(["Option1", "Option2", "Option3"])
```
```
> Option1
Option2
Option3

(Enter)
```
```python
print(selected_option)
>> "Option1"
```
```
> Option1
Option2
Option3

(Q)
```
```python
print(selected_option)
>> None
```
