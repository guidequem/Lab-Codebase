import shutil
from os import listdir
from os.path import isfile, join

mainDir = "C:\\Users\\markertlab\\Desktop"
mainDir = r"C:\\Users\\ifeel\\Desktop"
copyDir = r"C:\\Users\\ifeel\Box\\Test Backup\\Back"

shutil.copytree(mainDir,copyDir)


