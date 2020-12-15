# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:12:10 2020
@author: ngarcia
"""

def proper(string):
    """Capitalizes the first letter of every word.
       Overcomes limitations of .title()"""
    if isinstance(string,str):
        res = []
        lst = string.split()
        for word in lst:
            r=''
            for i,l in enumerate(word):
                if l.isalpha():
                    res.append(r + l.upper() + word[i+1:].lower())
                    break
                r+=l
            if r not in lst:
                continue
            res.append(r)
        return ' '.join(res)
    raise TypeError('type must be string, not {}'.format(type(string).__name__))
