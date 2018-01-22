#POST subcontroller

if "action" in p: 
  if p["control"]=="admin" and "action" in p:
  	if p["action"]=="listar":
  		if p["method"]=="get":

        modelos=p["model"]["main"].obtenerFilas("Tablas,args>Modelos")[0][0]


        tablas=p["model"]["main"].obtenerFilas("args>Tablas")[0][0]


        
        
        data["listar"]=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].obtenerFilas(tablas[data["args"][0]] if data["args"][0] else data["args"][0]) 
        


        data["ajax-data"]={"action":"listar","args":data["args"],"pag-action":None}
        data["baseAction"]="app="+data["app"]+"&admin=True&vista=index&args="+data["args"][0]
        data["titulo"]=decode(data["args"][0])
        data["acciones"]=["Acciones en lote","Editar","Mover a la papelera"]
        data["filtrar"]=["Todas las fechas","Septiembre 2014"]
        data["acciones"]={"Acciones en lote":"marcar","Editar":"editar","Mover a la papelera":"eliminar"}
        data["addNew"]="Añadir nuevo"
        data["n-pag"]=5
        data['status']=["Publicada"]
        dicstatus={}
        for elem in data['status']:
          try:
            filtrados=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].filtrar([elem],data["args"][0])
            dicstatus[elem]=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].obtenerIdsFiltrados(filtrados)
          except:
            filtrados=[]
            dicstatus={}
        data['filtros']=dicstatus
        if data["titulo"]=="Publicaciones":  
          data["keyNew"]="Publicación"

		elif p["method"]=="ajax":
			modelos=p["model"]["main"].obtenerFilas("Tablas,args>Modelos")[0][0]
	        tablas=p["model"]["main"].obtenerFilas("args>Tablas")[0][0]
	        

	        
	        lista=p["model"][modelos[normalizar(data["args"].value)[0]]].obtenerFilas(tablas[normalizar(data["args"].value)[0]])

	        formato=p["model"][modelos[normalizar(data["args"].value)[0]]].db(tablas[normalizar(data["args"].value)[0]]).obtenerFormato("Fecha")
	        titulo=data["args"].value
	        print "data={}"
	        
	        #lista=p["model"][tablas[normalizar(data["args"].value)[0].lower()]].obtenerFilas(normalizar(data["args"].value)[0])
	        for k,elem in enumerate(lista):
	          del lista[k][1]
	        print 'data["listar"]='+str(lista)
	        print 'data["ajax-data"]='+str({"action":"listar","args":normalizar(data["args"].value)[0],"pag-action":None})
	        print 'data["baseAction"]="'+zred.urlBuilder(config,p["app"],"admin","index",args=normalizar(data["args"].value))+'"'
	        print 'data["titulo"]="'+str(data["args"].value)+'"'
	        print 'data["filtrar"]='+str(["Todas las fechas","Septiembre 2014"])
	        print 'data["addNew"]='+"'Añadir nuevo'"
	        print 'data["n-pag"]='+str(5)
	        print "data['campos']="+str(["Titulo","Fecha"])
	        print "data['app']='"+p["app"]+"'"
	        print "data['vista']='"+"index"+"'"
	        print 'data["beforeAction"]="'+p["action"]+'"'
	        print 'data["action"]="'+p["action"]+'"'
	        print 'data["acciones"]={"Acciones en lote":"marcar","Editar":"editar","Mover a la papelera":"eliminar"}'
	        if titulo=="Paginas":
	          pass
	        elif titulo=="Entradas":
	          pass
	        elif titulo=="Menus":
	          pass
	        elif titulo=="Portafolio":
	          pass
	        elif titulo=="Usuarios":
	          pass
	        elif titulo=="Plugins":
	          print "data['campos']="+str(["Plugin","Descripción"])
	        elif titulo=="Negocios" or titulo=="Archivos":
	          #{filto:[elementos filtrados]}
	          status=["Publicada"]
	          dicstatus={}
	          for elem in status:
	            filtrados=p["model"]["main"].ordenar(filtros=[elem])
	            dicstatus[elem]=p["model"]["main"].obtenerIdsFiltrados(filtrados)
	          print "data['filtros']="+str(dicstatus)
	        else:
	          print "data['campos']="+str(["Titulo","Fecha"])
    elif p["action"]=="editar":
        """
        se puede crear un prefijo custom:nombre en el name para saber cuando son nuevos campos 
        ejemplo
        {"Titulo":"text","value":"hola","name":"custom:nombre"}
        """


        data["repeate"]=1

        data["plantillas"]=data["model"]["main"].obtenerFilas("Plantillas")

                      

        if p["method"]=="ajax":
          pass

        elif p["method"]=="get":
          if "args" in p:
            keys=p["args"][0]
            i=normalizar(p["args"][1])
            data["categorias"]={}
            data["titulo"]=p["args"][0]

            if i!=None:
              data["categorias"]={}

              
              if keys=="Menu":

                i=normalizar(p["args"][1])
                data["titulo"]=data["model"]["main"].obtenerFilas("Menus")[i][0]
                l1=data["model"]["main"].obtenerFilas("Menus")[i][1]
                data["boxes"]=[l1]
              elif keys=="Pagina":
                data["titulo"]=data["model"]["paginas"].obtenerFilas("Paginas")[i][0]
                data["layout"]=data["titulo"]
                data["post"]=str(i)
                data["pagina"]="{'pagina':'"+data["titulo"]+"'}"
                
                if len(data["args"])>2:
                  
                  l1=data["model"]["paginas"].obtenerFilas("Pagina-"+str(data["args"][2]) )[i][1]
                else:
                  l1=data["model"]["paginas"].obtenerFilas("Paginas")[i][1]

                data["boxes"]=[l1]

if  p["app"]==settings.app:
	if beforeAction=="Publicacion":
		if data["action"].value=="Registrar":
				
				p["model"]["publicaciones"].crearPublicacion(data["titulo"].value,p["model"]["publicaciones"].obtenerFilas("Opciones")[0][1].index(data["img"].value),data["publish"].value)
			
		elif data["action"].value=="Guardar":
			
			if p["model"]["publicaciones"].modificarPublicacion(indice,data["titulo"].value,p["model"]["publicaciones"].obtenerFilas("Opciones")[0][1].index(data["img"].value),data["publish"].value):
				redirecter("",settings.app,"index",admin=True,args="Publicaciones",action="listar")()