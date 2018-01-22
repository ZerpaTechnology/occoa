# -*- coding: utf-8 -*-
try:
 from modulos.ztec.zdb import DB
except:
 from zdb import DB
db=DB()
db.load=True
db('Usuarios').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Usuarios').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Usuarios').insertar('Administrador', [[{'name': 'usuario', 'value': 'Administrador', 'Usuario': 'text'}, {'Email': 'text', 'value': 'marquis@occoasolutions.com', 'name': 'email'}, {'Password': 'text', 'name': 'password', 'value': 'marquis@2017'}, {'opcion': 1, 'opciones': 'archivos', 'Avatar': 'select', 'value': 0, 'name': 'avatar'}, {'Token': 'hidden', 'name': 'token', 'value': 'yFDdxD$y'}, {'Muere': 'hidden', 'name': 'muere', 'value': '4/10/2017 16:37:25'}, {'Login': 'hidden', 'name': 'login', 'value': False}, {'opcion': 0, 'value': 0, 'name': 'permisologia', 'opciones': 'usuarios', 'Permisologia': 'select'}]], {'Usuario': 0}, '12/7/2017 10:27:11', [])
db('Opciones').insertar('Permisos', ['Administrador', 'Editor', 'Autor', 'Colaborador', 'Subscriptor'])
db.load=False
