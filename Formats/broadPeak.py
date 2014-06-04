#!/usr/bin/env python

'''
Created on 11/07/2013

@author: slois
'''

from Utils.File import getLine
from Formats import Bed
import sys, math

class Record (Bed.Record):
    '''Holds information from a BED entry'''

    header = ['chrom', 'start', 'end', 'name', 'score', 'strand']

    def __init__(self, chrom='', start=-1, end=0, strand="+", score=0, name="region"):
	Bed.Record.__init__(self, chrom, start, end, strand, score, name)

    def setAdditionalFeatures (self, lst):
        h = ['firstStart', 'firstEnd', 'RGB', 'nblocks', 'lengths', 'starts']
        d = dict(zip(h, lst))
        for x in d: setattr(self, x, d[x])
	self.lengths = self.lengths.split(",")
        self.starts = self.starts.split(",")

class RecordParser (object):
    '''Parse BED data into a Bed.Record Object'''

    def __init__ (self):
        pass

    def parseString (self, string):
        lines = string.split("\t")
        n = len(lines)

        bedDict = dict(zip(Record.header[0:n], lines[0:n]))

        rec = Record(**bedDict)

        if n>6:
            rec.setAdditionalFeatures(lines[6:])

        return rec

def Iterator (handle, parser, intersect=False):
    for line in getLine(handle):
	if intersect:
                f = line.split("\t")
                s1 = "\t".join(f[0:10])
                s2 = "\t".join(f[10:20])
                olap = f[20]
                yield parser.parseString(s1), parser.parseString(s2), olap
        else:
                yield parser.parseString(line)
        
	yield parser.parseString(line)

def transform_values (n):
	return -math.log10(n)

def split2encodePeaks (string):
	f = string.split("\t")
	return (encodePeak("\t".join(f[0:10])), encodePeak("\t".join(f[10:20])), f[20])
