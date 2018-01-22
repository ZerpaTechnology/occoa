#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html><html lang="en">  '''
try: doc+=str(incluir(data,"head"))
except Exception, e: doc+=str(e)
doc+='''  <body>    <div class="page">      <!--      ========================================================      							HEADER      ========================================================                  -->      '''
try: doc+=str(incluir(data,"header2"))
except Exception, e: doc+=str(e)
doc+='''      <!--      ========================================================                                  CONTENT      ========================================================      -->      <main>        <section class="well1 ins2 mobile-center">          <div class="container">            <h2>The best business services</h2>            <div class="row off2">              '''
try: doc+=str(incluir(data,"blog-article"))
except Exception, e: doc+=str(e)
doc+='''              '''
try: doc+=str(incluir(data,"blog-article"))
except Exception, e: doc+=str(e)
doc+='''              '''
try: doc+=str(incluir(data,"blog-article"))
except Exception, e: doc+=str(e)
doc+='''            </div>            <hr>            <div class="row">              '''
try: doc+=str(incluir(data,"blog-article"))
except Exception, e: doc+=str(e)
doc+='''              '''
try: doc+=str(incluir(data,"blog-article"))
except Exception, e: doc+=str(e)
doc+='''              '''
try: doc+=str(incluir(data,"blog-article"))
except Exception, e: doc+=str(e)
doc+='''            </div>          </div>        </section>        '''
try: doc+=str(incluir(data,"section-how-we-can-help"))
except Exception, e: doc+=str(e)
doc+='''        '''
try: doc+=str(incluir(data,"section-prices"))
except Exception, e: doc+=str(e)
doc+='''      </main>      <!--      ========================================================                                  FOOTER      ========================================================      -->      '''
try: doc+=str(incluir(data,"footer"))
except Exception, e: doc+=str(e)
doc+='''    </div>    <script src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''static/js/script.js"></script>  </body></html>'''