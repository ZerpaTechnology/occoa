#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>
<html>
'''
data["titulo"]="Unexpo núcleo Charallave"
doc+='''
'''
incluir(data,"head")
doc+='''
  <!-- hola mundo -->
<body class="sin-pad sin-marg">
<div class="container sin-pad">
<div class="row  bg-ubuntu_jet marg-t5">
<div class="col-md-12 height-50">

</div>
</div>
<div class="row bg-ubuntu_ash height-2 pad-05 text-center">
 <div class="col-xs-12 col-sm-12 col-md-12  font-ubuntu">
  <a href="" class="bg-ubuntu_yellow pad-05 pad-l2 pad-r2 decoration-none white b-s1" >Rectorados</a>
  <input type="search" name="" placeholder="Buscar..." class="text-center">
  <a href="" class="bg-ubuntu_yellow pad-05 decoration-none white b-s1" >Vice-rectorados</a>
 </div>
</div>
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2 ohidden">
 <h1 class="text-center">Cultura</h1>
 
 <img src="'''
try: doc+=str(data['base_url']+'static/imgs/portada.jpg')
except Exception, e: doc+=str(e)
doc+='''" class="width-100p top-100">
</div>
<div class="col-md-4 height-5">
 <h1>Misión</h1>
</div>
<div class="col-md-4 height-5">
 <h1>Visión</h1>
</div>
</div>
'''
incluir(data,"footer")
doc+='''
<div class="row">
 
</div> 
</div>

'''
incluir(data,"header")
doc+='''
</body>
</html>

'''