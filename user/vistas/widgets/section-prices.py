#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<section class="well1">          <div class="container">            <h2 class="mobile-center">Price list</h2>            <div class="row">              <div class="grid_4">                '''
try: doc+=str(incluir(data,"table-prices"))
except Exception, e: doc+=str(e)
doc+='''              </div>              <div class="grid_4">                '''
try: doc+=str(incluir(data,"table-prices"))
except Exception, e: doc+=str(e)
doc+='''              </div>              <div class="grid_4">                '''
try: doc+=str(incluir(data,"table-prices"))
except Exception, e: doc+=str(e)
doc+='''              </div>            </div>          </div>        </section>'''