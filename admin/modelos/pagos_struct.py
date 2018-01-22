db=DB()

db('Pagos').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Pagos').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Pagos').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Pagos').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Pagos').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Pagos').insertar('Pago por uso de la ptc',[
	[{'name': 'pago', 'value': 'Pago por uso de la ptc', 'Usuario': 'titulo'}, 
	{'Usuario': 'number', 'value': 0, 'name': "usuario"}, 
	{'Monto': 'float', 'name': 'monto', 'value': 100.00}, 
	],
	], 
	{'Pagos': 0}, 
	'12/7/2017 10:27:11', [])
db('Opciones').insertar('Permisos', ['Super admin','Administrador',"Editor","Autor","Colaborador", 'Subscriptor'])