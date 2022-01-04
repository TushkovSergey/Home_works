import re
string = '''The rte manufacturer of professional 3D printers Sintratec has released a software solution called Nesting, which allows for automatic placement of models in additive systems based on selective laser sintering (SLS) technology with optimal use of the build volume.'''
keywords  = {'rte'}
def find_match(string, keywords):
     string_splitted = re.split(r'[/ /,/(/)/.]', string.lower())
     string_set = set(string_splitted)
     if string_set & keywords:
          return 'true'
     else:
          return 'false'

find_match(string, keywords)




