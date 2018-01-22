#POST subcontroller"
if  p["app"]==settings.app and  p["multipart/form-data"]==True:
	
	if beforeAction=="Formulario":

		if data["action"].value=="Enviar":
			p["model"]["formularios"].modificarFormulario(data)
			redirecter(config,settings.app,"admin","index","Paginas",action="listar")()
		elif data["action"].value=="Registrar":
			p["model"]["formularios"].crearFormulario(data)
	elif p["cookies"]["beforeControl"]==None and p["cookies"]["beforeVista"]==None:
		
		if "Post-de-Formulario:" in data["action"].value:
			

			p["model"]["formularios"].registrarFormulario(data)
			#redirecter(config,settings.app,"index")()
	elif "Post de Formulario_" in beforeAction:
		p["model"]["formularios"].registrarFormulario(data)
		redirecter(config,settings.app,"index")()
