#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+="""<div class="box wow fadeInRight">					                  <div class="box_aside">                    <div class='"""
try: doc+=str(data["widget"]["icon"])
except Exception, e: doc+=str(e)
doc+="""' style="background-color:"""
try: doc+=str(data['widget']['icon-bg'])
except Exception, e: doc+=str(e)
doc+='''"></div>                  </div>                  <div class="box_cnt__no-flow">                    '''
try: doc+=str(data["widget"]["content"])
except Exception, e: doc+=str(e)
doc+='''                  </div>                </div>'''