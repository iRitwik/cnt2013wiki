#!/usr/bin/python

from operator import itemgetter
import sys
def main():
	fromID=None
	toID=None

	current_fromID=None
	toIDList=[]
	for line in sys.stdin:
		line=line.strip()
		try:
			line=line.split('\t')
			fromID=line[0]
			toID=line[1]
		except:
			continue
		if current_fromID==fromID:
			toIDList.append(toID)
		else:
			if current_fromID is not None:
				print current_fromID+'\t'+'\t'.join(toIDList)
			current_fromID=fromID
			toIDList=[toID]
	if current_fromID==fromID:
		print current_fromID+'\t'+'\t'.join(toIDList)
if __name__=='__main__':
	main()


