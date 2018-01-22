__pragma__("alias","s","$")
from Widget import Widget
from Image import Image
class Collage(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self._html="<b class='titulo'></b><div class='container'></div>"
		self.target.html("<button class='titulo'></button>")
		self.__button=self.target.find(">button")
		self._hmtl=""
		self._imgs=[]
	def addImages(self,widget):
		
		if type(widget)==list:
			for elem in widget:
				elem.rotation="random"
				elem.update()
				
				self.children.append(elem)
				self.target.find(">.container").append(elem.target)
		else:
			widget.rotation="random"
			widget.update()

			self.children.append(widget)
			self.target.find(">.container").append(widget.target)


	def titulo(self,titulo):
		self.target.find(">.titulo").text(titulo)
		self._titulo=titulo


	def update(self):
		self.format=[self._titulo]
		self.__update__()
		for elem in self._imgs:
			img=Image()
			img._src=elem
			img.rotation="random"
			img.update()
			self.target.find(">.container").append(img.target)

		self.titulo(self._titulo)
		self.__titulo=self.target.find(">.titulo")
	
	
		


		