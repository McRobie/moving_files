""" 
author: Ryan McRobie
This script was created to make directories based off of file names.
Then move those files into the corresponding directory based off of their file name.
"""

import os
import shutil

# place your absolute file path here.
working_directory = "absolute path"

# changes to the working directory and creates the variable 'contents' of your absolute path.
os.chdir(working_directory)
contents = os.listdir(os.getcwd())

# main function call that takes contents as an argument. 
def creating(contents):
	# Loops through the items in the directory.
	for item in contents:
		# if the item in the directory is a file execute this block.
		if os.path.isfile(item):
			# you can use the slicing technique to create a new directory from the name of the file.
			is_dir(item[13:])
			# this function moves that item from the list into the directory that it created for the file.
			move(item)

# if the directory doesn't exist for the file evaluated then create a directory of the item[splice].
def is_dir(ext):
	if os.path.isdir(ext) == False:
		os.mkdir("./%s" % ext)

# moves the file/item into the directory of the indicated item[splice].
def move(file):
	dir = file[13:]	
	shutil.move('./%s' % (file),'./%s/%s' % (dir,file))
				

creating(contents)
