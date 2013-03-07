#!/usr/bin/python

from operator import itemgetter
import sys
def main():
	pageName=None
	pageID=None
	for line in sys.stdin:
		line=line.strip()
		try:
			line=line.split('\t')
			pageName=line[0]
			pageID=line[1]
			print '%s\t%s\t%s' % (pageName, pageID, '0')
		except:
			continue

if __name__=='__main__':
	main()