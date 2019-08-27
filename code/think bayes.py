# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:08:20 2018

@author: QJ
"""

###Think Bayes
from thinkbayes2 import Pmf
pmf=Pmf()
for x in [1,2,3,4,5,6]:
    pmf.Set(x,1/6.0)
pmf.Set('Bowl1',0.5)
pmf.Set('Bowl2',0.5)
pmf.Mult('Bowl1',0.75)
pmf.Mult('Bowl2',0.5)
print pmf.Prob('Bowl 1')
print(pmf)
