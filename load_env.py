from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except:
    from yaml import Loader, Dumper

from pathlib import Path

from dotenv import dotenv_values

p = Path('../env')
q = p / '.env'
config = None 

with open(q, 'r') as f:
    config = dotenv_values(stream=f)

# print(q.resolve())
# with open(q, 'r') as f:
#     loader = load(f, Loader=Loader)
#     config = loader

print(config['exchange'])
