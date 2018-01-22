#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>\n<html>\n<head>\n	'''
try: doc+=str(incluir(data,"head"))
except Exception as e: doc+=str(e)
doc+='''\n	\n</head>\n<body>\n<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''Components/css/Components.css">\n<section class="Components" style="padding: 10px;height: 500px;width:800px">\n	\n</section>\n<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''/static/js/python/__javascript__/divi.js"></script>\n</body>\n</html>'''