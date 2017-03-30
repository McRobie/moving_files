""" 
author: Ryan McRobie
This script was created to make directories based off of file names.
Then move those files into the corresponding directory based off of their file name.
"""

import os
import shutil

# place your absolute file path here.
working_directory = "/mnt/c/Users/rmcrobie/Desktop/test"

os.chdir(working_directory)
contents = os.listdir(os.getcwd())

def creating(contents):
	for item in contents:
		if os.path.isfile(item):
			is_dir(item[13:])
			move(item)

def is_dir(ext):
	if os.path.isdir(ext) == False:
		os.mkdir("./%s" % ext)

def move(file):
	dir = file[13:]	
	shutil.move('./%s' % (file),'./%s/%s' % (dir,file))
				

creating(contents)
