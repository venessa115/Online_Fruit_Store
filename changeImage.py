#!/usr/bin/env python3
from PIL import Image
from os import listdir
import os

def changeImage(path):
   for filename in listdir(path):
      filepath=path+filename
      if filename.endswith((".tiff")):
         im=Image.open(filepath).convert('RGB')
         width,height=im.size
         if width!=600 or  height!=400 or filename.endswith((".tiff")):
            filename=os.path.splitext(filename)[0]+'.jpeg'
            im.resize((600,400)).save(path+filename,'JPEG')
            os.remove(path+os.path.splitext(filename)[0]+'.tiff')

if __name__=='__main__':
   changeImage('./supplier-data/images/')
