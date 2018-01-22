import imp
import sys
from config import config
from modulos.ztec.zred import gringolizar
class app(object):
	"""docstring for app"""
	__path__=__file__[:__file__.rfind("/")]

	#--------------------------------------
	class admin:
		settings=imp.load_source("",__file__[:__file__.rfind("/")]+"/admin/settings/config.py")
		settings.__path__=__file__[:__file__.rfind("/")]+"/admin/settings/"
		sys.path.append(settings.__path__[:-len("settings/")])
		routes=imp.load_source("",settings.__path__+"routes.py")
		routes.__path__=settings.__path__



		
		class modelos:
			"""docstring for modelos"""
			
			#__path__=__file__[:__file__.rfind("/")]+"/admin/"#+admin.routes.models_folder
			def __init__(self,padre=None,diccionario={}):
				self.parent=padre
				self.root=padre.root
				self.diccionario=diccionario
				self.__path__=self.parent.__path__+self.parent.routes.models_folder
				
				
			def __getitem__(self,clave):
				return self.diccionario[clave]
			def __setitem__(self,clave,valor):	
					self.diccionario[clave]=valor

		def __init__(self,padre):
			self.parent=padre
			self.root=padre.root
			self.__path__=self.parent.__path__+"/admin/"
			
			
			self.modelos=self.modelos(self)
			
	#--------------------------------------
	class user:
		__path__=__file__[:__file__.rfind("/")]+"/user/"


		class cnt(object):
			"""docstring for default"""
			
			class http(object):
				"""docstring for http"""
				def __init__(self, padre):
					self.parent=padre


					self.root=padre.root
					self.__path__=self.parent.__path__+self.root.admin.routes.http_folder
					



					

				def __call__(self,data):

					controladores=self.root.admin.settings.http
					

					


					
					if data["control"] in controladores:


						control=imp.load_source("",self.__path__+data["control"]+".py")
						
						exec("ncontrol=control."+data["control"]+"(data)")



						if data["metodo"]!=None:




							metodo=gringolizar(data["metodo"])

							
							
							

							if  metodo in dir(ncontrol):
								exec("ncontrol."+metodo+"()")
							else:
								exec("ncontrol.metodo_desconocido()")
					
					elif data["control"]=="Plugin":
						from config import config
						import os
						for plugin in data["model"]["main"].obtenerFilas("Plugins"):
							

							if data["metodo"] == plugin[0] and os.path.exists(config.base_root+config.plugins_folder+plugin[0]+"/default.py"):




								control=imp.load_source("",config.base_root+config.plugins_folder+plugin[0]+"/default.py")
								

								exec("ncontrol=control.Plugin(data)")


								if data["args"][0].replace("-","_") in dir(ncontrol):
									exec("ncontrol."+data["args"][0].replace("-","_")+"()")
								else:
									exec("ncontrol.metodo_desconocido()")

						"""
						control=imp.load_source("",self.__path__+self.root.admin.settings.controller+".py")
						exec("ncontrol=control."+self.root.admin.settings.controller+"(data)")
						exec("ncontrol.metodo_desconocido()")
						"""
					elif data["control"]==None:
						
						
						control=imp.load_source("",self.__path__+self.root.admin.settings.controller+".py")
						exec("ncontrol=control."+self.root.admin.settings.controller+"(data)")
					elif data["control"]!=None:
						control=imp.load_source("",self.__path__+self.root.admin.settings.controller+".py")
						exec("ncontrol=control."+self.root.admin.settings.controller+"(data)")
						if data["control"] in dir(ncontrol):
							exec("ncontrol."+data["control"]+"()")
						else:
							ncontrol.metodo_desconocido()

	



			class websockets(object):
				"""docstring for websockets"""
				def __init__(self, padre):
					self.parent=padre
					self.root=padre.root
				def __call__(self,data):
					controladores=self.root.admin.settings.websockets
					if data["control"] in controladores:
						print controladores

			class custom_http(object):
				"""docstring for custom_http"""
				def __init__(self,padre):
					self.parent=padre
					self.root=padre.root
				def __call__(self,data):
					controladores=self.root.admin.settings.custom_http
					if data["control"] in  controladores:
						print controladores
			class custom_websockets(object):
				"""docstring for custom_websockets"""
				def __init__(self,padre):
					self.parent=padre
					self.root=padre.root
				def __call__(self,data):
					controladores=self.root.admin.settings.custom_websockets
					if data["control"] in controladores:
						print controladores					
					
					
					
			def __init__(self,padre):
				self.parent=padre
				self.root=padre.root
				self.__path__=__file__[:__file__.rfind("/")]+"/user/controles/"
				self.http=self.http(self)

				self.custom_http=self.custom_http(self)
				self.websockets=self.websockets(self)
				self.custom_websockets=self.custom_websockets(self)				

				
			def __call__(self,data):
				self.http(data)
				self.custom_http(data)
				self.websockets(data)
				self.custom_websockets(data)


				
		def __init__(self,padre):
			
			self.parent=padre
			self.root=padre.root
			self.cnt=self.cnt(self)
			self.__url__=config.base_url+config.apps_folder+self.root.admin.settings.app+"/user/"
			
			pass



	def __init__(self):
		self.root=self
		self.admin=self.admin(self)
		self.user=self.user(self)
		


	def run(self):
		pass
		
		
		
		
		

		

		




	



		
		
		
		
		