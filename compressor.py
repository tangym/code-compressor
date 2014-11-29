__author__ = 'TYM'

import ply

def js(file_name, encoding='utf8'):
    '''opens the file, compress it, and returns the compressed string'''
    s = ''
    with open(file_name, encoding=encoding) as f:
        for l in f:
            if '//' in l:
                l = l.split('//')[0].strip()
            elif '/*' in l:

