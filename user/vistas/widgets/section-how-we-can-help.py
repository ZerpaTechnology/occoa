#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+=''''''
data["widget"]={} 

data["widget"]["content"]="""
<h2>How we can help?</h2>
                <p>Curabitur pellentesque, turpis sit amet iaculis condimentum, urna mi aliquet turpis, itae pharetra mauris eros non arcu. Aenean felis augue, dignissim in tempus eget, cursus sit amet sem? Cras vehicula vehicula nunc id fringilla?</p>
"""

doc+='''<section class="well1 ins4 bg-image">          <div class="container">            <div class="row">              <div class="grid_7 preffix_5">                '''
try: doc+=str(data["widget"]["content"])
except Exception, e: doc+=str(e)
doc+='''              '''
try: doc+=str(incluir(data,"list-2colums"))
except Exception, e: doc+=str(e)
doc+='''              </div>            </div>          </div>        </section>'''