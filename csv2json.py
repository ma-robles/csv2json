from sys import argv
import csv

filename = argv[1]
data={}
names = []
with open(filename) as pfile:
    csvreader = csv.reader(pfile, delimiter=',')
    for i,line in enumerate(csvreader):
        if (i==0):
            for j,d in enumerate(line):
                data[d]=[]
                names.append(d)

        else:
            for j,d in enumerate(line):
                if (j!=0):
                    if (d==''):
                        data[names[j]].append(0.0)
                    else:
                        data[names[j]].append(float(d))
                else:
                    data[names[j]].append(d.replace(' ','T'))

with open(filename.split('.')[0]+'.json', 'w') as pfile:
    print(data, file=pfile)
