#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<li>'''
try: doc+=str(data["elem"] if "elem" in data else "")
except Exception, e: doc+=str(e)
doc+='''</p><a href="#"></a></li>'''