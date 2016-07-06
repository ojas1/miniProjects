import string 
import random
from io import FileIO
import sys

def genrandstr(len):
 return ''.join(random.choice(string.lowercase) for i in range(len))

def getName():
 return ' '.join([
  genrandstr(random.randint(5,8)), genrandstr(random.randint(5,8))
 ])

def genrandDigs(len):
 return ''.join(random.choice(string.digits) for i in range(len))

def getBal():
 return '.'.join([
  genrandDigs(random.randint(4,6)), genrandDigs(2)
 ])

def getId(ids):
 id=genrandDigs(3)
 while id in ids:
  id=genrandDigs(3)
 ids.append(id)
 return id

def getRec():
 ids=[]
 id=getId(ids)
 name=getName()
 bal=getBal()
 return [id,name,bal]

def getTable(len):
 return [getRec() for i in xrange(len)]

def createFile(size):
 headers=['Id', 'Name', 'Balance']
 try: fp=open('sample.txt', 'w')
 except:fp=FileIO('sample.txt','w')
 fp.truncate()
 table=getTable(size)
 for row in table:
  i=0
  for item in row:
   readyItem=headers[i]+':'+item+'\n'
   i+=1
   fp.write(readyItem)
  fp.write('\n')
 fp.close()

if __name__=='__main__':
 createFile(int(sys.argv[1]))
