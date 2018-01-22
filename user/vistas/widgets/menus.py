doc+='''
<link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/jquery-ui-1.12.1.custom/jquery-ui.css">
<style type="text/css">
	#accordion{
	width:300px;
	font-size:14px;
	
	}
	.ui-accordion .ui-accordion-content{
		padding: 0px;
		height: 300px
	}
	.ui-tabs-anchor{
		padding: .1em .8em !important;
	}
	
	li{
		list-style: none;
	}
	span[name='seleccionar-todo']{
		cursor: pointer;
	}
	
</style>
  <div class="tabs">
  <ul>
    <li><a href="#edit-menu"><b>Editar menu</b></a></li>
    <li><a href="#manage-locations"><b>Manejar localizaciones</b></a></li>
    </ul>
  <div id="edit-menu">
<div class="box">
<div class="row">
<div class="col-md-12">
<div class="b-s1 b-r5 b-gray pad-05">
<span>Selecciona un menu para editar </span>
 
<select class="bg-white" style="width: 200px" name="seleccionar-menu">
    <option></option>
	'''
try2:
 for elem in data["Menus"]:
  doc+='''
	<option>'''
  try: doc+=str(elem[0])
  except Exception as e:   doc+=str(e)
  doc+='''</option>
	'''
  pass
except Exception as e: doc+=str(e)
doc+='''
</select>
<button name="aplicar-menu">seleccionar</button>
o <a href="">crea un nuevo menu</a>
</div>

</div>
</div>
<div class="row">
	<div class="col-md-4">
		
<div id="accordion">
  <h3>Paginas</h3>
  <div>
  <div class="tabs">
  <ul>
    <li><a href="#tabs-1">Mas reciente</a></li>
    <li><a href="#tabs-2">Ver todo</a></li>
    <li><a href="#tabs-3">Buscar</a></li>
  </ul>
  <div id="tabs-1" class="sin-marg">
    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">
	<ul style="text-align: left">
	'''
metas=self.data["model"]["global"].formatearListaMetadatos(data["Paginas"])
doc+='''
	'''
try2:
 for k, pagina in enumerate(data["Paginas"]):
  doc+='''
	'''
  meta=metas[k]
  doc+='''
	<li><input type="checkbox"> <b 
	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+pagina[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" 
	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	
	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"
	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" >'''
  try: doc+=str(pagina[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>
	'''
  pass
except Exception as e: doc+=str(e)
doc+='''
	</ul>
	</div>
    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>
  </div>
  <div id="tabs-2">
    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">
	<ul style="text-align: left">
	'''
try2:
 for pagina in data["Paginas"]:
  doc+='''
	'''
  meta=metas[k]
  doc+='''
	<li><input type="checkbox"> <b 
	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+pagina[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" 
	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	
	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"
	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" >'''
  try: doc+=str(pagina[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>
	'''
  pass
except Exception as e: doc+=str(e)
doc+='''
	</ul>
	</div>
    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>
  </div>
  <div id="tabs-3">
    <div>
    	<input type="search" name="buscar-pagina" >
    	<div style="overflow: scroll;height: 200px">
    		
    	</div>
    </div>
  </div>
</div>
 
  </div>
  <h3>Entradas</h3>
  <div>
  <div class="tabs">
  <ul>
    <li><a href="#tabs-4">Mas reciente</a></li>
    <li><a href="#tabs-5">Ver todo</a></li>
    <li><a href="#tabs-6">Buscar</a></li>
  </ul>
  <div id="tabs-4" class="sin-marg">
    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">
	<ul style="text-align: left">
	'''
metas=self.data["model"]["global"].formatearListaMetadatos(data["Entradas"])
doc+='''

	'''
try2:
 for k,entrada in enumerate(data["Entradas"]):
  doc+='''

	'''
  meta=metas[k]
  doc+='''
	<li><input type="checkbox"> <b 
	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+entrada[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" 
	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	
	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"
	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" >'''
  try: doc+=str(entrada[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>
	'''
  pass
except Exception as e: doc+=str(e)
doc+='''
	</ul>
	</div>
    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>
  </div>
  <div id="tabs-5">
    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">
	<ul style="text-align: left">
	
	'''
try2:
 for k,entrada in enumerate(data["Entradas"]):
  doc+='''
	'''
  meta=metas[k]
  doc+='''
	<li><input type="checkbox"> <b 
	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+entrada[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" 
	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	
	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"
	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"
	 >'''
  try: doc+=str(entrada[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>
	'''
  pass
except Exception as e: doc+=str(e)
doc+='''
	</ul>
	</div>
    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>
  </div>
  <div id="tabs-6">
    <div>
    	<input type="search" name="buscar-pagina" >
    	<div style="overflow: scroll;height: 200px">
    		
    	</div>
    </div>
  </div>
  
</div>
 
  </div>
  <h3>Enlaces personalizados</h3>
  <div>
  <table>
  	<tr>
  		<td><b>URL</b></td>
  		<td><input type="" name="custom-url" value="http://"></td>
  	</tr>
  	<tr>
  		<td><b>Texto del enlace</b></td>
  		<td><input type="" name="custom-text"></td>
  	</tr>
  	
  </table>
  <button name="add-to-menu2">Añadir al menu</button>
  </div>
  <h3>Categorias</h3>
  <div>
  <div class="tabs">
  <ul>
    <li><a href="#tabs-7">Mas reciente</a></li>
    <li><a href="#tabs-8">Ver todo</a></li>
    <li><a href="#tabs-9">Buscar</a></li>
  </ul>
  <div id="tabs-7" class="sin-marg">
    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">
	<ul style="text-align: left">
	'''
metas=self.data["model"]["global"].formatearListaMetadatos(data["Categorias"])
doc+='''
	'''
try2:
 for categoria in data["Categorias"]:
  doc+='''
	'''
  meta=metas[k]
  doc+='''
	<li><input type="checkbox"> <b 
	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+categoria[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" 
	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	
	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"
	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''">'''
  try: doc+=str(categoria[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>
	'''
  pass
except Exception as e: doc+=str(e)
doc+='''
	</ul>
	</div>
    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>
  </div>
  <div id="tabs-8">
    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">
	<ul style="text-align: left">
	
	'''
try2:
 for categoria in data["Categorias"]:
  doc+='''
	'''
  meta=metas[k]
  doc+='''
	<li><input type="checkbox"> <b 
	href="'''
  try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(meta['control']+'/' if 'control' in meta else '')+categoria[0].replace(' ','-'))
  except Exception as e:   doc+=str(e)
  doc+='''" 
	modelo="'''
  try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 	
	tabla="'''
  try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	indice="'''
  try: doc+=str(meta['indice'] if 'indice' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"
	control="'''
  try: doc+=str(meta['control'] if 'control' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''" 
	metodo="'''
  try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
  except Exception as e:   doc+=str(e)
  doc+='''"
	>'''
  try: doc+=str(categoria[0])
  except Exception as e:   doc+=str(e)
  doc+='''</b></li>
	'''
  pass
except Exception as e: doc+=str(e)
doc+='''
	</ul>
	</div>
    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>
  </div>
  <div id="tabs-9">
    
  </div>
</div>
 
  </div>
  '''
try2:
 for other_tag in data["other-tags"]:
  doc+='''
  <h3>'''
  try: doc+=str(other_tag)
  except Exception as e:   doc+=str(e)
  doc+='''</h3>
  <div>
  <div class="tabs">
  <ul>
    <li><a href="#tabs-4">Mas reciente</a></li>
    <li><a href="#tabs-5">Ver todo</a></li>
    <li><a href="#tabs-6">Buscar</a></li>
  </ul>
  <div id="tabs-4" class="sin-marg">
    <div class="pad-1 b-s1" style="overflow: scroll;height: 180px;border-radius: 5px;border-color: gray">
	<ul style="text-align: left">
	
	'''
  try2:
   for tag in data[other_tag]:
    doc+='''
	<li><input type="checkbox"> <b 
	href="'''
    try: doc+=str((config.base_url+(settings.app+'/') if config.default_app==settings.app else '')+(tag[0]['control']+'/' if 'control' in tag[0] else '')+tag[0]['titulo'].replace(' ','-'))
    except Exception as e:     doc+=str(e)
    doc+='''" 
	modelo="'''
    try: doc+=str(meta['modelo'] if 'modelo' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''" 	
	tabla="'''
    try: doc+=str(meta['tabla'] if 'tabla' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''" 
	indice="'''
    try: doc+=str(meta['indice'] if 'indice' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''"
	control="'''
    try: doc+=str(meta['control'] if 'control' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''" 
	metodo="'''
    try: doc+=str(meta['metodo'] if 'metodo' in meta else '')
    except Exception as e:     doc+=str(e)
    doc+='''"
	>'''
    try: doc+=str(tag[0])
    except Exception as e:     doc+=str(e)
    doc+='''</b></li>
	'''
    pass
  except Exception as e: doc+=str(e)
  doc+='''
	</ul>
	</div>
    <span name="seleccionar-todo">Seleccionar todo</span> <button name="add-to-menu">Añadir al menu</button>
  </div>
  <div id="tabs-5">
    
  </div>
  <div id="tabs-6">
    <div>
    	<input type="search" name="buscar-pagina" >
    	<div style="overflow: scroll;height: 200px">
    		
    	</div>
    </div>
  </div>
  
</div>
 
  </div>
  '''
  pass
except Exception as e: doc+=str(e)
doc+='''
</div>


	</div>
	<div class="col-md-8">
	<div class="pad-1 bg-graylight">
		<label><b>Nombre del menu</b></label><input type="" name="nombre-menu" placeholder="Menú">
		<button name="guardar-menu">Guardar</button>
	</div>
	<div class=" pad-1">
	<h2><b>Estructura del menu</b></h2>

<p>Arrastre cada elemento en el orden que prefiera. Haga clic en la flecha a la derecha del elemento para mostrar opciones de configuración adicionales.</p>


		<ul id="nav-menu" class="sortable droptrue">
  
  
</ul>
	</div>
	<div>
		<h2>Configuracion del menu</h2>
		<table>
			<tr>
				<td>Añadir pagina automaticas</td>
				<td><input type="checkbox" name="nivel-superior">
Agregar automáticamente nuevas páginas de nivel superior a este menú</td>
			</tr>
			<tr>
				<td>Mostrar localización</td>
				<td><input type="checkbox" name="menu-principal">Menu principal</td>
			</tr>
			<tr>
				<td></td>
				<td><input type="checkbox" name="menu-pie">Menu de pie</td>
			</tr>
			<tr>
				<td></td>
				<td><input type="checkbox" name="menu-barra-superior">Menu barra superior</td>
			</tr>
			<tr>
				<td></td>
				<td><input type="checkbox" name="menu-mi-cuenta">Menu mi cuenta</td>
			</tr>
		</table>
		<a href="" name="borrar-menu"> Borrar menu</a>
		<button name="guardar-menu">Guardar menu</button>
	</div>
	</div>

</div>
</div>
</div>
<div id="manage-locations">
<span>El tema admite 4 menús. Seleccione el menú que aparecerá en cada ubicación.</span>
<div>
	<table>
		<tr>
			<td style="padding-right: 30px;"><b>Localizacion del tema</b></td>
			<td><b>Asignar menu</b></td>
			<td></td>
		</tr>
		<tr>
			<td>Menu principal</td>
			<td><select style="width: 200px" name="asignar-menu-principal"><option></option></select></td>
			<td><a href="" name="editar-menu">Editar</a>|<a href="" name="usar-nuevo-menu">Usar nuevo menu</a></td>
		</tr>
		<tr>
			<td>Menu de pie</td>
			<td><select style="width: 200px" name="asignar-menu-pie"><option></option></select></td>
			<td><a href="" name="editar-menu">Editar</a>|<a href="" name="usar-nuevo-menu">Usar nuevo menu</a></td>
		</tr>
		<tr>
			<td>Menu barra superior</td>
			<td><select style="width: 200px" name="asignar-menu-barra-superior"><option></option></select></td>
			<td><a href="" name="editar-menu">Editar</a>|<a href="" name="usar-nuevo-menu">Usar nuevo menu</a></td>
		</tr>
		<tr>
			<td>Menu de mi cuenta</td>
			<td><select style="width: 200px" name="asignar-menu-mi-cuenta"><option></option></select></td>
			<td><a href="" name="editar-menu">Editar</a>|<a href="" name="usar-nuevo-menu">Usar nuevo menu</a></td>
		</tr>

	</table>
</div>
</div>

 <script>
  $( function() {
    $( "#accordion" ).accordion({
      collapsible: true
    });
    $( ".accordion" ).accordion({
      collapsible: true,
      active:false
    });
     $( ".tabs" ).tabs();
       $( "ul.droptrue" ).sortable({
      connectWith: "ul"
    });
 
    $( "ul.dropfalse" ).sortable({
      connectWith: "ul",
      dropOnEmpty: false
    });
    $( ".sortable" ).disableSelection();

  } );
  </script>
  <script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/gestor-menus.by"></script>
 <script type="text/python3">
 from browser import window
 window.Gestor("#nav-menu")
 </script>'''