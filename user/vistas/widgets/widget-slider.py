#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<div class="height-30-xs"><div class="swiper-container swiper-container1">'''

if "slider-imgs" not in data:
    data["slider-imgs"]=[
        data["base_url"]+"static/imgs/Slider/Slider_1.png",
        data["base_url"]+"static/imgs/Slider/Slider_2.png",
        data["base_url"]+"static/imgs/Slider/Slider_3.png"
    ]

print '''        <div class="swiper-wrapper">        '''
for img in data["slider-imgs"]:
  print '''            <div class="swiper-slide"><img src="'''  +str(img)  +'''"></div>        '''
  pass
print '''        </div>        <!-- Add Pagination -->        <div class="swiper-pagination"></div>        <!-- Add Arrows -->        <div class="swiper-button-next"></div>        <div class="swiper-button-prev"></div></div><script>    var swiper = new Swiper('.swiper-container1', {        pagination: '.swiper-pagination',        slidesPerView: 1,        paginationClickable: true,        spaceBetween: 30    });    </script></div>'''