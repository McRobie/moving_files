""" 
author: Ryan McRobie

This script was created to make directories based off of file names.
Then move those files into the corresponding directory based off of their file name.
"""

import os
import shutil

# place your absolute file path here.
working_directory = "absolute file path goes here."

os.chdir(working_directory)
contents = os.listdir(os.getcwd())

true_files = []
files = []
dirs = []

def create_files_list(contents):
	for item in contents:
		if os.path.isfile(item) == True:
			true_files.append(item)
			parsed_item = item[5:]
			files.append(parsed_item)

def make_dirs_of_files(files):
	for item in files:
		if os.path.isdir(item) == False:
			os.mkdir("./%s" % item)

def get_dirs_list(contents):
	for item in contents:
		if os.path.isdir(item):
			dirs.append(item)

def move_files():
	for file in files:
		pass

def get_listing(files, dirs):
	for fi, di in zip(true_files, dirs):
		if fi[5:] in dirs:
			shutil.move('./%s' % (fi),'./%s/%s' % (di,fi))


create_files_list(contents)

get_dirs_list(contents)

make_dirs_of_files(files)

get_listing(files, dirs)
