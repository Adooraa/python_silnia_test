# -*- coding: UTF-8 -*-
import sys
class silnia:
    kop = 1
    
    
    def __init__(self,root):
        self.root = root
        print(root)
    def show(self):
        
        r = self.root
        c = silnia.kop
        e = silnia.kop
        d =    silnia.kop
        
        
        
        for i in range(c,r):
            c = c * i 
            yield(c)
                                          
                          
                         
                
        
         
print("podaj ile chcesz mieć liczb powstałych ze wzoru na silnjią od zera "  )      
        
v = int(input("podaj liczbe:  "))

si = silnia(v)

f = si.show()
print("pierwasza liczba to zero a pozostałe to :")
while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()
