#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<section>          <div class="container banner_wr">                       <ul class="banner">              '''
if "block-services" in data:
  doc+='''              '''
  for elem in data["block-services"]:
    doc+='''              '''
    data["elem"]=elem
    doc+='''              '''
    try: doc+=str(incluir(data,"block-service"))
    except Exception, e:     doc+=str(e)
    doc+='''              '''
    pass
  doc+='''              '''
  pass
doc+='''                          </ul>          </div>        </section>'''