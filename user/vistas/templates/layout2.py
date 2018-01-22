#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>
<html>
'''
try: doc+=str(incluir(data,"head"))
except Exception, e: doc+=str(e)
doc+='''
<body onload="brython(1)">
<div class="white" style="background-color: rgb(77, 148, 255) !important">
	<h4 class="marg-l12 marg-l2-xs">UNEXPO - Charallave</h4>
</div>
<section class="container font-s14" style="font-family: sans-serif;">
	<div class="row">
	<div class="col-md-6">
	<div class="pad-t2 pad-b2">
		<span class="blue font-s30"><b>UNEXPO</b></span> | <span class="font-s25">WebLogin</span>
	</div>
	<div class="bg-gray b-r5 pad-3">
	<label class="font-s20">Expediente:</label>
		<input type="" name="">
	<label class="font-s20">Contraseña:</label>
		<input type="" name="">
	<input type="checkbox" name="" class="width-2 sin-marg"><span class="alg-top">Yo uso esta maquina regularmente</span>
	</div>
		
	</div>
	<aside class="col-md-6 text-justify">
		<div class="height-4"></div>
		<div>
			<p><b>Información de seguridad importante:</b> Iniciar sesión en WebAuth le permite acceder a otros sitios web protegidos de UNEXPO Charallave con este navegador, no solo al sitio web que solicitó.</p>
		</div>
	</aside>	
	</div>
	
</section>
<section>
<div class="pad-4 pad-1-xs font-s14 text-justify" style="font-family: sans-serif;">
	<p class="marg-l8 marg-l1-xs">El uso de este sistema está sujeto a las normas y reglamentos de la Universidad de Stanford. Consulte la Guía Administrativa de Stanford para obtener más información.</p>
	
</div>	
</section>

'''
try: doc+=str(incluir(data,"subfooter"))
except Exception, e: doc+=str(e)
doc+='''
'''
try: doc+=str(incluir(data,"footer"))
except Exception, e: doc+=str(e)
doc+='''

</body>
</html>'''