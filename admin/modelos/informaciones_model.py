#!/usr/bin/env python
# -*- coding: utf-8 -*-
#autor:Jesús Zerpa 
from modulos.ztec.zmodel import Model
import sys
import os
import datetime
import modulos.ztec.zu as zu
sys.path.append("../")
import settings
try:
	import config.config as config
except:
	import config

try:
	class model(Model):
		

		"""docstring for model"""
		#===================================================================
		#Cuerpo del modelo
		
			
		def modificarInformacion(self,indice,nombre,contenido):
			if self.request():
				self.db("Informaciones").modificarCampo(indice,"Nombre",
					nombre
					)
				self.db("Informaciones").modificarCampo(indice,"Contenido",
					[
					[
					{"Titulo":"text","name":"titulo","value":nombre},
					{"Contenido":"textarea","name":"contenido","value":contenido}
					],
					],
					)
				self.db("Informaciones").modificarCampo(indice,"Fecha",
					zu.DateTime(),
					)

				return self.grabar()
		def buscarError(self,token):
			if self.update():
				for elem in self.obtenerFilas("Log"):
					if elem[0]==token:
						return elem
				
		def corregirError(self,indice):
			if self.request():
				self.db("Log").modificarCampo(indice,"Status",True)
				self.grabar()

		def limpiarErrores(self):
			if self.request():
				for k,elem in enumerate(self.obtenerFilas("Log")):
					self.db("Log").delFila(k)
				self.db("Log").id(0)
				self.grabar()



		def borrarFila(self,c,tabla):
			if self.request():
				self.db(tabla).delFila(c)
				return self.grabar()
		def obtenerFilas(self,tabla):
			if self.update():
				c=0
				l=[]
				if tabla in self.db.tablas:
					try:
						while True:
				
							l.append(self.db(tabla).obtenerFilaValores(c))
							c+=1					
					except:

						return l

		def obtenerMenus(self):
			if self.update():
				c=0
				l=[]
				try:
					while True:
			
						l.append(self.db("Menus").obtenerFilaValores(c))
						c+=1					
				except:

					return l

		def borrarConfiguracionPagina(self,pagina,**kwargs):
			if self.request():
				campos=[]
				valores=[]
				for elem in kwargs:
					campos.append(elem)
					valores.append(kwargs)
				_id=self.db("Paginas").obtenerColumna("Nombre").index(Pagina)
				self.db("Paginas").modificarFila(_id,pagina,campos,valores)
				self.grabar()
		#{act}
		def filtrar(self,status,tabla=None):
			#status=["activo"] todos los que tenga activo
			#status=["activo","aprobado"] todos los que tengan activo y aprodado no uno solo
			
			if self.update():	
				l2=[]

				if tabla!=None and type(tabla)!=str:
					l=tabla
				elif type(tabla)==str:
					l=self.obtenerFilas(tabla)
				else:
					l=self.obtenerFilas(self.db.seleccion)

				for k,fila in enumerate(l):
					if len(status)==1:
						for estado in status:
							if estado in fila[4]:
								l2.append(fila)

					else:
						pasa=True
						l3=[]


						for estado in status:
							if estado in fila[4]:
								l3.append(fila)
							else:
								pasa=False
						
						if pasa!=False:
							l2.extend(l3)
				


				return l2


					


		def ordenar(self,por="Fecha",ascendente=True,filtros=None):
			if por=="Fecha":
				formato=self.db.obtenerFormato("Fecha")

				l=[]
				for fila in self.obtenerFilas(self.db.seleccion):
					if l!=[]:
						

						if ascendente==True:
							if datetime.datetime.strptime(l[-1][3],formato)>=datetime.datetime.strptime(fila[3],formato):
								l.append(fila)

							else:
								l.insert(0,fila)

						else:

							if datetime.datetime.strptime(l[-1][3],formato)>=datetime.datetime.strptime(fila[3],formato):
								l.insert(0,fila)

							else:
								l.append(fila)

					else:
						l.append(fila)
				

			elif por=="Nombre":
				l=[]
				for fila in self.obtenerFilas(self.db.seleccion):
					if l!=[]:
						if ascendente==True:
							if zu.cmpString(l[-1][0],fila[0]):
								l.append(fila)
							else:
								l.insert(0,fila)

						else:
							if zu.cmpString(l[-1][0],fila[0]):
								l.insert(0,fila)
							else:
								l.append(fila)
					else:
						l.append(fila)
			


			else:
				pass

			if filtros!=None:
					return self.filtrar(filtros,l)
		def obtenerIdsFiltrados(self,lista):
			l=[]

			for elem in lista:
				

				clave=elem[2].keys()[0]
				l.append(elem[2][clave])
			return l
	
		def closeSession(self,token):
			if self.request():
				filas=self.db("usuarios").obtenerFilasValores(token)
				if filas[6]==token:
					self.db("usuarios").modificarCampo(self.db("usuarios").obtenerFilasId(token)[0],"login",False)
					newToken=zu.randomString()
					while newToken in self.db.obtenerColumna("valor","tokens"):
						newToken=zu.randomString()
					self.db("tokens").modificarCampo(self.db("tokens").obtenerFilasId(token)[0],"valor",newToken)
					return self.grabar()
					
				else:
					return False




except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e