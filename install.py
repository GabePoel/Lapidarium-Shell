import os
import sys

home = os.path.expanduser("~")
insdir = os.getcwd()
tardir = os.path.join(home, ".local", "share", "themes")

def link():
    #if not os.path.exists(os.path.join(tardir, name)):
        #os.makedirs(os.path.join(tardir, name))
    os.system("ln -sf '" + insdir + "' " + tardir)

def move():
    os.system("mvdir '" + insdir + "' " + tardir)

if len(sys.argv) == 1:
    raise ValueError("No input provided.\nPlease specify either 'link' or 'move'.")
if sys.argv[1] == "link":
    if not os.path.exists(tardir):
        os.mkdir(tardir)
    link()
elif sys.argv[1] == "move":
    if not os.path.exists(tardir):
        os.mkdir(tardir)
    move()
else:
    raise ValueError("Invalid input provided.\nPlease specify either 'link' or 'move'.")
