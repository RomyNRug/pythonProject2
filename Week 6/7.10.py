#Write a program that reads a file and writes out a new file with the lines in reversed order (i.e. the first line inthe old file becomes the last one in the new file.)

#1

def filter(normafile,reversefile):
with open(normalfile,"r") as infile, open(reversefile,"w") as outfile:
    f= open(reversefile, "w")
    lines= f.readlines()
    for lines in reversefile:





def filter(oldfile, newfile):
2 with open(oldfile, "r") as infile, open(newfile, "w") as outfile:
3 for line in infile:
4 # Put any processing logic here
5 if not line.startswith('#'):
6 outfile.write(line)
