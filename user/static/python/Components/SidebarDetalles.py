
__pragma__("xpath",["","../../../../../../htdocs/PTC/Components"])

__pragma__("alias","s","$")
from Widget import Widget
from BoxText import BoxText
from ControlDeslizante import ControlDeslizante
from ControlDeslizanteStatus import ControlDeslizanteStatus
from BTNS import BTNS
from Button import Button
from DragSlider import DragSlider
config=Config.Config()

class SidebarDetalles(Widget):
	"""docstring for Button"""
	def __init__(self, titulo="Presionar"):
		Widget.__init__(self,titulo)
		self.iframe=None
		self.data={"pamax":["https://www.pamaxoutsourcing.com",
		   """
		   descripcion
		   """,
		   {'interactividad':0,
		    'Diseño':0,
		    "Informacion":0,
		    "Recursos multimedia":0},
		    {'Estado del proyecto':0},
		    ['Galeria',"Slider","Info",
		     "SmoothScroll","Video","Info Popup",
		     "Ventana Popup","Partners","Contactos",
		     "Formulario de contacto","Web Responsive"],
		   ],
		  "devstargroup":["https://www.devstar-group.com",
		  """
		   descripcion
		   """,
		   {'interactividad':0,
		    'Diseño':0,
		    "Informacion":0,
		    "Recursos multimedia":0},
		    {'Estado del proyecto':0},
		    ['Galeria',"Slider","Info",
		     "SmoothScroll","Video","Info Popup",
		     "Ventana Popup","Partners","Contactos",
		     "Formulario de contacto","Web Responsive"],
		  ],
		  "pralinepastries":["https://www.pralinepastries.com",
		  """
		   descripcion
		   """,
		   {'interactividad':0,
		    'Diseño':0,
		    "Informacion":0,
		    "Recursos multimedia":0},
		    {'Estado del proyecto':0},
		    ['Galeria',"Slider","Info",
		     "SmoothScroll","Video","Info Popup",
		     "Ventana Popup","Partners","Contactos",
		     "Formulario de contacto","Web Responsive"],],
		 'storm-fc':["https://www.storm-fc.com",
		  """
		   descripcion
		   """,
		   {'interactividad':0,
		    'Diseño':0,
		    "Informacion":0,
		    "Recursos multimedia":0},
		    {'Estado del proyecto':0},
		    ['Galeria',"Slider","Info",
		     "SmoothScroll","Video","Info Popup",
		     "Ventana Popup","Partners","Contactos",
		     "Formulario de contacto","Web Responsive"],],

		  'joaquinmosquera':["https://www.joaquinmosquera.com",
		  """
		   descripcion
		   """,
		   {'interactividad':0,
		    'Diseño':0,
		    "Informacion":0,
		    "Recursos multimedia":0},
		    {'Estado del proyecto':0},
		    ['Galeria',"Slider","Info",
		     "SmoothScroll","Video","Info Popup",
		     "Ventana Popup","Partners","Contactos",
		     "Formulario de contacto","Web Responsive"],],
		     
		  'cbkmusica':["https://www.cbkmusica.com",
		  """
		   descripcion
		   """,
		   {'interactividad':0,
		    'Diseño':0,
		    "Informacion":0,
		    "Recursos multimedia":0},
		    {'Estado del proyecto':0},
		    ['Galeria',"Slider","Info",
		     "SmoothScroll","Video","Info Popup",
		     "Ventana Popup","Partners","Contactos",
		     "Formulario de contacto","Web Responsive"],],

		  'dosbandidos':["https://dosbandidosrestaurant.com",
		  """
		   descripcion
		   """,
		   {'interactividad':0,
		    'Diseño':0,
		    "Informacion":0,
		    "Recursos multimedia":0},
		    {'Estado del proyecto':0},
		    ['Galeria',"Slider","Info",
		     "SmoothScroll","Video","Info Popup",
		     "Ventana Popup","Partners","Contactos",
		     "Formulario de contacto","Web Responsive"],],

		  'gasstationexpert':["http://gasstationexpert.com/wordpress/",
		  """
		   descripcion
		   """,
		   {'interactividad':0,
		    'Diseño':0,
		    "Informacion":0,
		    "Recursos multimedia":0},
		    {'Estado del proyecto':0},
		    ['Galeria',"Slider","Info",
		     "SmoothScroll","Video","Info Popup",
		     "Ventana Popup","Partners","Contactos",
		     "Formulario de contacto","Web Responsive"],],

		 
		  

		   

		   'occoabrosolutions':["https://www.occoasolutions.com",
		  """
		   descripcion
		   """,
		   {'interactividad':0,
		    'Diseño':0,
		    "Informacion":0,
		    "Recursos multimedia":0},
		    {'Estado del proyecto':0},
		    ['Galeria',"Slider","Info",
		     "SmoothScroll","Video","Info Popup",
		     "Ventana Popup","Partners","Contactos",
		     "Formulario de contacto","Web Responsive"],],
		  }
		anterior=window.location.href
		app=anterior.split("#")[1].strip()
		def intervalo():
			nonlocal anterior
			nonlocal self

			if anterior!=window.location.href:
				anterior=window.location.href
				self.reloadInfo(anterior.split("#")[1])
				
			
			

		setInterval(intervalo,1000)

	def reloadInfo(self,app):
		self.BoxText.titulo("Proyecto: "+app)
		
		self.BoxText.text(self.data[app][1])

		self.iframe.__iframe.attr("src",self.data[app][0])


	def update(self):
		self.format=[self.titulo]
		self.__update__()
		anterior=window.location.href
		app=anterior.split("#")[1].strip()
		
		
		self.BoxText=BoxText("Proyecto: "+app)
		self.add(self.BoxText)
		self.BoxText.__titulo.css({"color":"orange"})

		self.BoxText.text(self.data[app][1])
		self.BoxText.h4("Balance del proyecto:",{"color":"blue"})
		
		d=ControlDeslizante("Interactividad")
		d.largo=260
		d.value=100
		self.add(d)
		d=ControlDeslizante("Diseño")
		d.largo=260
		d.value=50
		self.add(d)
		d=ControlDeslizante("Información")
		d.largo=260
		self.add(d)
		d=ControlDeslizante("recursos multimedia")
		d.largo=260
		self.add(d)
		d=ControlDeslizanteStatus("Estado del proyecto")
		d.largo=260
		d.value=50
		self.add(d)

		btns=BTNS("Modulos")
		btns._randomBg=True


		btns._btns=[[config.base_url+"static/imgs/iconos/025-photo.svg","Galeria"],
					[config.base_url+"static/imgs/iconos/015-slider.svg","Slider"],
					[config.base_url+"static/imgs/iconos/007-info.svg","Info"],
					[config.base_url+"static/imgs/iconos/005-scroll.svg","Smooth Scroll"],
					[config.base_url+"static/imgs/iconos/018-youtube.svg","Video"],
					[config.base_url+"static/imgs/iconos/002-speech-bubble-with-ellipsis.png","Info Popup"],
					[config.base_url+"static/imgs/iconos/023-browser-1.svg","Ventana popup"],
					[config.base_url+"static/imgs/iconos/012-youtuber.svg","partners"],
					[config.base_url+"static/imgs/iconos/phone-book.png","Contacto"],
					[config.base_url+"static/imgs/iconos/009-form-2.svg","Formulario de contacto"],
					[config.base_url+"static/imgs/iconos/002-responsive-symbol-with-a-widescreen-monitor-a-cellphone-and-a-tablet.svg","Web responsive"],

					]
		self.add(btns)
		
		slider=DragSlider("Otros proyectos",10)
		slider.height=200
		
		

		self.add(slider)

		slider.bgToSlide(0,config.base_url+"apps/occoa/user/static/images/partners/logo_white.png")
		slider.bgToSlide(1,config.base_url+"apps/occoa/user/static/images/partners/logo-dos-bandidos.png")
		slider.bgToSlide(2,config.base_url+"apps/occoa/user/static/images/partners/logo (2).png")
		slider.bgToSlide(3,config.base_url+"apps/occoa/user/static/images/partners/logo-cbk-2016.png")
		slider.bgToSlide(4,config.base_url+"apps/occoa/user/static/images/partners/logo-white.png")
		slider.bgToSlide(5,config.base_url+"apps/occoa/user/static/images/partners/logo (1).png")
		slider.bgToSlide(6,config.base_url+"apps/occoa/user/static/images/partners/praline-logo.PNG")
		slider.bgToSlide(7,config.base_url+"apps/occoa/user/static/images/partners/storm-home-logo.png")
		slider.bgToSlide(8,config.base_url+"apps/occoa/user/static/images/partners/logo.png")
		slider.bgToSlide(9,config.base_url+"apps/occoa/user/static/images/partners/logoOccoa.jpg")

		slider.loop(3000)

		def cargar():
			nonlocal app
			nonlocal self
			self.iframe.__iframe.attr("src",self.data[app][0])
		
		setTimeout(cargar,1000)
		
		
		
		
		#self.add(b3)
		#self.add(b)

		


	
	
		


		