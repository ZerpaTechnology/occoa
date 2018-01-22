db=DB()
db('Menus').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Menus').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Menus').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Menus').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Menus').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Principal-0').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Principal-0').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Principal-0').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Principal-0').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Principal-0').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Menus').insertar('Principal', [
	{'Titulo': 'text', 'name': 'titulo', 'value': 'Principal'},
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'INICIO'}, 
	{'Valor': 'text', 'name': 'enlace', 'value': ''}, 
	{'Padre': 'select', 'name': 'padre', 'value': 0,"names":"section-header"}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'ANUNCIOS'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'anuncios'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'ANUNCIANTES'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'anunciantes'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'GANA MÁS'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'gana-mas'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'PREG.\nFREC.'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'preguntas-frecuentes'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'CONTACTO'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'contacto'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'REDES SOCIALES'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'redes-sociales'}, 
	],
	], 
	{'Pagina': 0}, 
	'8/8/2017 19:45:34', [])

db('Principal-0').insertar('Principal', [
	{'Titulo': 'text', 'name': 'titulo', 'value': 'Principal'},
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'INICIO'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': ''}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'ANUNCIOS'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'anuncios'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'ANUNCIANTES'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'anunciantes'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'GANA MÁS'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'gana-mas'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'PREG.\nFREC.'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'preguntas-frecuentes'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'CONTACTO'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'contacto'}, 
	], 
	[
	{'Titulo': 'text-titulo', 'name': 'section-header', 'value': 'REDES SOCIALES'}, 
	{'Valor': 'text-titulo', 'name': 'enlace', 'value': 'redes-sociales'}, 
	],
	], 
	{'Principal-0': 0}, 
	'8/8/2017 19:45:34', [])

