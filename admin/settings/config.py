#!/usr/bin/python
# -*- coding: utf-8 -*-
libs_python=["ztec","functions"]
libs_php=[]
#aqui va el nombre de las bases de datos
dbs=["main","usuarios","formularios","paginas","archivos","conversaciones","ayuda","publicaciones","informaciones","anuncios","entradas","menus"]
#variable para paso de parametros
serial="00001"
vistas=["index","admin","Sesion","Administrativos","Inicio","Entrar","index2"]
vistas_admin=["index","login","licencias"]
vista_default="index"
app="occoa"
plugins=["pageCreator"]
consola=True
host="localhost"
consola_port=9999
mod_debug=True
ajax_file="ajax.json"
socket_default_controller="chat"
get_controllers=["vistas"]
get_custom_controllers=[]


custom_websocket_controllers=[]

post_controllers=[]
#====================
controller="Inicio"
http=[controller,"admin","Sesion","Blog","Static","Portafolio"]
custom_http=[]
websockets=[]
custom_websockets=[]

layouts=["index","administrativo","Entrar","instalaciones","organizaciones","coordinacion-de-cultura","formulario","galeria","Blog"]
#===============


#===============
post_custom_controllers=[]
get_php_controllers=[]
post_php_controllers=[]
admin_models_embebed={}
models_embebed={"usuarios":["login","closeSession"],"global":["isUser","login"]}
seo_url=True
static_dir="static"
lang="es"