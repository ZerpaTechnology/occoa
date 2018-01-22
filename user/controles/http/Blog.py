from Controladores.http.Blog import Blog as blog
class Blog(blog):
	def __init__(self,data):
		blog.__init__(self,data)
		self.add_vista("index")
		if self.data["metodo"]==None:
			self.servir()
	
	def Coordinaciones(self):
		self.add_vista("coordinaciones")
		self.servir()
	def Organizaciones(self):
		self.add_vista("organizaciones")
		self.servir()
	def Instalaciones(self):
		self.add_vista("instalaciones")
		self.servir()
	
	

		
		