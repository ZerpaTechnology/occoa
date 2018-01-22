#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>\n<html>\n\n	'''
try: doc+=str(incluir(data,"head"))
except Exception as e: doc+=str(e)
doc+='''\n	<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">\n\n<body >\n	<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''Components/css/Components.css">\n	<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/python/Components/css/Components.css">\n	\n	<link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/bootstrap/css/bootstrap.min.css" />\n	<script type="text/javascript" src="'''
try: doc+=str(config.base_url+settings.app)
except Exception as e: doc+=str(e)
doc+='''/Portafolio/datos"></script>\n	<section class="Components" id="portafolio-comp">\n		\n	</section>\n	<footer class="Components">\n		\n	</footer>\n	<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/bootstrap/js/bootstrap.js" type="text/javascript" ></script>\n	\n	<script type="text/javascript" src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/python/__javascript__/portafolio.js"></script>\n\n</body>\n</html>'''