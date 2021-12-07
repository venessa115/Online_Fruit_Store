#!/usr/bin/env python3
import changeImage
import supplier_image_upload
import os
import requests
from os import listdir
import json
from collections import OrderedDict
import re

def upload(src_path):
        file_dict={}
        for filename in listdir(src_path):
                filepath=src_path+filename
                with open(filepath) as file:
                        fruit_name=file.readline()
                        weight=file.readline()
                        description=file.readlines()
                        weight=int(re.search(r'\d+', weight).group())
                        file_dict['name']=fruit_name.strip()
                        file_dict['weight']=weight
                        file_dict['description']=''.join(description).strip()
                        file_dict['image_name']=os.path.splitext(filename)[0]+'.jpeg'
                print(file_dict)
                response = requests.post("http://35.193.68.13/fruits/",data=file_dict)
                print("Status code: ", response.status_code)

if __name__=='__main__':
        upload('./supplier-data/descriptions/')

