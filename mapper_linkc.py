#!/usr/bin/python
import sys, string, re
def main():
	pageName=None
	pageID=None
	key_act=None
	for line in sys.stdin:
		line=line.strip()
		try:
			line=line.split('\t')
			pageName=line[0]
			pageID=line[1]
			key_act=line[2]
			print '%s\t%s\t%s' % (pageName, pageID, key_act)
		except:
			continue
if __name__=='__main__':
	main()
