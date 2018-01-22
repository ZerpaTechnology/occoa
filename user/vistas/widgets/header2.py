doc+='''<header>\n        <div class="container">\n          <div class="brand">\n            <h1 class="brand_name"><a href="./">Business</a></h1>\n            <p class="brand_slogan">Company</p>\n          </div><a href="callto:#" class="fa-phone">800-2345-6789</a>\n          <p>One of our representatives will happily contact you within 24 hours. For urgent needs call us at</p>\n        </div>\n        <div id="stuck_container" class="stuck_container">\n          <div class="container">\n            <nav class="nav">\n              <ul data-type="navbar" class="sf-menu">\n                <li class="active"><a href="'''
try: doc+=str(routes.base_url)
except Exception as e: doc+=str(e)
doc+='''">Home</a>\n                </li>\n                <li><a href="'''
try: doc+=str(routes.base_url)
except Exception as e: doc+=str(e)
doc+='''acerca">About</a>\n                  <ul>\n                    <li><a href="#">Lorem ipsum dolor</a></li>\n                    <li><a href="#">Conse ctetur adipisicing</a></li>\n                    <li><a href="#">Elit sed do eiusmod\n                        <ul>\n                          <li><a href="#">Lorem ipsum</a></li>\n                          <li><a href="#">Conse adipisicing</a></li>\n                          <li><a href="#">Sit amet dolore</a></li>\n                        </ul></a></li>\n                    <li><a href="#">Incididunt ut labore</a></li>\n                    <li><a href="#">Et dolore magna</a></li>\n                    <li><a href="#">Ut enim ad minim</a></li>\n                  </ul>\n                </li>\n                <li><a href="'''
try: doc+=str(routes.base_url)
except Exception as e: doc+=str(e)
doc+='''servicios">Services</a>\n                </li>\n                <li><a href="'''
try: doc+=str(routes.base_url)
except Exception as e: doc+=str(e)
doc+='''faqs">FAQS</a>\n                </li>\n                <li><a href="'''
try: doc+=str(routes.base_url)
except Exception as e: doc+=str(e)
doc+='''contacto">Contacts</a>\n                </li>\n              </ul>\n            </nav>\n          </div>\n        </div>\n      </header>'''