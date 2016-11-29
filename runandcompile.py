#!/usr/bin/env python

import sys
import os
import getopt

def main(argv):
	filenameList = argv
	filename = filenameList[0]
	print(filename)
	os.system("pwd")
	os.system("gcc "+str(filename))
	os.system("./a.out")



if __name__ == "__main__":
	main(sys.argv[1:])