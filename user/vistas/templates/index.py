#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>\n<html lang="en">\n  '''
try: doc+=str(incluir(data,"head"))
except Exception as e: doc+=str(e)
doc+='''\n  <body>\n    <div class="page">\n      <!--\n      ========================================================\n             HEADER\n      ========================================================\n      \n      \n      -->\n      '''
try: doc+=str(incluir(data,"header2"))
except Exception as e: doc+=str(e)
doc+='''\n      \n      <!--\n\n      ========================================================\n                                  CONTENT\n      ========================================================\n      -->\n      <main>\n        <section class="camera_container">\n          <div id="camera" class="camera_wrap">\n            <div data-src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/page-1_slide01.jpg">\n              <div class="camera_caption fadeIn">\n                <div class="container">\n                  <div class="row">\n                    <div class="preffix_6 grid_6">Helping with any of your business needs!</div>\n                  </div>\n                </div>\n              </div>\n            </div>\n            <div data-src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/page-1_slide02.jpg">\n              <div class="camera_caption fadeIn">\n                <div class="container">\n                  <div class="row">\n                    <div class="preffix_6 grid_6">The best strategies to attract new business</div>\n                  </div>\n                </div>\n              </div>\n            </div>\n            <div data-src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/page-1_slide03.jpg">\n              <div class="camera_caption fadeIn">\n                <div class="container">\n                  <div class="row">\n                    <div class="preffix_6 grid_6">A wide range of global business information</div>\n                  </div>\n                </div>\n              </div>\n            </div>\n          </div>\n        </section>\n        '''
data["block-services"]=["hola","mundo","como","estan"] 
doc+='''\n        '''
try: doc+=str(incluir(data,"block-services"))
except Exception as e: doc+=str(e)
doc+='''\n        '''
data["widget"]={} 
doc+='''\n        '''
data["widget"]["titulo"]="Our awards"
doc+='''\n        '''
data["widget-bg-color"]="red"
doc+='''\n        '''
data["widget-color"]="white"
doc+='''\n        '''
data["widget-title-color"]="white"
doc+='''\n        '''
data["widget"]["call-to-actions"]=[
            {"icon":"icon fa-comments","icon-bg":"blue","content":"""<h3 style='color:"""+data["widget-title-color"]+"""'><a href="#">Incididunt ut labore et dolore</a></h3>
                    <p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolor.</p>"""},
            {"icon":"icon fa-comments","icon-bg":"blue","content":"""<h3 style='color:"""+data["widget-title-color"]+"""'><a href="#">Incididunt ut labore et dolore</a></h3>
                    <p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolor.</p>"""},
            {"icon":"icon fa-comments","icon-bg":"blue","content":"""<h3 style='color:"""+data["widget-title-color"]+"""'><a href="#">Incididunt ut labore et dolore</a></h3>
                    <p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolor.</p>"""},
            {"icon":"icon fa-comments","icon-bg":"blue","content":"""<h3 style='color:"""+data["widget-title-color"]+"""'><a href="#">Incididunt ut labore et dolore</a></h3>
                    <p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolor.</p>"""},
                    ] 
doc+='''\n        '''
try: doc+=str(incluir(data,"call-to-actions"))
except Exception as e: doc+=str(e)
doc+='''\n        <section class="well1">\n          <div class="container">\n            <div class="row">\n             '''
data["widget"]={} 
doc+='''\n              '''
data["widget"]["titulo"]="About"
doc+='''\n              '''
data["widget"]["img"]=data['base_url']+"static/images/page-1_img01.jpg"
doc+='''\n              '''
data["widget"]["content"]='''
              <p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatu. Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt. Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna.</p><a href="#" class="btn">Read more</a>
              '''
doc+='''\n              '''
try: doc+=str(incluir(data,"block-colum"))
except Exception as e: doc+=str(e)
doc+='''\n\n              '''
data["widget"]={} 
doc+='''\n              '''
data["widget"]["titulo"]="services"
doc+='''\n'''
data["widget"]["img"]=data['base_url']+"static/images/page-1_img01.jpg"
doc+='''\n'''
data["widget"]["content"]='''<p>Lorem ipsum dolor sit amet conse ctetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>'''
doc+='''\n'''
data["widget"]["list"]=[{"href":"#","service":"Lorem ipsum dolor sit amet","class":""},
                                        {"href":"#","service":"Conse ctetur adipisicing","class":""},
                                        {"href":"#","service":"Elit sed do eiusmod tempor","class":""},
                                        {"href":"#","service":"Incididunt ut labore","class":""},
                                        {"href":"#","service":"Et dolore magna aliqua","class":""},
                                        {"href":"#","service":"Ut enim ad minim veniam","class":""},
                                        {"href":"#","service":"Quis nostrud exercitation","class":""},
                                        {"href":"#","service":"Incididunt ut labore","class":""},
                                        {"href":"#","service":"Et dolore magna aliqua","class":""},]
doc+='''\n\n'''
data["widget"]["btn"]={"href":"#","class":"btn","titulo":"Read more"} 
doc+='''\n'''
try: doc+=str(incluir(data,"block-colum-services"))
except Exception as e: doc+=str(e)
doc+='''\n'''
try: doc+=str(incluir(data,"block-help-center"))
except Exception as e: doc+=str(e)
doc+='''\n            </div>\n          </div>\n        </section>\n      </main>\n      <!--\n      ========================================================\n                                  FOOTER\n      ========================================================\n      -->\n      '''
try: doc+=str(incluir(data,"widget-php",embebido="php"))
except Exception as e: doc+=str(e)
doc+='''\n      '''
try: doc+=str(incluir(data,"footer2"))
except Exception as e: doc+=str(e)
doc+='''\n    </div>\n    <script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/js/script.js"></script>\n  </body>\n</html>\n'''