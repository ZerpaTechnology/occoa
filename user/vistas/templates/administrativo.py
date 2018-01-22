#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>
<html>
'''
data["titulo"]="Unexpo núcleo Charallave"
doc+='''
'''
try: doc+=str(incluir(data,"head"))
except Exception, e: doc+=str(e)
doc+='''
<body class="" >
'''
try: doc+=str(incluir(data,"widget-navbar"))
except Exception, e: doc+=str(e)
doc+='''
<div class="container-fluid">


'''
#=incluir(data,"barra-buscador")
doc+='''
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2">
	<h1>DACE</h1>
</div>
<div class="col-md-2 height-5">
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Descargar constancia de estudios</div></a>
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Descargar record Academico</div></a>
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Descargar requisitos de inscripción</div></a>
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Carreras</div></a>
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Especializaciones</div></a>
</div>
<div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">
	<p>
		Unidad del nucleo charallave encarada de gestionar las inscripicones y administracion de notas de nuestro alumnado
	</p>
</div>
</div>
<hr>
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2">
	<h1>DOBE</h1>
</div>
<div class="col-md-2 height-5">
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Solicitar beca trabajo</div></a>
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Descargar record Academico</div></a>
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Descargar requisitos de inscripción</div></a>
</div>
<div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">
	<p>
		Unidad del nucleo charallave encarada de gestionar las inscripicones y administracion de notas de nuestro alumnado
	</p>
</div>
</div>
<hr>
<div class="row bg-porcelain height-50">
<div class="col-md-4 height-5 pad-2">
	<h1>DIRECCIÓN</h1>
</div>
<div class="col-md-2 height-5">
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Enviar carta</div></a>
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Descargar record Academico</div></a>
	<a href="" class="d-block decoration-none marg-05"><div class="pad-1 bg-ubuntu_blue white decoration-none">Descargar requisitos de inscripción</div></a>
</div>
<div class="col-md-6 height-5 pad-1 bg-ubuntu_porcelain font-ubuntu">
	<p>
		Unidad del nucleo charallave encarada de gestionar las inscripicones y administracion de notas de nuestro alumnado
	</p>
</div>
</div>
'''
try: doc+=str(incluir(data,"footer"))
except Exception, e: doc+=str(e)
doc+='''
<div class="row">
	
</div>	
</div>


</body>
</html>'''