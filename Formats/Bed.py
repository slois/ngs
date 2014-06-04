#!/usr/bin/env python

'''
Created on 11/07/2013

@author: slois
'''

from Utils.File import getLine
import sys, math

class Record (object):
    '''Holds information from a BED entry'''

    header = ['chrom', 'start', 'end', 'name', 'score', 'strand']

    def __init__(self, chrom='', start=-1, end=0, strand=".", score=0, name="region"):
        self.chromosome = str(chrom)
        self.startPosition = int(start)+1
        self.endPosition = int(end)
        self.strand = str(strand)
        self.name = str(name)
        self.score = float(score)

    def setAdditionalFeatures (self, lst):
        h = [ "V%s" % i for i in range(1, len(lst)+1)]
        d = dict(zip(h, lst))
        for x in d: setattr(self, x, d[x])

    def length(self):
        return float(self.endPosition - self.startPosition + 1)

    def writeBed(self):
        return "%s\t%s\t%s\t%s\t%s\t%s" % (self.chromosome, self.startPosition-1, self.endPosition, self.name, self.score, self.strand)

    def overlapRatio (self, other):
	olap = float(self.overlap(other))
	return olap/self.length(), olap/other.length()

    def UCSCcoords (self):
	return "%s:%s-%s" % (self.chromosome, self.startPosition, self.endPosition)


    def overlap (self, other):
	if self.chromosome == other.chromosome:
		return max(0, min(self.endPosition, other.endPosition) - max(self.startPosition, other.startPosition) + 1)

    def mergeCoordinates (self, other):
	if self.chromosome == other.chromosome:
		return (min(self.startPosition, other.startPosition), max(self.endPosition, other.endPosition))

    def __repr__(self):
        return "%s [%s:%s-%s (%s)]" % (self.name, self.chromosome, self.startPosition, self.endPosition, self.strand)

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
        yield parser.parseString(line)

def transform_values (n):
	return -math.log10(n)
