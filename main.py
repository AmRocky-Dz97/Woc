#!usr/bin/env python
#
# WOC v 1.0
# Coded By AmRocky-Dz97
#           2014 &copy;
# 

import func
from wc import *
import sys
import os
import signal

def ctrl_c(a,b) :
 print "\nhhh nn You Can't Kill Me :v !!!"
signal.signal(signal.SIGINT,ctrl_c);
print ""
func.wcm();
print "Os : "+func._os();
try :
 import colorama
 print "colorama : On ( use colmain.py for colored version )";
except :
 print "colorama : Off";
try :
 filename = sys.argv[4];
except :
 filename = "output.txt"

try :
 Min = int(sys.argv[1]);
 Max = int(sys.argv[2]);
 chars = func.re_char(sys.argv[3]);
except :
 print "[!] Error Syntax "
 print "Usage: woc <min> <max> [options]"
 print "where min and max are numbers"
 print "  ex : user@Unix:~/$ python main.py <min> <max> chars saved.txt "
 print "  ex : user@Unix:~/$ python main.py 1 5 abcd1fg5 saved.txt \n"
 sys.exit(1);
func.sec(Max,Min);
lines = func.calc(chars,Min,Max);
size = func.tai_con(func.calc_tai(chars,Min,Max));
sec_line = 1000000;

if __name__ == "__main__" and Min <= Max :
 try : 
  cv = Wc(chars,Min,Max,filename);
  

  if lines > sec_line :
   print "Calculated Lines : %d"%lines
   print "Size : %.1f %s"%(size[0],size[1])
   res = raw_input("Do You Whant Continue ? (y/N) : ");
  elif lines < sec_line :
   print "Calculated Lines : %d"%lines
   print "Size : %.1f %s"%(size[0],size[1])
   res = raw_input("Do You Whant Continue ? (Y/n) : ");
  else :
    print "Calculated Lines : %d"%lines
    print "Size : %.1f %s"%(size[0],size[1])
    res = raw_input("Do You Whant Continue ? (Y/N) : ");



  if cv.sec == 1 and res == "Y" or res == "y" or res == "YES" or res == "yes" or res == "Yes" or res == "YEs" or res == "yEs" or res == "yeS" :
   if cv.run() == 1 :
    print "Saved on : %s"%(filename);
   else :
    print "[!] error as Creating Wordlist Or Unkown Erro !!!";
    sys.exit(1);
  else :
   print "[!] Exiting ...";
 except :
  func.error(10);
else :
 func.error(10);
