#!/usr/bin/python
import sys, string, re
def main():
	for line in sys.stdin:
		if (line.startswith('INSERT INTO')):
			records=re.compile('\((.*?),(.*?),\'(.*?)\',\'(.*?)\',(.*?),(.*?),(.*?),(.*?),\'(.*?)\',(.*?),(.*?)\)', re.DOTALL |  re.IGNORECASE).findall(line)
			for record in records:
				try:
					pg_id=int(record[0])
					ns=record[1]
					pageName=repr(record[2])
					if ns=='0':
						print "%s\t%d" % (pageName, pg_id)
					del pg_id, ns, pageName
				except Exception as e:
					continue
if __name__=='__main__':
	main()
