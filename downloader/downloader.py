from os import path, system
from urllib import urlretrieve
from time import sleep
from sys import stdout, argv

_PREVPERCENT=100

def status_update(content_length):
 global _PREVPERCENT
 content_downloaded = path.getsize('somevid')
 percent_remaining = (content_length - content_downloaded)*100/content_length
 if _PREVPERCENT!=percent_remaining:
  #stdout.write('PROGRESS: '+str(100-percent_remaining)+'%'+'\r')
  if percent_remaining%10==0:
   stdout.write('==')
   stdout.flush()
  sleep(0.01)
 _PREVPERCENT=percent_remaining


def routine_call(block_count, block_size, content_length):
 if content_length==-1:
  print "content-length not available, unable to updata status"
  return
 status_update(content_length)

def download(inp):
 system('setterm -cursor off')
 print "\nPROGRESS:"
 stdout.write('                       ]\r[ ') 
 response = urlretrieve(
  'file:///home/ojas/Downloads/720P_1500K_68295501.mp4',
  'somevid',routine_call)
 stdout.write(' ] Download Complete! \n\n')
 system('setterm -cursor on')

if __name__=='__main__':
 download(argv[1:])
