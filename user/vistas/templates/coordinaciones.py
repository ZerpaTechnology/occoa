#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html>'''
data["titulo"]="Unexpo núcleo Charallave"
print ''''''
incluir(data,"head")
print '''<body class="sin-pad sin-marg"><div class="container sin-pad"><div class="row  bg-ubuntu_jet marg-t5"><div class="col-md-12 height-10 ohidden"><img src="'''+str(data['base_url']+'static/imgs/portada.jpg')+'''" class="width-100p top-100"></div></div>'''
incluir(data,"barra-buscador")
print '''<div class="row bg-porcelain height-50"><div class="col-md-4 height-5 pad-2">	<h1>CULTURA</h1></div><div class="col-md-2 height-5">	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">GRUPOS CULTURALES</div></a>	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">PRODUCCIONES</div></a>	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">PROYECTOS</div></a></div><div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">	<p>		Unidad del nucleo charallave encarada de gestionar las inscripicones y administracion de notas de nuestro alumnado	</p></div></div><hr><div class="row bg-porcelain height-50"><div class="col-md-4 height-5 pad-2">	<h1>COORDINACION DE TEGNOLOGIA</h1></div><div class="col-md-2 height-5">	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">GRUPOS CULTURALES</div></a>	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">PRODUCCIONES</div></a>	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">PROYECTOS</div></a></div><div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">	<p>		Unidad del nucleo charallave encarada de gestionar las inscripicones y administracion de notas de nuestro alumnado	</p></div></div>'''
incluir(data,"footer")
print '''<div class="row">	</div>	</div>'''
incluir(data,"header")
print '''</body></html>'''