#Get subcontroller

try:
    
  
  data["hidden"]=[]
  data["style"]={}
  data["css"]={}
  


  
  if p["control"]!="admin"  and "vista" in p: 

    """
    Cuando el admin esta desactivado.
    """



    
    if errores==[]:





      if (p["vista"]=="index" or p["vista"]==None) and p["control"]==None:

            
        def _min(foto):
          return foto[:foto.find(".")]+"_540x540"+foto[foto.find("."):]
        data["min"]=_min
        
        if "post" not in p:
          post=0
        else:
          post=p["post"]
        

        data["page"]=data["model"]["paginas"].obtenerFilas("Paginas")[post][1]

        data["parrafer"]=zred.parrafer
        i=0
        
        data["actionbase"]="app="+settings.app+"&vista="
        servir("index",data)


      elif p["vista"]==None   and p["control"]=="chat":
        data["opciones"]=p["model"]["main"].obtenerFilas("Opciones")
        
        #servir("chat",data)
      elif p["vista"]=="noticias":
       
       data["opciones"]=data["model"]["main"].obtenerFilas("Opciones") 
       i=0
       data["pagina"]=data["model"]["paginas"].obtenerFilas("Paginas")[i][1]

       data["entradas"]=data["model"]["entradas"].obtenerFilas("Entradas")

      elif p["vista"]=="formulario":
       data["opciones"]=data["model"]["main"].obtenerFilas("Opciones")     
       data["boxes"]=[data["model"]["formularios"].obtenerFilas("Formularios")[0][1]]
       data["action"]="Post de Formulario_0"
       if "post" not in p:
        post=0
       else:
        post=int(p["post"])

       data["page"]=data["model"]["formularios"].obtenerFilas("Formularios")


      elif p["vista"]=="galeria":
       
       data["opciones"]=data["model"]["main"].obtenerFilas("Opciones")
       data["galeria"]=data["model"]["galerias"].obtenerFilas("Galerias")
       
      elif p["vista"]=="logs":
       
       #redirecter("",settings.app,"index")()
       pass

      else:

        l1=[]
        if "args" not in data:
          data["args"]={"Login":True}


        data["titulo"]=data["model"]["usuarios"].obtenerFilas("Usuarios")[0][0]
        #data["model"]["main"].obtenerFilas("Paginas")[i][1]
        for box in data["model"]["usuarios"].obtenerFilas("Usuarios")[0][1]:
          l=[]
          for campos in box:
            if type(campos)==dict:
              campos["value"]=""
              l.append(campos)
          if l!=[]:
            l1.append(l)
        data["boxes"]=l1


        if  data["login"]==True:

          """
          Cuando el usuario esta logeado pero en el modo de usuario.


          Nota: eso le permitira hacer operaciones que se registren en la base 
          de datos que no nos necesariamentes las del dashboard, como por ejemplo
          comentar, comprar, etc

          """

        else:

          if p["vista"]!="logs":
           #redirecter("",settings.app,"logs")()
           pass

          else:

           if "args" not in p:

            
            reporte=data["model"]["main"].reportarError(errores)
            
            data["errores"]=reporte[0]
            if data["errores"]:

             data["errores_link"]="app="+settings.app+"&admin=True&args={'ticket':'"+reporte[1]+"'}&vista=logs"
            else:
             HEADERS.show()
             print "No se a podido crear el ticket"
            












except Exception, e:
 HEADERS.show()
 print "error en el subcontrolador vistas:<br>"
 print e






