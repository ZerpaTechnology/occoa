#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/jquery-ui-1.12.1.custom/jquery-ui.css">
	
	<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/jquery-3.1.0.js"></script>
	<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/jquery-ui-1.12.1.custom/jquery-ui.js"></script>
	<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/brython/brython.js"></script>
 <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/brython/brython_stdlib.js"></script>
</head>

<body onload="brython(1)">
<input type="datetime" name="fecha" id="campofecha">
<script type="text/python3">
from browser import window
s=window.jQuery
s("[type='datetime']").datepicker()
</script>
</body>
</html>'''