db=DB()
db('Paginas').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Paginas').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Paginas').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Paginas').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Paginas').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Pagina-0').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Pagina-0').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Pagina-0').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Pagina-0').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Pagina-0').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Paginas').insertar('Inicio', [
	[{'Titulo': 'text', 'name': 'titulo', 'value': 'Inicio'}, 
	{'Plantilla': 'hidden', 'name': 'plantilla', 'value': 'index'}, 
	{'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-header', 'value': 'Home4'}, 

	{'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 0,"opciones":"archivos"}, 
	{'Conenido': 'textarea', 'name': 'contenido', 'value': ""}, 
	], 
	[{'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-about', 'value': 'About Us'}, 
	]], 
	{'Pagina': 0}, 
	'8/8/2017 19:45:34', [])

db('Pagina-0').insertar('Inicio', [
	[{'Titulo': 'text', 'name': 'titulo', 'value': 'Inicio'}, 
	{'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-header', 'value': 'Home4'}, 
	{'opcion': 0, 'Logo': 'select', 'name': 'logo', 'value': 0,"opciones":"archivos"}, 
	{'Conenido': 'textarea', 'name': 'contenido', 'value': ""}, 
	], 
	[{'Secci\xc3\xb3n': 'text-titulo', 'name': 'section-about', 'value': 'About Us'}, 
	]], 
	{'Pagina-0': 0}, 
	'8/8/2017 19:45:34', [])