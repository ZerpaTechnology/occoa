
from modulos.controlador import Controlador

from Controladores.http.default import default 
from settings import config as settings
from settings import routes
class Static(Controlador):
	def __init__(self,data):
		Controlador.__init__(self,data)

		self.vista="index"
		
		if data["metodo"]==None and data["control"]==None and data["action"]==None:
			self.servir()
		self.modelo=data["model"]["paginas"]
		self.vistas=[]

	def i(self):
		if len(self.data["args"])>0:
			if self.data["args"][0]:
				for elem in self.data["model"]["archivos"].obtenerFilas("Opciones")[0][1]:
					
					if elem==self.data["args"][0]:

						print "Content-type: image/png"+"\n"
						print file(config.base_root+config.apps_folder+settings.app+"/admin/"+routes.static_folder+"/archivos/Imagenes/"+elem, "rb").read()	

		

	





		
		