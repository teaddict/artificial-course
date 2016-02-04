#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Oct 21, 2015

@author: teaddict
'''
#Kuyruk Sınıfımızı oluşturup fonksiyonlarımızı ekledik
class Queue(object):
    def __init__(self):
        #kuyruğa eklediklerimiz
        self.inqueue=[]
        #kuyruktan çıkardıklarımız
        self.outqueue=[]
    def enqueue(self,element):
        self.inqueue.append(element)
    def dequeue(self):
        if not self.outqueue:
            while self.inqueue:
                #kuyruktan fifo ile çıkartıyoruz döngü içinde
                self.outqueue.append(self.inqueue.pop())
        return self.outqueue.pop()
q=Queue()
for i in range(10):
    q.enqueue(i)
    print(str(i) + ": Kuyruğa eklendi!")
print("####################################################")
for i in range(10):
    print(str(q.dequeue()) + ": kuyruktan çıkartıldı!")

print("####################################################")
print("Kuyruğa giriş sırası ve çıkış sırası aynıdır!")