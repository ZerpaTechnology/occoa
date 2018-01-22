	(function () {
		var __name__ = '__main__';
		var SidebarDetalles = __init__ (__world__.Components.SidebarDetalles).SidebarDetalles;
		var LayoutHorizontal = __init__ (__world__.LayoutHorizontal).LayoutHorizontal;
		var Iframe = __init__ (__world__.Iframe).Iframe;
		var Button = __init__ (__world__.Button).Button;
		var config = Config.Config ();
		var l = LayoutHorizontal ();
		l.run ($ ('section'));
		var i = Iframe ();
		i.__iframe.css (dict ({'height': '100vh', 'background-image': "url('{}')".format (config.base_url + 'static/imgs/giphy.gif')}));
		var sidebar = SidebarDetalles ();
		sidebar.iframe = i;
		l.add (sidebar);
		l.add (i);
		l.reloadSizes ();
		__pragma__ ('<use>' +
			'Button' +
			'Components.SidebarDetalles' +
			'Iframe' +
			'LayoutHorizontal' +
		'</use>')
		__pragma__ ('<all>')
			__all__.Button = Button;
			__all__.Iframe = Iframe;
			__all__.LayoutHorizontal = LayoutHorizontal;
			__all__.SidebarDetalles = SidebarDetalles;
			__all__.__name__ = __name__;
			__all__.config = config;
			__all__.i = i;
			__all__.l = l;
			__all__.sidebar = sidebar;
		__pragma__ ('</all>')
	}) ();
