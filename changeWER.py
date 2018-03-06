import sys
import re

tex=sys.argv[1]
out=sys.argv[2]
#& 0.588 & 3.245 & 0.976 &  0.354 & 2.51 & 0.942
#Closest cluster next UBT & 0.685 & 1.30 & 0.019 & 0.532 & 1.14 & 0.075 \\
#PHOC vectors 50\%  & 0.458 & 14.85 & 0.984 &  0.386 & 13.88 & 0.957 \\
with open(tex) as f:
    with open(out,'w') as o:
        for line in f.readlines():
            m = re.search(r'(.+& +\d+\.\d+ +& +\d+\.\d+ +& +)(\d+\.\d+)( +& +\d+\.\d+ +& +\d+\.\d+ +& +)(\d+\.\d+)(.+)',line)
            if m:
                o.write(m.group(1)+str(1.0-float(m.group(2)))+m.group(3)+str(1.0-float(m.group(4)))+m.group(5)+'\n')
            else:
                o.write(line)
