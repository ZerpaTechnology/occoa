#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+=''''''
data["widget"]["titulo"]="Our awards"

data["widget-bg-color"]="red"
doc+=''''''
data["widget-color"]="white"
doc+=''''''
data["widget-title-color"]="white"
doc+=''''''
'''

#EJEMPLO DE USO DE los parametros

data["widget"]["titulo"]="Our awards"

data["widget"]["call-to-actions"]=[
            {"icon":"icon fa-comments","content":"""<h3><a href="#">Incididunt ut labore et dolore</a></h3>
                    <p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolor.</p>"""},
            {"icon":"icon fa-comments","content":"""<h3><a href="#">Incididunt ut labore et dolore</a></h3>
                    <p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolor.</p>"""},
            {"icon":"icon fa-comments","content":"""<h3><a href="#">Incididunt ut labore et dolore</a></h3>
                    <p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolor.</p>"""},
            {"icon":"icon fa-comments","content":"""<h3><a href="#">Incididunt ut labore et dolore</a></h3>
                    <p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolor.</p>"""},
                    ] 

'''
doc+='''<section class="well ins1" style="background-color:'''
try: doc+=str(data['widget-bg-color'])
except Exception, e: doc+=str(e)
doc+=''';color:'''
try: doc+=str(data['widget-color'])
except Exception, e: doc+=str(e)
doc+='''">          <div class="container hr" >        '''
if "titulo" in data["widget"]:
  doc+='''          <h2 style="color:'''
  try: doc+=str(data['widget-title-color'])
  except Exception, e:   doc+=str(e)
  doc+='''">'''
  try: doc+=str(data["widget"]["titulo"])
  except Exception, e:   doc+=str(e)
  doc+='''</h2>          '''
  pass
doc+='''                <ul class="row product-list">                '''
widget=data["widget"]
doc+='''                '''
for k,elem in enumerate(widget["call-to-actions"]):
  doc+='''                                <li class="grid_6">                '''
  data["widget"]=elem
  doc+='''                '''
  data["widget"]['widget-title-color']=data['widget-title-color']
  doc+='''                '''
  try: doc+=str(incluir(data,"call-to-action"))
  except Exception, e:   doc+=str(e)
  doc+='''                '''
  if k!=len(widget["call-to-actions"])/2 and k!=len(widget["call-to-actions"])-1:
    doc+='''                <hr>                '''
  elif k==len(widget["call-to-actions"])/2:
    doc+='''                </li>                <li class="grid_6">                '''
    pass
  doc+='''                </li>                '''
  pass
doc+='''                </ul>          </div>        </section>'''