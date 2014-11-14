#
# WOC v 1.0
# Coded By AmRocky-Dz97
#           2014 &copy;
# 

import wc
import base64
import sys
import hashlib


def error(n) :
 print "Error-Maybe :";
 if n == 0 :
  print "[!] <min> > <max> !!!";
  sys.exit(1);
 elif n == 1 :
  print "[!] ^^ max > 20 !!!";
  sys.exit(1);
 elif n == 2 :
  print "[!] ^^ Chars Not in ASCII !!!";
  sys.exit(1);
 else :
  print "[!] ^^ <min> > <max> !!!"; 
  print "[!] Or ^^ max > 20 !!!";
  print "[!] Or ^^ Chars Not in ASCII !!!";
  sys.exit(1);

def sec(Max,Min) :
 if Min > 20 or Max > 20 :
  error(1);
  sys.exit(1);
 else :
  pass

def wcm() : # dont toutch this !!!
 md5_0 = hashlib.md5();
 md5_1 = hashlib.md5();
 sn = "V2VsY29tZSBUbyBXT1QgMS4w";
 sn1 = "QnkgOiBBbVJvY2t5LUR6OTcgfCBGQiA6IC9UZWFtNFNlYw==";
 md5_0.update(sn);
 md5_1.update(sn1);
 lol = wc.Wc("1",1,1,"sec.log");
 lol.suc();
 if lol.key == md5_0.hexdigest() and lol.key1 == md5_1.hexdigest() :
  print base64.b64decode(sn);
  print base64.b64decode(sn1);
 else :
  print "[!] Hi Bitch this is For Me :'(\n(( i tell You Dont toutch the code source )) ";
  print "Exiting ...";
  sys.exit(1);
 
def _os() :
 name = sys.platform
 os = ["windows","mac","linux","other"];
 for i in xrange(len(os)-1) :
  if name.find(os[i]) == 0 :
   return os[i]; 
   break;
 return os[3];

def calc(chars,a,b) :
 le = len(chars);
 num = 0
 for i in xrange(a,b+1,1) :
   num += le**i
 return num


def calc_tai(chars,a,b) :
 try :
  le = len(chars);
  dic = {};
  for i in xrange(a,b+1,1) :
   dic[i] = le**i
  tai = 0;
  for j in xrange(a,b+1) :
   cur = dic.get(j);
   tai += (cur)*(j+1);
  return tai
 except :
  print "Error-Maybe :";
  print "[!] BIGG SIZE !!!";
  print "[!] Or ^^ Chars Not in ASCII !!!"
  sys.exit(1);


def tai_con(tai) :
 try :
  bytes = tai
  kB = bytes/1000.000000
  MB = kB/1000.000000
  GB = MB/1000.000000
  T = GB/1000.000000
  PB = T/1000.000000
  Sec = 0
  if bytes < 1000 :
   return [bytes,"bytes"];
  elif kB < 1000 :
   return [kB,"kB"];
  elif MB < 1000 :
   return [MB,"MB"];
  elif GB < 1000 :
   return [GB,"GB"];
  elif T < 1000 :
   return [T,"T"];
# elif PB < 1000 :
#  return [PB,"PB"];
  else :
   return [PB,"PB"];
#  return [Sec,"Sec"];

 except :
  error(2);

      
 

def re_char(chars):
 try :
  new = "";
  for i in xrange(len(chars)) :
   if chars[i] not in new :
    new += chars[i];
  return new
 except :
  error(2);
