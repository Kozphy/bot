from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except:
    from yaml import Loader, Dumper

from pathlib import Path


p = Path('../env')
q = p / 'config.yaml'
