#POST subcontroller

if p["action"]=="listar" and p["multipart/form-data"]==False:

	
      
      
	  

      if p["method"]=="get":

      	


        modelos=p["model"]["main"].obtenerFilas("Tablas,args>Modelos")[0][0]



        tablas=p["model"]["main"].obtenerFilas("args>Tablas")[0][0]




        
        
        data["listar"]=data["model"][modelos[data["args"][0]] if data["args"][0] in modelos else data["args"][0]].obtenerFilas(tablas[data["args"][0]] if data["args"][0] in tablas else data["args"][0]) 




        


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
        
        if data["titulo"]=="Informaciones":


          data["keyNew"]="Información"
        
      elif p["method"]=="ajax":

        modelos=p["model"]["main"].obtenerFilas("Tablas,args>Modelos")[0][0]
        tablas=p["model"]["main"].obtenerFilas("args>Tablas")[0][0]
        

        
        lista=p["model"][modelos[normalizar(data["args"].value)[0]] if normalizar(data["args"].value)[0] in modelos else normalizar(data["args"].value)[0]].obtenerFilas(tablas[normalizar(data["args"].value)[0]] if normalizar(data["args"].value)[0] in tablas else normalizar(data["args"].value)[0])

        formato=p["model"][modelos[normalizar(data["args"].value)[0]] if normalizar(data["args"].value)[0] in modelos else normalizar(data["args"].value)[0]].db(tablas[normalizar(data["args"].value)[0]]  if normalizar(data["args"].value)[0] in tablas else normalizar(data["args"].value)[0]).obtenerFormato("Fecha")
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

if  p["app"]==settings.app and p["multipart/form-data"]==True:

	if p["method"]!="ajax":
		print "Content-type: text/html\n"
		if normalizar(p["cookies"]["beforeArgs"])[0]=="Info":

			if data["action"].value=="Registrar":
					
					if p["model"]["informaciones"].crearInformacion(data["titulo"].value,data["contenido"].value):
						redirecter(config,settings.app,"admin","index","Informaciones",action="listar")()
			elif data["action"].value=="Guardar":
				
				if p["model"]["informaciones"].modificarInformacion(indice,data["titulo"].value,data["contenido"].value):
					redirecter(config,settings.app,"admin","index","Informaciones",action="listar")()
