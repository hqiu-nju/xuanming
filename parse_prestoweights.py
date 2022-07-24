import numpy as np
import sys

filename=sys.argv[1]
splitband=int(sys.argv[2]) ### this is the channel you want to split the band
print(filename)
w=open(filename,'r')
strings=w.readlines()[0][:-1]  ### -1 to remove \n
print(strings)
print('parsing the file')
w.close()
indexes=strings.split(',')
w=open(f'{filename}_b1.flags','w')
w2=open(f'{filename}_b2.flags','w')

for chans in indexes:
    flags=chans.split(":")
    print(flags)
    if len(flags)<2:
        flaglist=int(flags[0])
        if flaglist>splitband:
            flaglist=flaglist-splitband
            w2.write(f'{flaglist}\n')
        else:
            w.write(f'{flaglist}\n')
        print(f'{flaglist}')

    else:
        a1=int(flags[0])
        a2=int(flags[1])
        if a1>splitband:
            a1=a1-splitband
            a2=a2-splitband
            flaglist=np.arange(a1,a2+1)
            for idx in flaglist:
                w2.write(f"{idx}\n")
                print(f"{idx}")
        else:
            flaglist=np.arange(a1,a2+1)
            for idx in flaglist:
                w.write(f"{idx}\n")
                print(f"{idx}")
w.close()
w2.close()
