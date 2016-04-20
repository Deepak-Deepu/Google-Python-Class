#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  list2=[]
  list3=[]
  ufile = urllib.urlopen(filename)
  info = ufile.info()
  if info.gettype() == 'application/x-msdos-program':
  	string =ufile.geturl()
        string=string[7:]
        string='http://'+string
        text = ufile.read()
        list1= re.findall('/[\w/.-]+jpg',text)
        for i in list1:
        	if i not in list2:
                	list2.append(i)

#               list2.sort()
#               return list2
        for i in list2:
        	list3.append(string+i)
#               return list3
        list10=[]
	string1=""
        list10=sorted(list3,key=lambda x:x[-8:-4])
        return list10

  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  list4=[]
  var=os.path.exists(dest_dir)
  if not var:
  	os.makedirs(dest_dir)

#  list4=img_urls
  
  j=0
  for i in img_urls:
  	filename=os.path.join(os.path.abspath(dest_dir),'img'+str(j))
        j=j+1
	print 'Retrieving...',i
        urllib.urlretrieve(i, filename)

  filename=os.path.join(os.path.abspath(dest_dir),'index.html')
  f=open(filename,'w')

  f.write("<verbatim><html><body><img src='img0'><img src='img1'><img src='img2'><img src='img3'><img src='img4'><img src='img5'><img src='img6'><img src='img7'><img src='img8'><img src='img9'><img src='img10'><img src='img11'><img src='img12'><img src='img13'><img src='img14'><img src='img15'><img src='img16'><img src='img17'><img src='img18'><img src='img19'></body></html>")

  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
