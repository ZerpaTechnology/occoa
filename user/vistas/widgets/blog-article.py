#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<div class="grid_4"><img src="'''
try: doc+=str(data['base_url'])
except Exception, e: doc+=str(e)
doc+='''static/images/page-3_img03.jpg" alt="">                <h3>Donec porta diam eu massa</h3>                <p>Aenean ac leo eget nunc fringilla a non nulla! Nunc orci mi, venenatis quis ultrices vitae, congue non nibh. Nulla bibendum, justo eget ultrices vestibulum erat tortor venenatis risus, sit amet cursus dui augue a arcu.</p><a href="#" class="btn">Read more</a>              </div>'''