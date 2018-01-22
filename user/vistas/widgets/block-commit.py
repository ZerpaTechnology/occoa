#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+=''''''
'''

#Ejemplo de los parametros

data["widget"]={} 

data["widget"]["img"]=data['base_url']+"static/images/page-1_img02.jpg" 

data["widget"]["commit"]="""<p>
<q>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore.</q>
</p>
<cite><a href="#">Incididunt ut labor</a></cite>"""

'''
doc+='''<div class="item">  <blockquote class="box">    <div class="box_aside"><img src="'''
try: doc+=str(data['widget']['img'])
except Exception, e: doc+=str(e)
doc+='''" alt=""></div>    <div class="box_cnt__no-flow">      '''
try: doc+=str(data["widget"]["commit"])
except Exception, e: doc+=str(e)
doc+='''    </div>  </blockquote></div>'''