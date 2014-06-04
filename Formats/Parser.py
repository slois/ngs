from Formats import Bed
from Formats import encodePeak
from Formats import broadPeak
import gzip


_FormatToParser = { 	'bed': Bed.RecordParser(),
			'encodePeak': encodePeak.RecordParser(),
			'broadPeak': broadPeak.RecordParser() }

_FormatToIterator = { 	'bed': Bed.Iterator,
			'encodePeak': encodePeak.Iterator,
			'broadPeak': broadPeak.Iterator }


class Parser(object):
	def __init__(self, mfile, mformat, compressed=False):
		self.file = mfile
		self.format = mformat
		self.compressed = compressed

		self.__handle = None
		self.__parser =	None
		self.__iterator = None
	
		self.initialize()
	
	def __end__(self):
		print "CLOSED"
		self.__handle.close()
		
	def initialize (self):

		if self.format in _FormatToParser:
			self.__parser = _FormatToParser[self.format]
			self.__iterator = _FormatToIterator[self.format]
		else:
			raise ValueError("Unknown format '%s'" % (self.format))	
		
		try:
			if self.compressed == True:
				self.__handle = gzip.open(self.file)
				
			else:
				self.__handle = open(self.file, 'r')
		except IOError:
			raise IOError("File not found '%s'" % (self.file))

	def read (self, intersect=False):
		return self.__iterator(self.__handle, self.__parser, intersect)

	def getHandle (self):
		return self.__handle

	def getParser (self):
		return self.__parser

	def getIterator (self):
		return self.__iterator


class Format(Parser):
	def __init__ (self, mfile, mformat):
		self.file = mfile
		self.format = mformat
		super(Format, self).__init__(self.file, self.format)
		
	def __repr__ (self):
		return "%s|%s" % (self.format, self.version)
