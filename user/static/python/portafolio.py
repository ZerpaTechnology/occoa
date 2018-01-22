__pragma__("xpath",["../../../../../Components","/opt/lampp/htdocs/PTC/Components"])

__pragma__("alias","s","$")

from DinamicFigure import DinamicFigure
from CyrusNavbar import CyrusNavbar
from SwiperSlider import SwiperSlider
from BoxGrid import BoxGrid
from Collage import Collage
from FooterFixedBrand import FooterFixedBrand

collage=Collage()
config=Config.Config()
collage._imgs=[
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-44-21.png",
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-45-15.png",
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-45-48.png",
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-47-55.png",
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-52-59.png",
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-55-46.png",
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-57-16.png",
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-58-11.png",
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_18-01-38.png",
config.base_url+"/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_19-31-39.png",
]
collage._hints=["Pamax Agency","devstar group","Pralinepatries","strom-fc","joaquinmosquera","cbkmusica","cbkmusica v2","Barra design","Dos bandidos","Gas station"]


def f1(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#pamax"
	return f

def f2(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#devstargroup"
	return f
def f3(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#pralinepatries"
	return f

def f4(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#strom-fc"
	return f

def f5(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#joaquinmosquera"
	return f

def f6(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#cbkmusica"
	return f

def f6(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#joaquinmosquera"
	return f

def f7(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#praline"
	return f

def f8(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#storm-fc"
	return f

def f9(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#barradesign"
	return f

def f10(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#dosbandidos"
	return f

def f10(self):
	def f(evt,self):
		window.location.href=config.base_url+"PTC/occoa/Portafolio/detalles#gasstation"
	return f

collage.activadores=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]



slider=SwiperSlider()
slider.fullscreen()
d=DinamicFigure("Alimentos")
d._src=config.base_url+"apps/occoa/user/static/images/alimentos-ricos-en-fibra.jpg"

d._descripcion="Observa nuestros trabajos en esta categoria"
d.width="100%"
d.activador=lambda self:lambda evt: (evt.preventDefault(),self.visor.slideTo(0,0),self.visor.show())
d.visor=slider


d2=DinamicFigure("Tecnologia")
d2._descripcion="Observa nuestros trabajos en esta categoria"
d2.width="100%"
d2.visor=slider
d2.activador=lambda self:lambda evt: (evt.preventDefault(),self.visor.slideTo(0,0),self.visor.show())
d2._src=config.base_url+"apps/occoa/user/static/images/tecnologia17.jpg"

d3=DinamicFigure("Deporte")
d3._descripcion="Observa nuestros trabajos en esta categoria"
d3.width="100%"
d3.visor=slider
d3.activador=lambda self:lambda evt: (evt.preventDefault(),self.visor.slideTo(0,0),self.visor.show())
d3._src=config.base_url+"apps/occoa/user/static/images/img_como_hacer_deporte_si_nunca_he_hecho_45499_300_150.jpg"

d4=DinamicFigure("Marketing Digital")
d4._descripcion="Observa nuestros trabajos en esta categoria"
d4.width="100%"
d4.visor=slider
d4._src=config.base_url+"apps/occoa/user/static/images/69.jpg"

d5=DinamicFigure("Medicina")
d5._descripcion="Observa nuestros trabajos en esta categoria"
d5.width="100%"
d5.visor=slider
d5._src=config.base_url+"apps/occoa/user/static/images/22730535_1843488702358328_37790343948702229_n.jpg"

d6=DinamicFigure("Construcción")
d6._descripcion="Observa nuestros trabajos en esta categoria"
d6.width="100%"
d6.visor=slider
d6._src=config.base_url+"apps/occoa/user/static/images/costos-construccion-tucuman.jpg"

d7=DinamicFigure("Arte")
d7._descripcion="Observa nuestros trabajos en esta categoria"
d7.width="100%"
d7.visor=slider
d7._src=config.base_url+"apps/occoa/user/static/images/alimentos-ricos-en-fibra.jpg"

d8=DinamicFigure("transporte")
d8._descripcion="Observa nuestros trabajos en esta categoria"
d8.width="100%"
d8.visor=slider
d8._src=config.base_url+"apps/occoa/user/static/images/transporte-terrestre.png"

d9=DinamicFigure("Arrendamiento")
d9._descripcion="Observa nuestros trabajos en esta categoria"
d9.width="100%"
d9.visor=slider
d9._src=config.base_url+"apps/occoa/user/static/images/alimentos-ricos-en-fibra.jpg"


slider.addToSlide(0,collage)


nav=CyrusNavbar()
nav._logo=config.base_url+"apps/occoa/user/static/images/partners/logoOccoa.jpg"

nav.run(s("#portafolio-comp"))

g=BoxGrid()
g.container="container-fluid"

g.appendRows(3)
g.addCols(0,[["md-4","xs-12"],["md-4","xs-12"],["md-4","xs-12"]],0)
g.addCols(1,[["md-4","xs-12"],["md-4","xs-12"],["md-4","xs-12"]],0)
g.addCols(2,[["md-4","xs-12"],["md-4","xs-12"],["md-4","xs-12"]],0)
g.addToCol(0,0,d)
g.addToCol(0,1,d2)
g.addToCol(0,2,d3)
g.addToCol(1,0,d4)
g.addToCol(1,1,d5)
g.addToCol(1,2,d6)
g.addToCol(2,0,d7)
g.addToCol(2,1,d8)
g.addToCol(2,2,d9)


g.run(s("section"))
slider.run(s("footer"))
f=FooterFixedBrand()
f.run(s("footer"))
