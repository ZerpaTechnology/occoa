#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<footer>        '''
try: doc+=str(incluir(data,"subFooter"))
except Exception, e: doc+=str(e)
doc+='''        '''
try: doc+=str(incluir(data,"footer-section"))
except Exception, e: doc+=str(e)
doc+='''      </footer>'''