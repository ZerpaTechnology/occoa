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
	'''
try: doc+=str(incluir(data,"box-form-login"))
except Exception, e: doc+=str(e)
doc+='''
		
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