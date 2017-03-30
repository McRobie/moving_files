import os
import shutil


def checkFolders(contents):
        for item in contents:
                if os.path.isdir(item):
                        drillDirDown(item)
                        for file in os.listdir(os.getcwd()):
                                fileExt = file[13:]
                                if fileExt != item:
                                        moveFileUp(file)
                        moveDirUp()

def drillDirDown(dir):
        os.chdir("./%s" % dir)

def moveDirUp():
        os.chdir("../")

def moveFileUp(file):
        dir = file[13:]
        shutil.move('./%s' % (file),'../')


#absolute file path here.
working_directory = "/opt/mounts/Customer/quarantine/footfall/"

os.chdir(working_directory)
contents = os.listdir(os.getcwd())

checkFolders(contents)
