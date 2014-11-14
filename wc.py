#
# WOC v 1.0
# Coded By AmRocky-Dz97
#           2014 &copy;
# 

class Wc :
 " This Class Have Function For Help =D "
 def __init__(self,_arr,_min,_max,_file) :
  self.arr = _arr;
  self.Min = _min;
  self.Max = _max;
  self.File = _file;
  self.Max_Lines = 20;
  self.key = "9deca8883ae3e550";
  self.key1 = "18aec026829192c8";
 
 def save(self,_stdin) :
  try :
   o = open(self.File,"a+");
   o.write(_stdin+"\n");
   o.close();
  except :
   print "[!] Error in Permession Or in Size or Unknown !!!";
  

 def line_1(self) :
  if self.Min <= 1 and self.Max >= 1 :
   l = len(self.arr);
   for i in range(l) :
    self.save(self.arr[i]);

 def line_2(self) :
  if self.Min <= 2 and self.Max >= 2 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     self.save(self.arr[i]+self.arr[j]);

 def line_3(self) :
  if self.Min <= 3 and self.Max >= 3 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      self.save(self.arr[i]+self.arr[j]+self.arr[a]);

 def line_4(self) :
  if self.Min <= 4 and self.Max >= 4 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]);

 def line_5(self) :
  if self.Min <= 5 and self.Max >= 5 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]);

 def line_6(self) :
  if self.Min <= 6 and self.Max >= 6 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]);

 def line_7(self) :
  if self.Min <= 7 and self.Max >= 7 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]);

 def line_8(self) :
  if self.Min <= 8 and self.Max >= 8 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]);

 def suc(self) :
  self.key += "a024adf10fbac5c1";
  self.key1 += "b37c11cf1431667d";

 def line_9(self) :
  if self.Min <= 9 and self.Max >= 9 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]);

 def line_10(self) :
  if self.Min <= 10 and self.Max >= 10 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]);

 def line_11(self) :
  if self.Min <= 11 and self.Max >= 11 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]);

 def line_12(self) :
  if self.Min <= 12 and self.Max >= 12 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              for q in range(l) :
               self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]+self.arr[q]);

 def line_13(self) :
  if self.Min <= 13 and self.Max >= 13 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              for q in range(l) :
               for g in range(l) :
                self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]+self.arr[q]+self.arr[g]);

 def line_14(self) :
  if self.Min <= 14 and self.Max >= 14 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              for q in range(l) :
               for g in range(l) :
                for s in range(l) :
                 self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]+self.arr[q]+self.arr[g]+self.arr[s]);

 def line_15(self) :
  if self.Min <= 15 and self.Max >= 15 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              for q in range(l) :
               for g in range(l) :
                for s in range(l) :
                 for t in range(l) :
                  self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]+self.arr[q]+self.arr[g]+self.arr[s]+self.arr[t]);

 def line_16(self) :
  if self.Min <= 16 and self.Max >= 16 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              for q in range(l) :
               for g in range(l) :
                for s in range(l) :
                 for t in range(l) :
                  for u in range(l) :
                   self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]+self.arr[q]+self.arr[g]+self.arr[s]+self.arr[t]+self.arr[u]);

 def line_17(self) :
  if self.Min <= 17 and self.Max >= 17 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              for q in range(l) :
               for g in range(l) :
                for s in range(l) :
                 for t in range(l) :
                  for u in range(l) :
                   for v in range(l) :
                    self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]+self.arr[q]+self.arr[g]+self.arr[s]+self.arr[t]+self.arr[u]+self.arr[v]);

 def line_18(self) :
  if self.Min <= 18 and self.Max >= 18 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              for q in range(l) :
               for g in range(l) :
                for s in range(l) :
                 for t in range(l) :
                  for u in range(l) :
                   for v in range(l) :
                    for w in range(l) :
                     self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]+self.arr[q]+self.arr[g]+self.arr[s]+self.arr[t]+self.arr[u]+self.arr[v]+self.arr[w]);

 def line_19(self) :
  if self.Min <= 19 and self.Max >= 19 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              for q in range(l) :
               for g in range(l) :
                for s in range(l) :
                 for t in range(l) :
                  for u in range(l) :
                   for v in range(l) :
                    for w in range(l) :
                     for x in range(l) :
                      self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]+self.arr[q]+self.arr[g]+self.arr[s]+self.arr[t]+self.arr[u]+self.arr[v]+self.arr[w]+self.arr[x]);

 def line_20(self) :
  if self.Min <= 20 and self.Max >= 20 :
   l = len(self.arr);
   for i in range(l) :
    for j in range(l) :
     for a in range(l) :
      for b in range(l) :
       for c in range(l) :
        for d in range(l) :
         for e in range(l) :
          for f in range(l) :
           for k in range(l) :
            for r in range(l) :
             for p in range(l) :
              for q in range(l) :
               for g in range(l) :
                for s in range(l) :
                 for t in range(l) :
                  for u in range(l) :
                   for v in range(l) :
                    for w in range(l) :
                     for x in range(l) :
                      for y in range(l) :
                       self.save(self.arr[i]+self.arr[j]+self.arr[a]+self.arr[b]+self.arr[c]+self.arr[d]+self.arr[e]+self.arr[f]+self.arr[k]+self.arr[r]+self.arr[p]+self.arr[q]+self.arr[g]+self.arr[s]+self.arr[t]+self.arr[u]+self.arr[v]+self.arr[w]+self.arr[x]+self.arr[y]);

 def sec(self) :
 
  if self.Max < self.Max_Lines and self.Min < self.Max_Lines and self.Max > self.Min :
   return 1;
  else :
   return 0;

 def run(self) :
  try :
   
   self.line_1();
   print "5%";
   self.line_2();
   print "10%";
   self.line_3();
   print "15%";
   self.line_4();
   print "20%";
   self.line_5();
   print "25%";
   self.line_6();
   print "30%";
   self.line_7();
   print "35%";
   self.line_8();
   print "40%";
   self.line_9();
   print "45%";
   self.line_10();
   print "50%";
   self.line_11();
   print "55%";
   self.line_12();
   print "60%";
   self.line_13();
   print "65%";
   self.line_14();
   print "70%";
   self.line_15();
   print "75%";
   self.line_16();
   print "80%";
   self.line_17();
   print "85%";
   self.line_18();
   print "90%";
   self.line_19();
   print "95%";
   self.line_20();
   print "100%";

   return 1;
 
  except :
   return 0;
