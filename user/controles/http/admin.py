
from modulos.controlador import Controlador
from config import config
from settings import config as settings
import sys

from Controladores.http.admin import preLoad

def admin(data):
	

	cnt=preLoad(data)
	

	class Admin(cnt):
		def __init__(self,data):
			
			cnt.__init__(self,data)
			if self.data["metodo"]==None and self.data["ajax"]==False:
				self.servir()
		def index(self):
			self.servir()

		

		def licencias(self):
			self.vista="licencias"
			self.servir()

	return Admin(data)