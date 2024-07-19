#!/usr/bin/env python3 

class line:
    def print():
        print("\n"+"- "*50+"\n")

line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner
banner.print("banner lower",spacing=0) 
print("")
banner.print("BANNER UPPER",spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner3 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner3d as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner4 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_5x7 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_5x8 as banner
banner.print(banner.__name__) 
print("")
banner.print(banner.__name__.upper()) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_6x9 as banner
banner.print(banner.__name__) 
print("")
banner.print(banner.__name__.upper()) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_6x10 as banner, MIDDOT
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr4x6 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr5x6 as banner
banner.print(banner.__name__) 
print("")
banner.print(banner.__name__.upper()) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr5x8 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0)
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr5x10 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0)
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr6x6 as banner
banner.print(banner.__name__) 
print("")
banner.print(banner.__name__.upper()) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr6x8 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr6x10 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clb6x10 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr7x8 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr7x10 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr8x8 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clb8x8 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clr8x10 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()
##──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
from pybanner import banner_clb8x10 as banner
banner.print(banner.__name__,spacing=0) 
print("")
banner.print(banner.__name__.upper(),spacing=0) 
line.print()

####################################################################################################################################
####################################################################################################################################

from pybanner import banner_clr6x6 as banner, MIDDOT
banner.print("BANNER clr6x6",spacing=1) 
print("")
banner.print("BANNER clr6x6",spacing=0) 
print("")
banner.print("BANNER clr6x6",char="^") 
print("")
banner.print("BANNER clr6x6",char=MIDDOT) 
print("")
