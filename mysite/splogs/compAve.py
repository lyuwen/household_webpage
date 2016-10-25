#!/usr/bin/env python
'''
    Created by: Lyuwen Fu
    On: Thu Aug 11 20:12:20 2016
'''
import os,sys
from .models import Logs, Pmt
from django.contrib.auth.models import User, Group


DefaultMembers=[]
class SharedPurchase():
    def getName(self, byName):
        if byName.lower() in self.members: return byName.lower()
        for n in self.members:
            if byName.lower().find(n)>-1:
                return n
        return byName.lower()
    def __init__(self, initWithPurchase, andPayment, andMembers=DefaultMembers):
        self.members=andMembers
        if len(initWithPurchase) == 0 :
            sys.stderr.write("No values!\n")
            self.isempty=True
            return
        self.sum=0.
        self.totalPayment=0.
        self.sharedPurchase={}
        self.payment={}
        for s in self.members: self.payment[s]=0.0
        for p in andPayment:
            fromName=self.getName(byName=str(p.fromN))
            toName=self.getName(byName=str(p.toN))
            if (fromName in self.payment.keys()) and (toName in self.payment.keys()):
                self.payment[fromName]+=p.amount
                self.payment[toName]-=p.amount
                self.totalPayment+=p.amount
        for s in initWithPurchase:
            price=s.price
            name = self.getName(byName=s.name)
            if name not in self.sharedPurchase.keys():
                self.sharedPurchase[name]=0.
            self.sharedPurchase[name]+=price
            if name in self.members: self.sum+=price
        self.ave=self.sum/6.
        self.due={}
        for s in self.members: self.due[s]=self.ave
	if len(self.sharedPurchase.keys())>0:
	    for s in self.sharedPurchase.keys():
                if s in self.members: 
                     self.due[s]-=self.sharedPurchase[s]
        self.balance={}
        for s in self.members:
            self.balance[s]=self.due[s]-self.payment[s]

        self.sum=sum([s.price for s in initWithPurchase if not s.cleared and self.getName(byName=s.name) in self.members])
        self.ave=self.sum/6.
    def __str__(self):
	if dir(self).count('isempty'): return ''
        string='Total\t{:.2f}\nAve\t{:.2f}\n'.format(self.sum,self.ave)+'-'+'\n'
        for s in self.members:
            string = string + '{}\t{:.2f}\n'.format(s,self.due[s])
        return string
    def getList(self):
        return [[s.title(),'{:.2f}'.format(self.balance[s])] for s in self.members]
if __name__ == "__main__":
    #a=SharedPurchase(initWithPurchase=[], andPayment=[])
    print "Import as a module to use"
