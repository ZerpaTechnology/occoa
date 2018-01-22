#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>
<html lang="en">
  '''
try: doc+=str(incluir(data,"head"))
except Exception, e: doc+=str(e)
doc+='''
  <body>
    <div class="page">
      <!--
      ========================================================
      							HEADER
      ========================================================
      
      
      -->
      '''
try: doc+=str(incluir(data,"header2"))
except Exception, e: doc+=str(e)
doc+='''
      <!--
      ========================================================
                                  CONTENT
      ========================================================
      -->
      <main class="mobile-center">
        '''
try: doc+=str(incluir(data,"video-detalle"))
except Exception, e: doc+=str(e)
doc+='''
        <section class="well1 ins3">
          <div class="container">
            <h2>Who we are</h2>
            <div class="row off1">
              '''
try: doc+=str(incluir(data,"box-article"))
except Exception, e: doc+=str(e)
doc+='''
              '''
#=incluir(data,"box-article2")
doc+='''
              
          </div>
        </section>
        '''
try: doc+=str(incluir(data,"call-to-actions"))
except Exception, e: doc+=str(e)
doc+='''
        '''
try: doc+=str(incluir(data,"row-messages"))
except Exception, e: doc+=str(e)
doc+='''
      </main>
      <!--
      ========================================================
                                  FOOTER
      ========================================================
      -->
      '''
try: doc+=str(incluir(data,"footer"))
except Exception, e: doc+=str(e)
doc+='''
    </div>
    <script src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''static/js/script.js"></script>
  </body>
</html>'''