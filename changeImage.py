#!/usr/bin/python3

from PIL import Image
from os import listdir

def changeImage(path):
	for filename in listdir(path):
		filepath=path+filename
		im=Image.open(filepath).convert('RGB')
		width,height=im.size
		if width!=600  and height!=400:
			im.resize((600,400)).save(path+filename,'JPEG')

if __name__=='__main__':
	changeImage('./supplier-data/images/')

