#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html><html lang="en">  '''
try: doc+=str(incluir(data,"head"))
except Exception, e: doc+=str(e)
doc+='''  <body>    <div class="page">      <!--      ========================================================      							HEADER      ========================================================                  -->      '''
try: doc+=str(incluir(data,"header2"))
except Exception, e: doc+=str(e)
doc+='''      <!--      ========================================================                                  CONTENT      ========================================================      -->      <main>        '''
try: doc+=str(incluir(data,"map"))
except Exception, e: doc+=str(e)
doc+='''        '''
try: doc+=str(incluir(data,"subFooter"))
except Exception, e: doc+=str(e)
doc+='''        '''
try: doc+=str(incluir(data,"contact-form"))
except Exception, e: doc+=str(e)
doc+='''      </main>      <!--      ========================================================                                  FOOTER      ========================================================      -->      '''
try: doc+=str(incluir(data,"footer"))
except Exception, e: doc+=str(e)
doc+='''    </div>    <script src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''static/js/script.js"></script>  </body></html>'''