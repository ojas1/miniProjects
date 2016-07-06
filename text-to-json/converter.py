import json
from collections import OrderedDict
from io import FileIO

def convert():
 fp=open('sample.txt')
 raw=fp.read()
 fp.close()
 filter1=raw.split('\n')
 filter2=[i for i in filter1 if i!='']
 
 filter3=[
  [filter2[i], filter2[i+1], filter2[i+2]] 
  for i in xrange(0,len(filter2),3)
 ]

 filter4=[
  [col.replace(': ', ':').split(':') 
  for col in row] for row in filter3
 ]
 filter5=[OrderedDict(row) for row in filter4]
 try: jfp=open('sample.json', 'w')
 except:
  jfp=FileIO('sample.json', 'w')
 jfp.truncate()
 json.dump(filter5, jfp, indent=4)
 jfp.close()

if __name__=='__main__':
 convert()
