#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+=''''''
data["widget"]={} 

data["widget"]["icon"]="icon2 fa-map-marker" 
doc+=''''''
data["widget"]["info"]="""
<address>4578 Marmora Road,Glasgow<br/> D04 89GR</address>
"""
doc+='''<div class="box">                  <div class="box_aside">                    <div class="'''
try: doc+=str(data['widget']['icon'])
except Exception, e: doc+=str(e)
doc+='''"></div>                  </div>                  <div class="box_cnt__no-flow">                  '''
try: doc+=str(data["widget"]["info"])
except Exception, e: doc+=str(e)
doc+='''                                      </div>                </div>'''