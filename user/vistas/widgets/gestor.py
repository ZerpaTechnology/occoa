doc+='''<div >
<form target="iframeUpload" method="post" enctype="multipart/form-data" action="'''
try: doc+=str(config.base_url+config.controller_folder)
except Exception, e: doc+=str(e)
doc+='''post.py" id="form-upload">
<h2>'''
try: doc+=str("Webapps" if data["action"]=="allapps" else "Plugins")
except Exception, e: doc+=str(e)
doc+="""</h2>
<input type="file" name="file" id="subir-app">
<input type="hidden" name="upload" value='"""
try: doc+=str("webapp" if data["action"]=="allapps" else "plugin")
except Exception, e: doc+=str(e)
doc+="""' >
<input type="hidden" name="action" value="upload">
<input type="hidden" name="nombre" value="" >
<div class="ff hidden" id="detalles">
	<p></p>
	
</div>
</form>
<iframe name="iframeUpload" class="hidden" style="height: 50px;border: none;"></iframe>
<button class="btn bg-blue white b-r5 hidden d-block" name="btn-instalar">Instalar</button>

<div class="bg-gray font-ubuntu pad-l05 font-s14" id="gestor">
	<style type="text/css">
	.btn-webapps:hover{
	color:#00a0d2;
	cursor: pointer;
	}
		
	</style>

	<span style="border: solid; border-color: transparent;" class="btn-webapps">Instaladas</span>
	<div class="d-inline-block bg-ubuntu_ash pad-05">
	<b class="" style="color:rgb(155,0,0);">Nuevo: </b>
	<div class="d-inline-block bg-gray pad-1">
	<span class="btn-webapps" style="border: solid; border-color: transparent;">Destacadas</span>	
	<span class="btn-webapps" style="border: solid; border-color: transparent;">Populares</span>	
	<span class="btn-webapps" style="border: solid; border-color: transparent;">Recientes</span>	
	<span class="btn-webapps" style="border: solid; border-color: transparent;">Favoritos</span>		
	</div>
	</div>
	<input type="search" name="buscar" placeholder="Buscar webapps" style="height:30px">
</div>
<div class="tab">
"""
for app in data["items"]:
  doc+='''
<span class="marg-05 font-ubuntu d-inline-block b-s1">
	<span>
		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][-1]['value'])
  except Exception, e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			
		</div>
	</span>
	<div class="bg-white pad-1">
		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception, e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1" name="'''
  try: doc+=str('activar' if 'Desactivada' in app[4] else 'desactivar')
  except Exception, e:   doc+=str(e)
  doc+='''">'''
  try: doc+=str("Activar" if "Desactivada" in app[4] else "Desactivar")
  except Exception, e:   doc+=str(e)
  doc+='''</button>
		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception, e:   doc+=str(e)
  doc+='''
	</div>
</span>
'''
  pass
doc+='''

</div>
<div class="tab hidden">
'''
for app in data["items-destacadas"]:
  doc+='''
<span class="marg-05 font-ubuntu d-inline-block b-s1">
	<span>
		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][0][-1]['value'])
  except Exception, e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			
		</div>
	</span>
	<div class="bg-white pad-1">
		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception, e:   doc+=str(e)
  doc+=''' </b> <button class="marg-l1" name="instalar_online">'''
  try: doc+=str("instalar")
  except Exception, e:   doc+=str(e)
  doc+="""</button> <span class="pad-l1" name="pago" value='"""
  try: doc+=str(True if "de Pago" in app[-1] else False)
  except Exception, e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str("de Pago" if "de Pago" in app[-1] else "Gratis")
  except Exception, e:   doc+=str(e)
  doc+='''</span>
		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception, e:   doc+=str(e)
  doc+='''
	</div>
</span>
'''
  pass
doc+='''
</div>
<div class="tab hidden">
'''
for app in data["items-populares"]:
  doc+='''
<span class="marg-05 font-ubuntu d-inline-block b-s1">
	<span>
		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][-1]['value'])
  except Exception, e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			
		</div>
	</span>
	<div class="bg-white pad-1">
		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception, e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1" name="instalar_online">'''
  try: doc+=str("instalar")
  except Exception, e:   doc+=str(e)
  doc+="""</button><span class="pad-l1" name="pago" value='"""
  try: doc+=str(True if "de Pago" in app[-1] else False)
  except Exception, e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str("de Pago" if "de Pago" in app[-1] else "Gratis")
  except Exception, e:   doc+=str(e)
  doc+='''</span>
		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception, e:   doc+=str(e)
  doc+='''
	</div>
</span>
'''
  pass
doc+='''
</div>
<div class="tab hidden">
'''
for app in data["items-recientes"]:
  doc+='''
<span class="marg-05 font-ubuntu d-inline-block b-s1">
	<span>
		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][-1]['value'])
  except Exception, e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			
		</div>
	</span>
	<div class="bg-white pad-1">
		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception, e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1" name="instalar_online">'''
  try: doc+=str("instalar")
  except Exception, e:   doc+=str(e)
  doc+="""</button><span class="pad-l1" name="pago" value='"""
  try: doc+=str(True if "de Pago" in app[-1] else False)
  except Exception, e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str("de Pago" if "de Pago" in app[-1] else "Gratis")
  except Exception, e:   doc+=str(e)
  doc+='''</span>
		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception, e:   doc+=str(e)
  doc+='''
	</div>
</span>
'''
  pass
doc+='''
</div>
<div class="tab hidden">
'''
for app in data["items-favoritos"]:
  doc+='''
<span class="marg-05 font-ubuntu d-inline-block b-s1">
	<span>
		<div class="height-30 width-30" style="background-image: url('''
  try: doc+=str(app[1][-1]['value'])
  except Exception, e:   doc+=str(e)
  doc+=''');background-size:cover;background-position: center; ">			
		</div>
	</span>
	<div class="bg-white pad-1">
		<b class="" name="item"> '''
  try: doc+=str(app[0])
  except Exception, e:   doc+=str(e)
  doc+=''' </b><button class="marg-l1" name="instalar_online">'''
  try: doc+=str("instalar")
  except Exception, e:   doc+=str(e)
  doc+="""</button><span class="pad-l1" name="pago" value='"""
  try: doc+=str(True if "de Pago" in app[-1] else False)
  except Exception, e:   doc+=str(e)
  doc+="""'>"""
  try: doc+=str("de Pago" if "de Pago" in app[-1] else "Gratis")
  except Exception, e:   doc+=str(e)
  doc+='''</span>
		'''
  try: doc+=str("<button name='actualizar'>Actualizar</button>" if "Actualizar" in app[4] else "")
  except Exception, e:   doc+=str(e)
  doc+='''
	</div>
</span>
'''
  pass
doc+='''
</div>
<div class="tab hidden">
</div>
</div>
<form target="online-install" method="post" enctype="multipart/form-data" action="'''
try: doc+=str(config.base_url+config.controller_folder)
except Exception, e: doc+=str(e)
doc+="""ajax.py" id="form-online-install">
<input type="hidden" name="control" value='"""
try: doc+=str("webapp" if data["action"]=="allapps" else "plugin")
except Exception, e: doc+=str(e)
doc+="""'>
<input type="hidden" name="app" value="asenzor">
<input type="hidden" name='item' value="">
<input type="hidden" name='action' value="install">

<input type="hidden" name="clave" value="">"""
#clave sirve para mandar un codigo de orden por compra en apps y plugins de pago que se envia por correo
doc+='''
</form>
'''

data["content"]="""
<h3>Para instalar """+("esta app" if data["action"]=="allapps" else "este plugin")+"""</h3>
<p>Deberas insertar la clave de orden que se envio a tu correo electronico en el siguiente campo:</p>
<input type="text" name="user_clave">
<button name="insertar_clave">Aceptar</button>
"""

doc+='''

'''
try: doc+=str(incluir(data,"alert",isglobal=True))
except Exception, e: doc+=str(e)
doc+='''
<iframe name="online-install" class="hidden" >	
</iframe>
<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/brython/gestor.by"></script>
<script type="text/python3">
from browser import window
window.Gestor("#gestor")
</script>'''