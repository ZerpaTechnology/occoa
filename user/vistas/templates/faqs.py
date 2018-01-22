#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html><html lang="en">  '''
try: doc+=str(incluir(data,"head"))
except Exception, e: doc+=str(e)
doc+='''  <body>    <div class="page">      <!--      ========================================================      							HEADER      ========================================================                  -->      '''
try: doc+=str(incluir(data,"header2"))
except Exception, e: doc+=str(e)
doc+='''      <!--      ========================================================                                  CONTENT      ========================================================      -->      <main>        <section class="well1">          <div class="container">            '''
try: doc+=str(incluir(data,"article-large"))
except Exception, e: doc+=str(e)
doc+='''            '''
try: doc+=str(incluir(data,"section-locations"))
except Exception, e: doc+=str(e)
doc+='''            <hr>            <p>Quisque placerat metus at neque aliquam sit amet iaculis lacus iaculis. Etiam ultrices condimentum justo eu viverra. Curabitur lacinia tristique imperdiet. Aenean bibendum vehicula diam nec placerat. Donec lectus leo, consequat sit amet viverra et, lacinia eu lectus! Nullam convallis; justo a vestibulum interdum, ipsum mauris lobortis urna, in fringilla elit erat at est. Nullam erat risus, volutpat quis porttitor eget, egestas n odio. Aliquam erat volutpat. Proin eu purus sapien, eu accumsan dolor. Nunc iaculis ligula eget massa dictum quis porttitor orci.<br/><br/>Elementum! In lobortis consectetur elit sed fringilla? Aliquam malesuada urna eu dolor volutpat lobortis! Curabitur pellentesque, turpis sit amet iaculis condimentum, urna mi aliquet turpis, itae pharetra mauris eros non arcu. Aenean felis augue, dignissim in tempus eget, cursus sit amet sem? Cras vehicula vehicula nunc id fringilla?</p>            <div class="btn_wr"><a href="#" class="btn2">Search all faqs</a></div>            <div class="btn_wr"><a href="#" class="btn2">Submit question form</a><a href="#" class="btn">Live chat for question</a></div>          </div>        </section>        '''
try: doc+=str(incluir(data,"call-to-actions"))
except Exception, e: doc+=str(e)
doc+='''        '''
#=incluir(data,"aditional-information")
doc+='''      </main>      <!--      ========================================================                                  FOOTER      ========================================================      -->      '''
try: doc+=str(incluir(data,"footer"))
except Exception, e: doc+=str(e)
doc+='''    </div>    <script src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''static/js/script.js"></script>  </body></html>'''