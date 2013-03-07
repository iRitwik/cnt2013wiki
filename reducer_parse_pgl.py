#!/usr/bin/python

from operator import itemgetter
import sys
def main():
	pageTo=None
	fromID=None
	for line in sys.stdin:
		line=line.strip()
		try:
			line=line.split('\t')
			pageTo=line[0]
			fromID=line[1]
			print '%s\t%s\t%s' % (pageTo, fromID, '1')
		except:
			continue

if __name__=='__main__':
	main()