	__nest__ (
		__all__,
		'Components.SidebarDetalles', {
			__all__: {
				__inited__: false,
				__init__: function (__all__) {
					var __name__ = 'Components.SidebarDetalles';
					var Widget = __init__ (__world__.Widget).Widget;
					var BoxText = __init__ (__world__.BoxText).BoxText;
					var ControlDeslizante = __init__ (__world__.ControlDeslizante).ControlDeslizante;
					var ControlDeslizanteStatus = __init__ (__world__.ControlDeslizanteStatus).ControlDeslizanteStatus;
					var BTNS = __init__ (__world__.BTNS).BTNS;
					var Button = __init__ (__world__.Button).Button;
					var DragSlider = __init__ (__world__.DragSlider).DragSlider;
					var config = Config.Config ();
					var SidebarDetalles = __class__ ('SidebarDetalles', [Widget], {
						__module__: __name__,
						get __init__ () {return __get__ (this, function (self, titulo) {
							if (typeof titulo == 'undefined' || (titulo != null && titulo .hasOwnProperty ("__kwargtrans__"))) {;
								var titulo = 'Presionar';
							};
							Widget.__init__ (self, titulo);
							self.iframe = null;
							self.data = dict ({'pamax': list (['https://www.pamaxoutsourcing.com', '\n\t\t   descripcion\n\t\t   ', dict ({'interactividad': 0, 'Diseño': 0, 'Informacion': 0, 'Recursos multimedia': 0}), dict ({'Estado del proyecto': 0}), list (['Galeria', 'Slider', 'Info', 'SmoothScroll', 'Video', 'Info Popup', 'Ventana Popup', 'Partners', 'Contactos', 'Formulario de contacto', 'Web Responsive'])]), 'devstargroup': list (['https://www.devstar-group.com', '\n\t\t   descripcion\n\t\t   ', dict ({'interactividad': 0, 'Diseño': 0, 'Informacion': 0, 'Recursos multimedia': 0}), dict ({'Estado del proyecto': 0}), list (['Galeria', 'Slider', 'Info', 'SmoothScroll', 'Video', 'Info Popup', 'Ventana Popup', 'Partners', 'Contactos', 'Formulario de contacto', 'Web Responsive'])]), 'pralinepastries': list (['https://www.pralinepastries.com', '\n\t\t   descripcion\n\t\t   ', dict ({'interactividad': 0, 'Diseño': 0, 'Informacion': 0, 'Recursos multimedia': 0}), dict ({'Estado del proyecto': 0}), list (['Galeria', 'Slider', 'Info', 'SmoothScroll', 'Video', 'Info Popup', 'Ventana Popup', 'Partners', 'Contactos', 'Formulario de contacto', 'Web Responsive'])]), 'storm-fc': list (['https://www.storm-fc.com', '\n\t\t   descripcion\n\t\t   ', dict ({'interactividad': 0, 'Diseño': 0, 'Informacion': 0, 'Recursos multimedia': 0}), dict ({'Estado del proyecto': 0}), list (['Galeria', 'Slider', 'Info', 'SmoothScroll', 'Video', 'Info Popup', 'Ventana Popup', 'Partners', 'Contactos', 'Formulario de contacto', 'Web Responsive'])]), 'joaquinmosquera': list (['https://www.joaquinmosquera.com', '\n\t\t   descripcion\n\t\t   ', dict ({'interactividad': 0, 'Diseño': 0, 'Informacion': 0, 'Recursos multimedia': 0}), dict ({'Estado del proyecto': 0}), list (['Galeria', 'Slider', 'Info', 'SmoothScroll', 'Video', 'Info Popup', 'Ventana Popup', 'Partners', 'Contactos', 'Formulario de contacto', 'Web Responsive'])]), 'cbkmusica': list (['https://www.cbkmusica.com', '\n\t\t   descripcion\n\t\t   ', dict ({'interactividad': 0, 'Diseño': 0, 'Informacion': 0, 'Recursos multimedia': 0}), dict ({'Estado del proyecto': 0}), list (['Galeria', 'Slider', 'Info', 'SmoothScroll', 'Video', 'Info Popup', 'Ventana Popup', 'Partners', 'Contactos', 'Formulario de contacto', 'Web Responsive'])]), 'dosbandidos': list (['https://dosbandidosrestaurant.com', '\n\t\t   descripcion\n\t\t   ', dict ({'interactividad': 0, 'Diseño': 0, 'Informacion': 0, 'Recursos multimedia': 0}), dict ({'Estado del proyecto': 0}), list (['Galeria', 'Slider', 'Info', 'SmoothScroll', 'Video', 'Info Popup', 'Ventana Popup', 'Partners', 'Contactos', 'Formulario de contacto', 'Web Responsive'])]), 'gasstationexpert': list (['http://gasstationexpert.com/wordpress/', '\n\t\t   descripcion\n\t\t   ', dict ({'interactividad': 0, 'Diseño': 0, 'Informacion': 0, 'Recursos multimedia': 0}), dict ({'Estado del proyecto': 0}), list (['Galeria', 'Slider', 'Info', 'SmoothScroll', 'Video', 'Info Popup', 'Ventana Popup', 'Partners', 'Contactos', 'Formulario de contacto', 'Web Responsive'])]), 'occoabrosolutions': list (['https://www.occoasolutions.com', '\n\t\t   descripcion\n\t\t   ', dict ({'interactividad': 0, 'Diseño': 0, 'Informacion': 0, 'Recursos multimedia': 0}), dict ({'Estado del proyecto': 0}), list (['Galeria', 'Slider', 'Info', 'SmoothScroll', 'Video', 'Info Popup', 'Ventana Popup', 'Partners', 'Contactos', 'Formulario de contacto', 'Web Responsive'])])});
							var anterior = window.location.href;
							var app = anterior.py_split ('#') [1].strip ();
							var intervalo = function () {
								if (anterior != window.location.href) {
									anterior = window.location.href;
									self.reloadInfo (anterior.py_split ('#') [1]);
								}
							};
							setInterval (intervalo, 1000);
						});},
						get reloadInfo () {return __get__ (this, function (self, app) {
							self.BoxText.titulo ('Proyecto: ' + app);
							self.BoxText.text (self.data [app] [1]);
							self.iframe.__iframe.attr ('src', self.data [app] [0]);
						});},
						get py_update () {return __get__ (this, function (self) {
							self.format = list ([self.titulo]);
							self.__update__ ();
							var anterior = window.location.href;
							var app = anterior.py_split ('#') [1].strip ();
							self.BoxText = BoxText ('Proyecto: ' + app);
							self.add (self.BoxText);
							self.BoxText.__titulo.css (dict ({'color': 'orange'}));
							self.BoxText.text (self.data [app] [1]);
							self.BoxText.h4 ('Balance del proyecto:', dict ({'color': 'blue'}));
							var d = ControlDeslizante ('Interactividad');
							d.largo = 260;
							d.value = 100;
							self.add (d);
							var d = ControlDeslizante ('Diseño');
							d.largo = 260;
							d.value = 50;
							self.add (d);
							var d = ControlDeslizante ('Información');
							d.largo = 260;
							self.add (d);
							var d = ControlDeslizante ('recursos multimedia');
							d.largo = 260;
							self.add (d);
							var d = ControlDeslizanteStatus ('Estado del proyecto');
							d.largo = 260;
							d.value = 50;
							self.add (d);
							var btns = BTNS ('Modulos');
							btns._randomBg = true;
							btns._btns = list ([list ([config.base_url + 'static/imgs/iconos/025-photo.svg', 'Galeria']), list ([config.base_url + 'static/imgs/iconos/015-slider.svg', 'Slider']), list ([config.base_url + 'static/imgs/iconos/007-info.svg', 'Info']), list ([config.base_url + 'static/imgs/iconos/005-scroll.svg', 'Smooth Scroll']), list ([config.base_url + 'static/imgs/iconos/018-youtube.svg', 'Video']), list ([config.base_url + 'static/imgs/iconos/002-speech-bubble-with-ellipsis.png', 'Info Popup']), list ([config.base_url + 'static/imgs/iconos/023-browser-1.svg', 'Ventana popup']), list ([config.base_url + 'static/imgs/iconos/012-youtuber.svg', 'partners']), list ([config.base_url + 'static/imgs/iconos/phone-book.png', 'Contacto']), list ([config.base_url + 'static/imgs/iconos/009-form-2.svg', 'Formulario de contacto']), list ([config.base_url + 'static/imgs/iconos/002-responsive-symbol-with-a-widescreen-monitor-a-cellphone-and-a-tablet.svg', 'Web responsive'])]);
							self.add (btns);
							var slider = DragSlider ('Otros proyectos', 10);
							slider.height = 200;
							self.add (slider);
							slider.bgToSlide (0, config.base_url + 'apps/occoa/user/static/images/partners/logo_white.png');
							slider.bgToSlide (1, config.base_url + 'apps/occoa/user/static/images/partners/logo-dos-bandidos.png');
							slider.bgToSlide (2, config.base_url + 'apps/occoa/user/static/images/partners/logo (2).png');
							slider.bgToSlide (3, config.base_url + 'apps/occoa/user/static/images/partners/logo-cbk-2016.png');
							slider.bgToSlide (4, config.base_url + 'apps/occoa/user/static/images/partners/logo-white.png');
							slider.bgToSlide (5, config.base_url + 'apps/occoa/user/static/images/partners/logo (1).png');
							slider.bgToSlide (6, config.base_url + 'apps/occoa/user/static/images/partners/praline-logo.PNG');
							slider.bgToSlide (7, config.base_url + 'apps/occoa/user/static/images/partners/storm-home-logo.png');
							slider.bgToSlide (8, config.base_url + 'apps/occoa/user/static/images/partners/logo.png');
							slider.bgToSlide (9, config.base_url + 'apps/occoa/user/static/images/partners/logoOccoa.jpg');
							slider.loop (3000);
							var cargar = function () {
								self.iframe.__iframe.attr ('src', self.data [app] [0]);
							};
							setTimeout (cargar, 1000);
						});}
					});
					__pragma__ ('<use>' +
						'BTNS' +
						'BoxText' +
						'Button' +
						'ControlDeslizante' +
						'ControlDeslizanteStatus' +
						'DragSlider' +
						'Widget' +
					'</use>')
					__pragma__ ('<all>')
						__all__.BTNS = BTNS;
						__all__.BoxText = BoxText;
						__all__.Button = Button;
						__all__.ControlDeslizante = ControlDeslizante;
						__all__.ControlDeslizanteStatus = ControlDeslizanteStatus;
						__all__.DragSlider = DragSlider;
						__all__.SidebarDetalles = SidebarDetalles;
						__all__.Widget = Widget;
						__all__.__name__ = __name__;
						__all__.config = config;
					__pragma__ ('</all>')
				}
			}
		}
	);
