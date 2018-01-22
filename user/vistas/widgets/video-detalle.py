#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<section>'''
data["widget"]={} 
doc+=''''''
data["widget"]["iframe"]="//player.vimeo.com/video/37582125?wmode=transparent"
doc+=''''''
data["widget"]["content"]="""<h2>Quick facts</h2>
                <div class="row">
                  <div class="grid_3">
                    <dl class="info">
                      <dt>Name</dt>
                      <dd>Business Company</dd>
                      <dt>Birth Date</dt>
                      <dd>June 23, 1987</dd>
                      <dt>Place of birth</dt>
                      <dd>Los Angeles, California</dd>
                    </dl>
                  </div>
                  <div class="grid_3">
                    <dl class="info">
                      <dt>History</dt>
                      <dd>
                        <ul>
                          <li>Lorem ipsum dolor sit 1997-1999 adipis</li>
                          <li>Pellentesque sed dolor  1995-1999</li>
                          <li>Aliquam congue nisl 2001-2005</li>
                          <li>Mauris accumsa vel diam 2006-2008</li>
                          <li>Sed in lacus ut 2008-2010 enim adipiscing </li>
                        </ul>
                      </dd>
                    </dl>
                  </div>
                </div>"""
doc+='''          <div class="container hr well1 ins2">            <div class="row">              <div class="grid_6">                <div class="video">                  <iframe src="'''
try: doc+=str(data['widget']['iframe'])
except Exception, e: doc+=str(e)
doc+='''" allowfullscreen></iframe>                </div>              </div>              <div class="grid_6">                '''
try: doc+=str(data["widget"]["content"])
except Exception, e: doc+=str(e)
doc+='''              </div>            </div>          </div>        </section>'''