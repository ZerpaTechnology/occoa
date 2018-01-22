
from modulos.controlador import Controlador

from Controladores.http.default import default 

class Inicio(default):
	def __init__(self,data):

		default.__init__(self,data)
		

		self.vista="index"
		
		if data["metodo"]==None and data["control"]==None and data["action"]==None:
			self.servir()
		self.modelo=data["model"]["paginas"]
		

	def acerca(self):
		self.add_vista("acerca")
		self.servir()
	def servicios(self):
		self.add_vista("servicios")
		self.servir()
	def faqs(self):
		self.add_vista("faqs")
		self.servir()
	def contacto(self):
		self.add_vista("contacto")
		self.servir()
	def Instalaciones(self):
		self.add_vista("instalaciones")
		self.servir()
	





		
		