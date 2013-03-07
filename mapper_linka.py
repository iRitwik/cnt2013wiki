#!/usr/bin/python
import sys, string, re
def main():
	fromID=None
	toID=None
	for line in sys.stdin:
		line=line.strip()
		try:
			line=line.split('\t')
			fromID=line[0]
			toID=line[1]
			print '%s\t%s' % (fromID, toID)
		except:
			continue
if __name__=='__main__':
	main()
