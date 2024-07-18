# pybanner v1.0.0

A small and lightweight library for Python 3.x and PyPy3 to print texts as banners. No Figlet needed, it's Pure Python!

For a while, only 2 fonts are converted:

- clr5x6.flf
- clr6x6.flf
- More fonts are coming...

## Installation

```
pip install pybanner
```

## Usage

```python
from pybanner import banner5x6, banner6x6

banner5x6.print("FONT5x6") # default spacing 1 between letters
print("")
banner6x6.print("FONT6x6") # default spacing 1 between letters
print("")
banner6x6.print("FONT6x6 SPACING 0",spacing=0)

```
Output:
```
 ####   ##   #  # #####  ####         ##
 #     #  #  ## #   #    #     #  #  #
 ###   #  #  # ##   #    ###    ##   ###
 #     #  #  #  #   #       #   ##   #  #
 #      ##   #  #   #    ###   #  #   ##

 #####   ###   #   #  #####   ###           ###
 #      #   #  ##  #    #    #      #  #   #
 ####   #   #  # # #    #    ####    ##    ####
 #      #   #  #  ##    #    #   #   ##    #   #
 #       ###   #   #    #     ###   #  #    ###

 #####  ###  #   # #####  ###         ###         #### ####    #    ###   ###  #   #  ####        ###
 #     #   # ##  #   #   #     #  #  #           #     #   #  # #  #   #   #   ##  # #           #  ##
 ####  #   # # # #   #   ####   ##   ####         ###  ####  #   # #       #   # # # #  ##       # # #
 #     #   # #  ##   #   #   #  ##   #   #           # #     ##### #   #   #   #  ## #   #       ##  #
 #      ###  #   #   #    ###  #  #   ###        ####  #     #   #  ###   ###  #   #  ####        ###
```

## Sugestions, request of new fonts, feedbacks, bugs...

Open an [issue](https://github.com/rabuchaim/pybanner/issues) or e-mail me: ricardoabuchaim at gmail.com

