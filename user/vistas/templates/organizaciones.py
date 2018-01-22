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
<body class="sin-pad sin-marg">
<div class="container sin-pad">
<div class="row  bg-ubuntu_jet marg-t5">
<div class="col-md-12 height-10 ohidden">
<img src="'''
try: doc+=str(data['base_url']+'static/imgs/portada.jpg')
except Exception, e: doc+=str(e)
doc+='''" class="width-100p top-100">
</div>
</div>
'''
incluir(data,"barra-buscador")
doc+='''
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2">
	<h1>CENUC</h1>
</div>
<div class="col-md-2 height-5">
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">MISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">VISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">SERVICIOS</div></a>
</div>
<div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">
	<p>
		CENUC es el centro estudiantil de nuestro núcleo 
	</p>
</div>
</div>
<hr>
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2">
	<h1>CIDGUN</h1>
</div>
<div class="col-md-2 height-5">
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">MISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">VISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">SERVICIOS</div></a>
</div>
<div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">
	<p>
		El Centro de Innovación y Desarrollo Gran Unexpo (C.I.D.G.UN por sus siglas) es una organización estudiantil conformada por un grupo de estudiantes de nuestro núcleo de challarave con el fin de garantizar la capacidad creación y ejecución de proyecto generados por nuestros estudiantes, de modo que la UNEXPO como casa de estudios de CIDGUN pueda mantener sus capacidades Cientifico-Tegnologicas y competir ante otras instituciones que desarrollen tecnologias en igualdad de condiciones.
	</p>
	<p>
		¡Haciendo nuestro aporte para construir un país potencia!   
	</p>
</div>
</div>
<hr>
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2">
	<h1>MEGUN</h1>
</div>
<div class="col-md-2 height-5">
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">MISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">VISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">SERVICIOS</div></a>
</div>
<div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">
	<p>
		Organización politica del núcleo Charallave
	</p>
</div>
</div>
<hr>
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2">
	<h1>CECHAR</h1>
</div>
<div class="col-md-2 height-5">
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">MISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">VISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">SERVICIOS</div></a>
</div>
<div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">
	<p>
		Organización Estudiantil encargada de organizar y entrenar a los estudiantes del nucleo para escurciones.
	</p>
</div>
</div>
<hr>
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2">
	<h1>FUNEC</h1>
</div>
<div class="col-md-2 height-5">
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">MISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">VISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">SERVICIOS</div></a>
</div>
<div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">
	<p>
		Organización politica del núcleo Charallave
	</p>
</div>
</div>
<hr>
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2">
	<h1>UNEXPO SOMOS TODOS</h1>
</div>
<div class="col-md-2 height-5">
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">MISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">VISIÓN</div></a>
	<a href="" class="d-block marg-05 decoration-none"><div class="pad-1 bg-ubuntu_blue white decoration-none">SERVICIOS</div></a>
</div>
<div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">
	<p>
		Organización politica del núcleo Charallave
	</p>
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
</html>'''