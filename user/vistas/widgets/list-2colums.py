#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+=''''''
data["widget"]={} 

data["widget"]["list"]=[{"href":"#","titulo":"Praesent vestibulum molestie"},
                          {"href":"#","titulo":"Praesent vestibulum molestie"},
                          {"href":"#","titulo":"Praesent vestibulum molestie"},
                          {"href":"#","titulo":"Praesent vestibulum molestie"},
]
doc+='''<div class="row off4">  <div class="grid_3">    <ul class="marked-list wow fadeInRight">      '''
k=0
doc+='''      '''
while k< (len(data["widget"]["list"])/2):
  doc+="""      <li><a href='"""
  try: doc+=str(data["widget"]["list"][k]["href"])
  except Exception, e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str(data["widget"]["list"][k]["titulo"])
  except Exception, e:   doc+=str(e)
  doc+='''</a></li>      '''
  k+=1
  doc+='''      '''
  pass
doc+='''                </ul>  </div>  <div class="grid_3">    <ul data-wow-delay="0.2s" class="marked-list wow fadeInRight">    '''
while k< len(data["widget"]["list"]):
  doc+="""      <li><a href='"""
  try: doc+=str(data["widget"]["list"][k]["href"])
  except Exception, e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str(data["widget"]["list"][k]["titulo"])
  except Exception, e:   doc+=str(e)
  doc+='''</a></li>      '''
  k+=1
  doc+='''      '''
  pass
doc+='''    </ul>  </div></div>'''