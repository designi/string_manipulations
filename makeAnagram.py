# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:08:42 2020

@author: ngarcia
"""
import pandas as pd

def makeAnagram(a,b):
    """Returns the minimum total characters that must be deleted to make a and b anagrams of each other"""

    excluded = [i for i in set(a) if i not in set(b)]
    excluded1 = [i for i in set(b) if i not in set(a)]
    lst = excluded+excluded1
    
    cnt_rem_a = 0
    cnt_add_a = 0
    new_str = ''
    cnt_rem_b = 0
    cnt_add_b = 0
    new_str1 = ''

    for i in a:
        if i not in lst:
            new_str = new_str + i
            cnt_add_a += 1
        else:
            cnt_rem_a += 1
    n = list(new_str)
    n.sort()
    r_str = ''.join(n)
    
    for i in b:
        if i not in lst:
            new_str1 = new_str1 + i
            cnt_add_b += 1
        else:
            cnt_rem_b += 1
    n1 = list(new_str1)
    n1.sort()
    r_str1 = ''.join(n1)
    
    zipped = zip(list(r_str),list(r_str1))
    tups = list(zipped)
    
    
    df1 = pd.DataFrame(tups,columns=['l1','l2']).groupby('l1').count()
    df2 = pd.DataFrame(tups,columns=['l1','l2']).groupby('l2').count()
    
    mdf = pd.merge(df1,df2,left_on='l1',right_on='l2',how='left',right_index=True)
    mdf.index.name = 'index'
    mdf.fillna(0,inplace=True)
    mdf['l3']=abs(mdf['l2'] - mdf['l1'])
    final_exclude  = sum(mdf['l3'])
    min_char_del = final_exclude +cnt_rem_b+cnt_rem_a
    return min_char_del 
