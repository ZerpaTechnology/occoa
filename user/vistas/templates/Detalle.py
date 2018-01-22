#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>\n<html>\n\n	'''
try: doc+=str(incluir(data,"head"))
except Exception as e: doc+=str(e)
doc+='''\n	\n\n<body >\n	<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''Components/css/Components.css">\n	<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/python/Components/css/Components.css">\n	<script type="text/javascript" src="'''
try: doc+=str(config.base_url+settings.app)
except Exception as e: doc+=str(e)
doc+='''/Portafolio/datos"></script>\n	<section class="Components">\n		\n	</section>\n	<script type="text/javascript" src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/python/__javascript__/detalles.js"></script>\n\n</body>\n</html>'''