#!usr/bin/env python
#
# WOC v 1.0
# Coded By AmRocky-Dz97
#           2014 &copy;
# 


import func
import sys
import signal

def ctrl_c(a,b) :
 print "\nhhh nn You Can't Kill Me :v !!!"
signal.signal(signal.SIGINT,ctrl_c);

print "";
func.wcm();
try :
 import colorama
 from color import *
 print "Os : "+color.blue+func._os()+color.clear;
 print "colorama : "+color.green+"On"+color.clear;
except :
 print "Os : "+func._os();
 print "colorama : Off (please Use main.py classic Version)";
 print "[!] Exiting ...";
 sys.exit(1);


import os
from wc import *

def error(n) :
 print color.red+"Error-Maybe :"+color.clear;
 if n == 0 :
  print color.red+"[!]"+color.clear+" ^^ <"+color.green+"min"+color.clear+"> > <"+color.green+"max"+color.clear+"> !!!";
 elif n == 1 :
  print color.yellow+"[!] ^^ max > 20 !!!"+color.clear
 elif n == 2 :
  print color+yellow+"[!] ^^ Chars Not in ASCII !!!"+color.clear
 else :
  print color.red+"[!]"+color.clear+" ^^ <"+color.green+"min"+color.clear+"> > <"+color.green+"max"+color.clear+"> !!!";
  print color.yellow+"[!] Or ^^ max > 20 !!!"+color.clear
  print color.yellow+"[!] Or ^^ Chars Not in ASCII !!!"+color.clear

def sec(Max,Min) :
 if Min > 20 or Max > 20 :
  error(1);
  sys.exit(1);
 else :
  pass

try :
 filename = sys.argv[4];
except :
 filename = "output.txt"

try :
 Min = int(sys.argv[1]);
 Max = int(sys.argv[2]);
 chars = func.re_char(sys.argv[3]);
except :
 print color.red+"[!] Error Syntax "+color.clear
 print "Usage: woc <"+color.green+"min"+color.clear+"> <"+color.green+"Max"+color.clear+"> ["+color.green+"options"+color.clear+"]"
 print "where "+color.green+"min"+color.clear+" and "+color.green+"max"+color.clear+" are "+color.green+"numbers"+color.clear
 print "  ex : "+color.red+"user"+color.clear+"@Unix:~/$ python main.py <"+color.green+"min"+color.clear+"> <"+color.green+"max"+color.clear+"> chars saved.txt "
 print "  ex : "+color.red+"user"+color.clear+"@Unix:~/$ python main.py 1 5 abcd1fg5 saved.txt\n"
 sys.exit(1);

sec(Max,Min);
lines = func.calc(chars,Min,Max);
size = func.tai_con(func.calc_tai(chars,Min,Max));

sec_line = 1000000;
if __name__ == "__main__" and Min <= Max :
 try :
  cv = Wc(chars,Min,Max,filename);
  if lines > sec_line :
   print "Calculated Lines : %s"%color.red+str(lines)+color.clear
   print "Size :"+color.red,
   print "%.1f"%size[0],
   print color.clear+size[1]
   res = raw_input("Do You Whant Continue ? ("+color.red+"y"+color.clear+"/"+color.green+"N"+color.clear+") : ");
  elif lines < sec_line :
   print "Calculated Lines : %s"%color.green+str(lines)+color.clear
   print "Size :"+color.green,
   print "%.1f"%size[0],
   print color.clear+size[1]
   res = raw_input("Do You Whant Continue ? ("+color.green+"Y"+color.clear+"/"+color.red+"n"+color.clear+") : ");
  else :
    print "Calculated Lines : %s"%color.white+str(lines)+color.clear;
    print "Size :"+color.white,
    print "%.1f"%size[0],
    print color.clear+size[1]
    res = raw_input("Do You Whant Continue ? ("+color.red+"Y"+color.clear+"/"+color.RED+"N"+color.clear+") : ");




  if cv.sec == 1 and res == "Y" or res == "y" or res == "YES" or res == "yes" or res == "Yes" or res == "YEs" or res == "yEs" or res == "yeS" :
   if cv.run() == 1 :
    print "Saved on : %s"%(filename);
   else :
    print color.red+"[!] error as Creating Wordlist Or Unkown Erro !!!"+color.clear;
    sys.exit(1);
  else :
   print color.red+"[!] Exiting ..."+color.clear;

 except :
  error(10);
else :
 error(10);
 
