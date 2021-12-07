#!/usr/bin/env python3
import requests
from os import listdir

def image_upload(src_path):
        url="http://35.193.68.13/upload/"
        for filename in listdir(src_path):
                filepath=src_path+filename
                with open(filepath,'rb') as file:
                        r=requests.post(url,files={'file':file})

if __name__=='__main__':
       image_upload('./supplier-data/images/')
