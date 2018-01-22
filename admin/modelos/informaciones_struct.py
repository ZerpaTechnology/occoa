db=DB()
db('Informaciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Informaciones').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Informaciones').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Informaciones').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Informaciones').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Informaciones').insertar('Bienvenido a su floristeria en l\xc3\xadnea', [
	[{'Titulo': 'text', 'name': 'titulo', 'value': 'Bienvenido a su floristeria en l\xc3\xadnea'}, 
	{'Contenido': 'textarea', 'name': 'contenido', 'value': 'Un lugar c\xc3\xb3modo y sencillo para solicitar sus flores y ramos favoritos'},
	],
	], 
	{'Info': 0}, 
	'12/7/2017 10:27:11', 
	[])
db('Informaciones').insertar('QUIENES SOMOS', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'Bienvenido a su floristeria en l\xc3\xadnea'}, {'Contenido': 'textarea', 'name': 'contenido', 'value': '\nEn inversiones J.DYM 2021 C.A. nos preocupamos por la salud f\xc3\xadsica, emocional, espiritual y ambiental de la comunidad de Chacao y de la gran caracas.\n\nBasados en esta inquietud, un grupo de j\xc3\xb3venes micro empresarios de inversiones J.DYM 2021 C.A. Nos hemos abocado a la cultivaci\xc3\xb3n y ventas de plantas ornamentales de gran belleza y m\xc3\xadnimo mantenimiento; para armonizar con naturaleza viva los rincones m\xc3\xa1s \xc3\xadntimos y personales de todo su hogar; como la elaboraci\xc3\xb3n de ramos de bases, ramilletes florales y frutales, para enaltecer el gozo y el esp\xc3\xadritu humano de cada uno de nuestros exclusivos clientes.\n\nContaran con la asesor\xc3\xada t\xc3\xa9cnica y experimental de profesionales en el ramo de: plantas ornamentales, florister\xc3\xada en general, festejos y producci\xc3\xb3n de sus eventos familiares y corporativos.Contar\xc3\xa1 con la m\xc3\xa1s excelsa atenci\xc3\xb3n, al visitar nuestras instalaciones f\xc3\xadsicas. \n\t'}]], {'Info': 1}, '12/7/2017 10:27:11', [])
db('Informaciones').insertar('CONTACTENOS:', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'CONTACTENOS:'}, {'Contenido': 'textarea', 'name': 'contenido', 'value': '\nCorreo electr\xc3\xb3nico: j.dym2021\xc2\xa9gmail.com\n\nTelefonos:0426-9006753 / 0426-9147588 \n\t'}]], {'Info': 2}, '12/7/2017 10:27:11', [])
db('Informaciones').insertar('UBICACI\xc3\x93N:', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'UBICACI\xc3\x93N:'}, {'Contenido': 'textarea', 'name': 'contenido', 'value': '\nMercado patrimonial de chacao, frente al seguro social de chacao, salida puerta este. \n\t'}]], {'Info': 3}, '12/7/2017 10:27:11', [])