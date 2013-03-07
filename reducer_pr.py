#!/usr/bin/python

from operator import itemgetter
import sys
def main():
	current_node = None
	current_pageRank = 0.0
	node = None
	for line in sys.stdin:
		line = line.strip()
		try:
			words=line.split('\t')
			node=words[0]
			fromNode=words[1]
			from_pageRank=float(words[2])
			outLinks=float(words[3])
		except ValueError:
			continue
		if current_node == node:
			current_pageRank +=  (from_pageRank/outLinks)
		else:
			if current_node:
				print '%s\t%f' % (current_node, current_pageRank*0.85+0.15)
			current_pageRank = from_pageRank
			current_node = node
	if current_node == node:
		print '%s\t%f' % (current_node, current_pageRank*0.85+0.15)

if __name__=='__main__':
	main()

