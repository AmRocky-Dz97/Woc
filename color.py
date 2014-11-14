#
# WOC v 1.0
# Coded By AmRocky-Dz97
#           2014 &copy;
# 
# just Some Color :v
#

import colorama


class Color :
 colorama.init(); # this For Windows :v
 def __init__(self) :
  self.white = colorama.Fore.WHITE
  self.red = colorama.Fore.RED
  self.green = colorama.Fore.GREEN
  self.yellow = colorama.Fore.YELLOW
  self.blue = colorama.Fore.BLUE
  self.clear = colorama.Fore.RESET

color = Color();
