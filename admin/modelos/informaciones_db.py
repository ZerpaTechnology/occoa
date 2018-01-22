# -*- coding: utf-8 -*-
try:
 from modulos.ztec.zdb import DB
except:
 from zdb import DB
db=DB()
db.load=True
db('Informaciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Informaciones').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Informaciones').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Informaciones').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Informaciones').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Informaciones').insertar('Bienvenido a su floristeria en l\xc3\xadnea', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'Bienvenido a su floristeria en l\xc3\xadnea'}, {'Contenido': 'textarea', 'name': 'contenido', 'value': 'Un lugar c\xc3\xb3modo y sencillo para solicitar sus flores y ramos favoritos'}]], {'Info': 0}, '12/7/2017 10:27:11', [])
db('Informaciones').insertar('Bienvenido a su floristeria en l\xc3\xadnea', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'Bienvenido a su floristeria en l\xc3\xadnea'}, {'Contenido': 'textarea', 'name': 'contenido', 'value': '<p>En Inversiones J.DYM 2021 C.A. nos preocupamos por la salud f&iacute;sica, emocional, espiritual y ambiental de la comunidad de Chacao y de la gran caracas. Basados en esta inquietud, un grupo de j&oacute;venes micro empresarios de inversiones J.DYM 2021 C.A. Nos hemos abocado a la cultivaci&oacute;n y ventas de plantas ornamentales de gran belleza y m&iacute;nimo mantenimiento; para armonizar con naturaleza viva los rincones m&aacute;s &iacute;ntimos y personales de todo su hogar; como la elaboraci&oacute;n de ramos de bases, ramilletes florales y frutales, para enaltecer el gozo y el esp&iacute;ritu humano de cada uno de nuestros exclusivos clientes. Contaran con la asesor&iacute;a t&eacute;cnica y experimental de profesionales en el ramo de: plantas ornamentales, florister&iacute;a en general, festejos y producci&oacute;n de sus eventos familiares y corporativos.Contar&aacute; con la m&aacute;s excelsa atenci&oacute;n, al visitar nuestras instalaciones f&iacute;sicas.</p>'}]], {'Info': 1}, '2/9/2017 0:20:47', [])
db('Informaciones').insertar('CONTACTENOS:', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'CONTACTENOS:'}, {'Contenido': 'textarea', 'name': 'contenido', 'value': '\nCorreo electr\xc3\xb3nico: j.dym2021\xc2\xa9gmail.com\n\nTelefonos:0426-9006753 / 0426-9147588 \n\t'}]], {'Info': 2}, '12/7/2017 10:27:11', [])
db('Informaciones').insertar('UBICACI\xc3\x93N:', [[{'Titulo': 'text', 'name': 'titulo', 'value': 'UBICACI\xc3\x93N:'}, {'Contenido': 'textarea', 'name': 'contenido', 'value': '<p>Mercado patrimonial de chacao, frente al seguro social de chacao, salida puerta este.a</p>'}]], {'Info': 3}, '2/9/2017 0:35:41', [])
db.load=False
