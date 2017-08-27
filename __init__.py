import os
import pandas as pd
import pickle 
from os.path import dirname, exists, join

#module_dir = dirname(__file__)
#repo = 'git@github.com:jehoons/downloader.git'

#if not exists(join(module_dir, 'downloader')): 
#    os.system('git clone %s %s/downloader' % (repo, module_dir))

from downloader import _downloader


def return_loader(): 
    _baseurl = 'http://143.248.32.25/~jhsong/dataset/Perturbation/DRIVE'
    # return _downloader(_baseurl+'/DriveCountData.RDS')
    return _downloader(_baseurl+'/DriveCountData.pkl')


def load():
    with open(return_loader().find(), 'rb') as f:  
        return pickle.load(f) 

        
