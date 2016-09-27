#!/usr/bin/env python
'''
    Created by: Lyuwen Fu
    On: Thu Aug 11 20:12:20 2016
'''
import os,sys
from .models import Logs, Pmt
members="sicen lyuwen dian xuechun xiwen pengyu".split()
def getName(byName):
    if byName.lower() in members: return byName.lower()
    for n in members:
        if byName.lower().find(n)>-1:
            return n
    return byName.lower()

class SharedPurchase():
    def __init__(self, initWithPurchase, andPayment):
        if len(initWithPurchase) == 0 :
            sys.stderr.write("No values!\n")
            self.isempty=True
            return
        self.sum=0.
        self.totalPayment=0.
        self.sharedPurchase={}
        self.payment={}
        for s in members: self.payment[s]=0.0
        for p in andPayment:
            fromName=getName(byName=str(p.fromN))
            toName=getName(byName=str(p.toN))
            if (fromName in self.payment.keys()) and (toName in self.payment.keys()):
                self.payment[fromName]+=p.amount
                self.payment[toName]-=p.amount
                self.totalPayment+=p.amount
        for s in initWithPurchase:
            price=s.price
            name = getName(byName=s.name)
            if name not in self.sharedPurchase.keys():
                self.sharedPurchase[name]=0.
            self.sharedPurchase[name]+=price
            if name in members: self.sum+=price
        self.ave=self.sum/6.
        self.due={}
        for s in members: self.due[s]=self.ave
	if len(self.sharedPurchase.keys())>0:
	    for s in self.sharedPurchase.keys():
                if s in members: 
                     self.due[s]-=self.sharedPurchase[s]
        self.balance={}
        for s in members:
            self.balance[s]=self.due[s]-self.payment[s]

        self.sum=sum([s.price for s in initWithPurchase if not s.cleared and getName(byName=s.name) in members])
        self.ave=self.sum/6.
    def __str__(self):
	if dir(self).count('isempty'): return ''
        string='Total\t{:.2f}\nAve\t{:.2f}\n'.format(self.sum,self.ave)+'-'+'\n'
        for s in members:
            string = string + '{}\t{:.2f}\n'.format(s,self.due[s])
        return string
    def getList(self):
        return [[s.title(),'{:.2f}'.format(self.balance[s])] for s in members]
if __name__ == "__main__":
    #a=SharedPurchase(initWithPurchase=[], andPayment=[])
    print "Import as a module to use"
