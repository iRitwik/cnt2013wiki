#!/usr/bin/python
import sys
def main():
	for line in sys.stdin:
	    # remove leading and trailing whitespace
	    line = line.strip()
	    words = line.split()
	    fromNode=words[0]
	    pageRank=words[1]
	    words=words[2:]
	    outLinks=len(words)
	    outLinks=str(outLinks)
	    if outLinks==0:
	    	outLinks=1
	    for toNode in words:
	    	print '%s\t%s\t%s\t%s' % (toNode, fromNode, pageRank, outLinks)
	    del words, fromNode, pageRank, words, outLinks
if __name__=='__main__':
	main()
