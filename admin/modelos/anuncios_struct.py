db=DB()

db('Anuncios').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Anuncios').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Anuncios').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Anuncios').insertar('Anuncio -1',[
	[{'name': 'anuncio', 'value':'Anuncio -1', 'Usuario': 'titulo'}, 
	{'clicks': 'number', 'value': 0, 'name': "clicks"}, 
	{'Enlace': 'text', 'name': 'enalce', 'value': "neobux.com"}, 
	{'Valor': 'number', 'value': 1, 'name': "valor"}, 
	],
	], 
	{'Anuncios': 0}, 
	'12/7/2017 10:27:11', [])
#db('Opciones').insertar('Permisos', ['Super admin','Administrador',"Editor","Autor","Colaborador", 'Subscriptor'])