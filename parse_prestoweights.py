import numpy as np
import sys

filename=sys.argv[1]
print(filename)
w=open(filename,'r')
strings=w.readlines()[0][:-1]  ### -1 to remove \n
print(strings)
print('parsing the file')
w.close()
indexes=strings.split(',')
w=open(f'{filename}.flags','w')
for chans in indexes:
    flags=chans.split(":")
    print(flags)
    if len(flags)<2:
        w.write(f'{flags[0]}\n')
        print(f'{flags[0]}')

    else:
        a1=int(flags[0])
        a2=int(flags[1])
        flaglist=np.arange(a1,a2+1)
        for idx in flaglist:
            w.write(f"{idx}\n")
            print(f"{idx}")
w.close()
