__pragma__("xpath",["../../../../../Components","/opt/lampp/htdocs/PTC/Components"])

__pragma__("alias","s","$")

from Components.SidebarDetalles import SidebarDetalles
from LayoutHorizontal import LayoutHorizontal
from Iframe import Iframe
from Button import Button
config=Config.Config()
l=LayoutHorizontal()
l.run(s("section"))
i=Iframe()

i.__iframe.css({"height":"100vh","background-image":"url('{}')".format(config.base_url+"static/imgs/giphy.gif")})
sidebar=SidebarDetalles()
sidebar.iframe=i








l.add(sidebar)
l.add(i)

#i.__iframe.attr("src","https://zerpatechnology.com.ve/woodridge")

#w.orientacion="vertical"
#w=Button("hola")

l.reloadSizes()
