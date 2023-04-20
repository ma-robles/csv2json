from sys import argv

filename = argv[1]
data=[]
with open(filename) as pfile:
    for i,line in enumerate(pfile):
        if (i!=0):
            for j,d in enumerate(line.split(',')):
                data.append
                if (j!=0):

