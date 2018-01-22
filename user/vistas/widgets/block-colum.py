#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+=''''''
"""

#Ejemplo de uso de los parametros

data["widget"]["titulo"]="About"

data["widget"]["img"]=data['base_url']+"static/images/page-1_img01.jpg"

data["widget"]["content"]='''
<p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatu. Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt. Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p><a href="#" class="btn">Read more</a>
'''

"""
doc+='''<div class="grid_4"><h2>'''
try: doc+=str(data["widget"]["titulo"])
except Exception, e: doc+=str(e)
doc+="""</h2><img src='"""
try: doc+=str(data["widget"]["img"])
except Exception, e: doc+=str(e)
doc+="""' alt="">"""
try: doc+=str(data["widget"]["content"])
except Exception, e: doc+=str(e)
doc+='''</div>'''