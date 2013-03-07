#!/usr/bin/python python

def main():
	f=open('links-simple-sorted.txt')
	line=f.readline()
	while(line!=''):
		record=line.split(':')
		print record[0]+' '+'1'+record[1],
		line=f.readline()


if __name__=='__main__':
	main()