#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Oct 21, 2015

@author: teaddict
'''

class Stack(object):
    def __init__(self):
        #burda verilerimizi saklaycağız
        self.instack = []
        #burda ise çıkartılan veriler saklanacak
        self.outstack= []
        
    #stack sıfırlanınca duracak
    def stack_empty(self):
        if len(self.instack)==0:
            return True
        else:
            return False
    
    #stacke ekleme yap
    def push(self,x):
        self.instack.append(x)
    #stackten çıkar LIFO
    def pop(self):
        if self.stack_empty():
            print("Stack Boş!!!!")
            print("####################################################")
            exit()
        else:
            self.outstack.append(self.instack.pop())
        return self.outstack.pop()
s = Stack()

for i in range (10):
    s.push(i)
    print(str(i) + ": Stacke eklendi!")
print("####################################################")
#fazladan döngü yaptırıyoruz ki stack sıfırlanınca tepki versin
for i in range (11):
    print(str(s.pop()) + ": Stackten çıkartıldı!")