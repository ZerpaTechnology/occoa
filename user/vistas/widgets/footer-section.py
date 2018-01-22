#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!--Footer-->'''
data["widget"]={} 
doc+=''''''
data["widget"]["content"]="""
<div class="copyright">Business Company © <span id="copyright-year"></span>.&nbsp;&nbsp;<a href="index-5.html">Privacy Policy</a>
            </div>
"""
doc+='''        <section>          <div class="container">            '''
try: doc+=str(data["widget"]["content"])
except Exception, e: doc+=str(e)
doc+='''          </div>        </section>            '''