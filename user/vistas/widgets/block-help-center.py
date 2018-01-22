#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+=''''''
#dejar widget como encapsulado por defecto

data["widget"]={} 
doc+=''''''
data["widget"]["titulo"]="Help center"
doc+=''''''
data["widget"]["titulo-icon"]="fa-comment"
doc+=''''''
data["widget"]["infos"]=[{"titulo":"Ask professionals:",
                            "detalle":"""
                  <dl>
                    <dt>Monday - Friday:</dt>
                    <dd>8am-7pm</dd>
                  </dl>
                  <dl>
                    <dt>Saturday:</dt>
                    <dd>8am-5pm</dd>
                  </dl>
                  <dl>
                    <dt>Sunday:</dt>
                    <dd>1pm-5pm</dd>
                  </dl>
                            """},
                           {"titulo":"24/7 Online Support:",
                           "detalle":"""
                           <dl>
                            <dt>800-2345-6789</dt>
                          </dl>
                           """
                           },
]
doc+="""              <div class="grid_4">                <div class="info-box">                  <h2 class='"""
try: doc+=str(data["widget"]["titulo-icon"])
except Exception, e: doc+=str(e)
doc+="""'>"""
try: doc+=str(data["widget"]["titulo"])
except Exception, e: doc+=str(e)
doc+='''</h2>                  <hr>                                    '''
for k,elem in enumerate(data["widget"]["infos"]):
  doc+='''                    <h3>'''
  try: doc+=str(elem["titulo"])
  except Exception, e:   doc+=str(e)
  doc+='''</h3>                    '''
  try: doc+=str(elem["detalle"])
  except Exception, e:   doc+=str(e)
  doc+='''                  '''
  if k< len(data["widget"]["infos"])-1: 
    doc+='''                    <hr>                  '''
    pass
  doc+='''                  '''
  pass
doc+='''                                  </div>                <div class="owl-carousel">                                '''
data["widget"]["commits"]=[1,2]
doc+='''                '''
for elem in data["widget"]["commits"]:
  doc+='''                '''
  #data["widget"]=elem
  doc+='''                '''
  data["widget"]={} 
  doc+=''''''
  data["widget"]["img"]=data['base_url']+"static/images/page-1_img02.jpg" 
  doc+=''''''
  data["widget"]["commit"]="""<p>
<q>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore.</q>
</p>
<cite><a href="#">Incididunt ut labor</a></cite>"""
  doc+='''                                '''
  try: doc+=str(incluir(data,"block-commit"))
  except Exception, e:   doc+=str(e)
  doc+='''                '''
  pass
doc+='''                </div>              </div>'''