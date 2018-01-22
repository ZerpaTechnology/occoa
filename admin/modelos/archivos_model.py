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
		
		def crearPlantilla(self,nombre,campos):
			if self.request():
				tabla="Plantillas"
				i=len(self.obtenerFilas(tabla))
				self.db(tabla).insertar(nombre,
					campos,
					{"Plantilla":i},
					zu.DateTime(),
					["Publicada"]
					)
				return self.grabar()
		def modificarPlantilla(self,i,nombre,campos):
			if self.request():
				tabla="Plantillas"
				self.db(tabla).modificarCampo(i,"Nombre",nombre)
				self.db(tabla).modificarCampo(i,"Contenido",campos)
				self.db(tabla).modificarCampo(i,"Fecha",zu.DateTime())
				return self.grabar()

		def subirArchivo(self,data):
			
			if self.request():
				tabla="Opciones"
				existe=True
				import os
				
				opciones=self.obtenerFilas(tabla)
				
				archivo=data["archivo"]
				
				opcion=opciones[5][1].index(data["opcion"].value)

				tipo=opciones[3][1].index(data["tipo"].value)
				if archivo.filename!="":
					renombre=data["renombre"].value+archivo.filename[archivo.filename.find("."):] if "renombre" in data and data["renombre"].value!="" else archivo.filename

					i=len(self.obtenerFilas("Archivos"))
					if  data["opcion"].value not in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"):
						
						os.mkdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+data["opcion"].value)
					

					if renombre not in os.listdir(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+data["opcion"].value):
						#self.db(tabla).modificarCampo(opcion,"Valores",l+[renombre+"."+archivo.filename.split(".")[1]])

						f=open(config.base_root+config.apps_folder+settings.app+"/admin/static/archivos/"+data["opcion"].value+"/"+renombre,"w")
						f.write(archivo.file.read())
						f.close()						
					else:
						existe=False

					if existe==True:
						l=self.obtenerFilas("Opciones")[0][1]

						l=l+[renombre]
                                                print len(l)
						self.db("Opciones").modificarCampo(0,"Valores",l)
						self.db("Archivos").insertar(renombre,
								[
									[
									{"Imagen":"img","name":"archivo","value":len(l)-1,"opcion":0},
									{"Título":"text","name":"renombe","value":renombre},							
									{"Enlace":"text","name":"enlace","value":config.base_url+config.apps_folder+settings.app+"/admin/static/archivos/"+data["opcion"].value+"/"+archivo.filename},
									{"Típo":"text","name":"tipo","value":data["tipo"].value},
									]
								],
								{"Archivo":i},
								zu.DateTime(),
								[]
								)
						
						
						
						self.grabar()
						return True
					else:
						return False
				else:
					return False

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
	

except Exception, e:

	if config.mod_debug==True:
		print "error en main_model2<br>"
		print e