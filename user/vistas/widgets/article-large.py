#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+=''''''
data["widget"]={} 

data["widget"]["content"]=""" 
<h2>Frequently asked questions and answers</h2>
            <p>Phasellus ullamcorper elementum est, id pretium turpis bibendum vel. Aliquam a odio arcu. Morbi a dignissim nisl? Aenean aliquet magna in nulla congue vehicula. Morbi dignissim tristique turpis sed sodales. In tincidunt dapibus semper. Nullam non orci eu massa tempus aliquam! Quisque placerat metus at neque aliquam sit amet iaculis lacus iaculis. Etiam ultrices condimentum justo eu viverra. Curabitur lacinia tristique imperdiet. Aenean bibendum vehicula diam nec placerat. Donec lectus leo, consequat sit amet viverra et.</p>
            <hr>
"""
doc+=''''''
try: doc+=str(data["widget"]["content"])
except Exception, e: doc+=str(e)
doc+=''''''