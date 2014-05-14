#!usr/bin/evn python
#! -*- coding:utf8 -*-
from __future__ import division
import re
from math import sqrt

class Similarity(object):
    def __init__(self, target1, target2):
        self.target1 = target1
        self.target2 = target2

    def vector(self):
        self.vdict1 = {}
        self.vdict2 = {}
        for target in re.findall('([a-zA-Z0-9_.&%]+)+', self.target1):
                self.vdict1[target] = self.vdict1.get(target, 0) + 1
        for target in re.findall('([a-zA-Z0-9_.&%]+)+', self.target2):
                self.vdict2[target] = self.vdict2.get(target, 0) + 1

    def mix(self):
        def mapminmax(vdict):
            _min = min(vdict.values())
            _max = max(vdict.values())
            _mid = _max - _min
            print _min, _max, _mid
            for key in vdict:
                vdict[key] = (vdict[key] - _min)/_mid
            return vdict
        for key in self.vdict1:
            self.vdict2[key] = self.vdict2.get(key, 0)
        for key in self.vdict2:
            self.vdict1[key] = self.vdict1.get(key, 0)
        self.vdict1 = mapminmax(self.vdict1)
        self.vdict2 = mapminmax(self.vdict2)

    def similar(self):
        self.vector()
        self.mix()
        sum = 0
        for key in self.vdict1:
            sum += self.vdict1[key] * self.vdict2[key]
        A = sqrt(reduce(lambda x,y: x+y, map(lambda x: x*x, self.vdict1.values())))
        B = sqrt(reduce(lambda x,y: x+y, map(lambda x: x*x, self.vdict2.values())))
        return sum/(A*B)

if __name__ == '__main__':
    t1 = file("20_1.c", "r").read()
    t2 = file("28_1.c", "r").read()
    s = Similarity(t1, t2)
    print s.similar()