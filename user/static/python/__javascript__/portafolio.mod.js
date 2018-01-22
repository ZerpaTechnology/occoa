	(function () {
		var __name__ = '__main__';
		var DinamicFigure = __init__ (__world__.DinamicFigure).DinamicFigure;
		var CyrusNavbar = __init__ (__world__.CyrusNavbar).CyrusNavbar;
		var SwiperSlider = __init__ (__world__.SwiperSlider).SwiperSlider;
		var BoxGrid = __init__ (__world__.BoxGrid).BoxGrid;
		var Collage = __init__ (__world__.Collage).Collage;
		var FooterFixedBrand = __init__ (__world__.FooterFixedBrand).FooterFixedBrand;
		var collage = Collage ();
		var config = Config.Config ();
		collage._imgs = list ([config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-44-21.png', config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-45-15.png', config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-45-48.png', config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-47-55.png', config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-52-59.png', config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-55-46.png', config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-57-16.png', config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_17-58-11.png', config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_18-01-38.png', config.base_url + '/apps/occoa/user/static/images/Captura de pantalla_2018-01-16_19-31-39.png']);
		collage._hints = list (['Pamax Agency', 'devstar group', 'Pralinepatries', 'strom-fc', 'joaquinmosquera', 'cbkmusica', 'cbkmusica v2', 'Barra design', 'Dos bandidos', 'Gas station']);
		var f1 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#pamax';
			};
			return f;
		};
		var f2 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#dosbandidos';
			};
			return f;
		};
		var f3 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#barradesign';
			};
			return f;
		};
		var f4 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#cbkmusica';
			};
			return f;
		};
		var f5 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#plazaequity';
			};
			return f;
		};
		var f6 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#joaquinmosquera';
			};
			return f;
		};
		var f7 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#praline';
			};
			return f;
		};
		var f8 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#storm-fc';
			};
			return f;
		};
		var f9 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#gasstation';
			};
			return f;
		};
		var f10 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#occoabrosolutions';
			};
			return f;
		};
		var f10 = function (self) {
			var f = function (evt, self) {
				window.location.href = config.base_url + 'PTC/occoa/Portafolio/detalles#PortafolioOccoa-Z';
			};
			return f;
		};
		collage.activadores = list ([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]);
		var slider = SwiperSlider ();
		slider.fullscreen ();
		var d = DinamicFigure ('Alimentos');
		d._src = config.base_url + 'apps/occoa/user/static/images/alimentos-ricos-en-fibra.jpg';
		d._descripcion = 'Observa nuestros trabajos en esta categoria';
		d.width = '100%';
		d.activador = (function __lambda__ (self) {
			return (function __lambda__ (evt) {
				return tuple ([evt.preventDefault (), self.visor.slideTo (0, 0), self.visor.show ()]);
			});
		});
		d.visor = slider;
		var d2 = DinamicFigure ('Tecnologia');
		d2._descripcion = 'Observa nuestros trabajos en esta categoria';
		d2.width = '100%';
		d2.visor = slider;
		d2.activador = (function __lambda__ (self) {
			return (function __lambda__ (evt) {
				return tuple ([evt.preventDefault (), self.visor.slideTo (0, 0), self.visor.show ()]);
			});
		});
		d2._src = config.base_url + 'apps/occoa/user/static/images/tecnologia17.jpg';
		var d3 = DinamicFigure ('Deporte');
		d3._descripcion = 'Observa nuestros trabajos en esta categoria';
		d3.width = '100%';
		d3.visor = slider;
		d3.activador = (function __lambda__ (self) {
			return (function __lambda__ (evt) {
				return tuple ([evt.preventDefault (), self.visor.slideTo (0, 0), self.visor.show ()]);
			});
		});
		d3._src = config.base_url + 'apps/occoa/user/static/images/img_como_hacer_deporte_si_nunca_he_hecho_45499_300_150.jpg';
		var d4 = DinamicFigure ('Marketing Digital');
		d4._descripcion = 'Observa nuestros trabajos en esta categoria';
		d4.width = '100%';
		d4.visor = slider;
		d4._src = config.base_url + 'apps/occoa/user/static/images/69.jpg';
		var d5 = DinamicFigure ('Medicina');
		d5._descripcion = 'Observa nuestros trabajos en esta categoria';
		d5.width = '100%';
		d5.visor = slider;
		d5._src = config.base_url + 'apps/occoa/user/static/images/22730535_1843488702358328_37790343948702229_n.jpg';
		var d6 = DinamicFigure ('Construcción');
		d6._descripcion = 'Observa nuestros trabajos en esta categoria';
		d6.width = '100%';
		d6.visor = slider;
		d6._src = config.base_url + 'apps/occoa/user/static/images/costos-construccion-tucuman.jpg';
		var d7 = DinamicFigure ('Arte');
		d7._descripcion = 'Observa nuestros trabajos en esta categoria';
		d7.width = '100%';
		d7.visor = slider;
		d7._src = config.base_url + 'apps/occoa/user/static/images/alimentos-ricos-en-fibra.jpg';
		var d8 = DinamicFigure ('transporte');
		d8._descripcion = 'Observa nuestros trabajos en esta categoria';
		d8.width = '100%';
		d8.visor = slider;
		d8._src = config.base_url + 'apps/occoa/user/static/images/transporte-terrestre.png';
		var d9 = DinamicFigure ('Arrendamiento');
		d9._descripcion = 'Observa nuestros trabajos en esta categoria';
		d9.width = '100%';
		d9.visor = slider;
		d9._src = config.base_url + 'apps/occoa/user/static/images/alimentos-ricos-en-fibra.jpg';
		slider.addToSlide (0, collage);
		var nav = CyrusNavbar ();
		nav._logo = config.base_url + 'apps/occoa/user/static/images/partners/logoOccoa.jpg';
		nav.run ($ ('#portafolio-comp'));
		var g = BoxGrid ();
		g.container = 'container-fluid';
		g.appendRows (3);
		g.addCols (0, list ([list (['md-4', 'xs-12']), list (['md-4', 'xs-12']), list (['md-4', 'xs-12'])]), 0);
		g.addCols (1, list ([list (['md-4', 'xs-12']), list (['md-4', 'xs-12']), list (['md-4', 'xs-12'])]), 0);
		g.addCols (2, list ([list (['md-4', 'xs-12']), list (['md-4', 'xs-12']), list (['md-4', 'xs-12'])]), 0);
		g.addToCol (0, 0, d);
		g.addToCol (0, 1, d2);
		g.addToCol (0, 2, d3);
		g.addToCol (1, 0, d4);
		g.addToCol (1, 1, d5);
		g.addToCol (1, 2, d6);
		g.addToCol (2, 0, d7);
		g.addToCol (2, 1, d8);
		g.addToCol (2, 2, d9);
		g.run ($ ('section'));
		slider.run ($ ('footer'));
		var f = FooterFixedBrand ();
		f.run ($ ('footer'));
		__pragma__ ('<use>' +
			'BoxGrid' +
			'Collage' +
			'CyrusNavbar' +
			'DinamicFigure' +
			'FooterFixedBrand' +
			'SwiperSlider' +
		'</use>')
		__pragma__ ('<all>')
			__all__.BoxGrid = BoxGrid;
			__all__.Collage = Collage;
			__all__.CyrusNavbar = CyrusNavbar;
			__all__.DinamicFigure = DinamicFigure;
			__all__.FooterFixedBrand = FooterFixedBrand;
			__all__.SwiperSlider = SwiperSlider;
			__all__.__name__ = __name__;
			__all__.collage = collage;
			__all__.config = config;
			__all__.d = d;
			__all__.d2 = d2;
			__all__.d3 = d3;
			__all__.d4 = d4;
			__all__.d5 = d5;
			__all__.d6 = d6;
			__all__.d7 = d7;
			__all__.d8 = d8;
			__all__.d9 = d9;
			__all__.f = f;
			__all__.f1 = f1;
			__all__.f10 = f10;
			__all__.f2 = f2;
			__all__.f3 = f3;
			__all__.f4 = f4;
			__all__.f5 = f5;
			__all__.f6 = f6;
			__all__.f7 = f7;
			__all__.f8 = f8;
			__all__.f9 = f9;
			__all__.g = g;
			__all__.nav = nav;
			__all__.slider = slider;
		__pragma__ ('</all>')
	}) ();
