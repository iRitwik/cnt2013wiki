#!/usr/bin/python

from operator import itemgetter
import sys
def main():
	pageName=None
	pageID=None
	key_act=None
	
	current_Name=None
	fromID=[]
	toID=None
	for line in sys.stdin:
		line=line.strip()
		try:
			line=line.split('\t')
			pageName=line[0]
			pageID=line[1]
			key_act=line[2]
		except:
			continue
		if current_Name==pageName:
			if key_act=='0':
				toID=int(pageID)
			else:
				fromID.append(int(pageID))
		else:
			if current_Name is not None:
				for frmID in fromID:
					print '%d\t%d' % (frmID, toID)
			current_Name=pageName
			if key_act=='0':
				toID=int(pageID)
			else:
				fromID=[int(pageID)]
	if current_Name==pageName:
		for frmID in fromID:
			print '%d\t%d' % (frmID, toID)			
if __name__=='__main__':
	main()