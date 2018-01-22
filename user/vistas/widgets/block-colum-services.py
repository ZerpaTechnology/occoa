#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+=''''''
"""

#Ejemplo de uso de los parametros

data["widget"]["titulo"]="services"

data["widget"]["img"]=data['base_url']+"static/images/page-1_img01.jpg"

data["widget"]["content"]='''
<p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>'''

data["widget"]["list"]=[{"href":"#","service":"Lorem ipsum dolor sit amet","class":""},
                                        {"href":"#","service":"Conse ctetur adipisicing","class":""},
                                        {"href":"#","service":"Elit sed do eiusmod tempor","class":""},
                                        {"href":"#","service":"Incididunt ut labore","class":""},
                                        {"href":"#","service":"Et dolore magna aliqua","class":""},
                                        {"href":"#","service":"Ut enim ad minim veniam","class":""},
                                        {"href":"#","service":"Quis nostrud exercitation","class":""},
                                        {"href":"#","service":"Incididunt ut labore","class":""},
                                        {"href":"#","service":"Et dolore magna aliqua","class":""},
]

data["widget"]["btn"]={"href":"#","class":"btn","titulo":"Read more"

"""
doc+='''<div class="grid_4">                <h2>'''
try: doc+=str(data["widget"]["titulo"])
except Exception, e: doc+=str(e)
doc+='''</h2>                '''
try: doc+=str(data["widget"]["content"])
except Exception, e: doc+=str(e)
doc+='''                <ul class="marked-list">                '''
for elem in data["widget"]["list"]:
  doc+="""                  <li><a href='"""
  try: doc+=str(elem["href"])
  except Exception, e:   doc+=str(e)
  doc+="""' class='"""
  try: doc+=str(elem["class"])
  except Exception, e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str(elem["service"])
  except Exception, e:   doc+=str(e)
  doc+='''</a></li>                '''
  pass
doc+='''                </ul>                '''
if data["widget"]["btn"]!={}:
  doc+="""                                <a href='"""
  try: doc+=str(data["widget"]["btn"]["href"])
  except Exception, e:   doc+=str(e)
  doc+="""' class='"""
  try: doc+=str(data["widget"]["btn"]["class"])
  except Exception, e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str(data["widget"]["btn"]["titulo"])
  except Exception, e:   doc+=str(e)
  doc+='''</a>                '''
  pass
doc+='''              </div>'''