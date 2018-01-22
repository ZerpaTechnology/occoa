doc+='''
'''
try: doc+=str(incluir(data,"flash-help",isglobal=True))
except Exception, e: doc+=str(e)
doc+='''
<section class="container-fluid sin-pad ">

'''
data["versiones"]=len(data["model"]["main"].db.tablas[str(data["metodo"])+"-"+str(data["args"][1])] ) if str(data["metodo"])+"-"+str(data["args"][0]) in  data["model"]["main"].db.tablas else None
doc+='''
<div>

<link href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/tinymce/js/tinymce/skins/lightgray/content.min.css" rel="stylesheet" type="text/css">

<div class="row">
<div class="col-md-9">

<div>
  
 <span class="alg-top">Enlace: </span><div class="width-28-xs" style="overflow-x:scroll;display:inline-block"><a name="preview-enlace" href="'''
try: doc+=str(urlBuilder(config,data['app'],data['control-post'],data['post']) )
except Exception, e: doc+=str(e)
doc+='''">'''
try: doc+=str(urlBuilder(config,data['app'],data['control-post'],data['post']))
except Exception, e: doc+=str(e)
doc+='''</a></div>
</div>
  

<div class="hidden" id="vars">
'''
try: doc+=str(data["categorias"])
except Exception, e: doc+=str(e)
doc+='''
</div>


<form id="form" method="post" action="'''
try: doc+=str(config.base_url+settings.app+'/'+data['control']+'/'+data['metodo']+('/'+'/'.join( [str(elem) for elem in data['args']] )))
except Exception, e: doc+=str(e)
doc+='''/action=save" enctype='multipart/form-data' onsubmit="return window.modificar_atributo();">
'''
args=data['metodo']
doc+='''

'''
if normalizar(data['args'][0])==None and data['metodo']!='login':
  doc+='''

 '''
  btn="Registrar"
  doc+='''
'''
elif data['metodo']=='login':
  doc+='''
 '''
  btn="Entrar"
  doc+='''
'''
else:
  doc+='''
 '''
  btn="Guardar"
  doc+='''
'''
  pass
doc+=''' 

<div class="pad-1 b-s1 marg-1 bg-ubuntu_porcelain" id="edit" '''
try: doc+=str('new='+str(data['repeate']) if 'new' in data and 'repeate' in data else '')
except Exception, e: doc+=str(e)
doc+='''> 
<h1>'''
try: doc+=str(data["titulo"])
except Exception, e: doc+=str(e)
doc+='''</h1>
<hr class="height-1 bg-ubuntu_blue">
'''
if data["versiones"]!=None:
  doc+='''
<div class="ff marg-b1">
  '''
  for elem in range(data["versiones"]-1):
    doc+='''
  <span class="btn bg-gray sin-marg b-r5 btn-version">'''
    try: doc+=str(elem)
    except Exception, e:     doc+=str(e)
    doc+='''</span>
  '''
    pass
  doc+='''

  <span class="btn bg-gray b-r5 btn-version">version actual</span>
  <span class="btn bg-bluelight white b-r5" id="ir-version" >ir a la version</span>
</div>
'''
  pass
doc+='''
<div id="edit-box">

'''
if "boxes" in data:
  doc+='''
'''
  try: doc+=str(incluir(data,"edit-box",isglobal=True))
  except Exception, e:   doc+=str(e)
  doc+=''' 
'''
  pass
doc+='''
</div>


</div>


<input type="submit" id="enviar" value="'''
try: doc+=str(btn)
except Exception, e: doc+=str(e)
doc+='''" class="btn bg-blue white pad-05 b-r5">
<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/brython/nuevo.by">
</script>

<div id="tablas">
 
</div>

</form>
<form id="metadatos">

  
</form>
<button id="insertar" class="hidden">Insertar Tabla</button>
<div>
 <!-- plugins inicio-->
 '''
for elem in data["plugins-hooks"]:
  doc+='''
    
    '''
  if data["action"]==elem[0]:
    doc+='''
    '''
    try: doc+=str(do_shortcode(elem[1]))
    except Exception, e:     doc+=str(e)
    doc+=''' 
    '''
    pass
  doc+='''
    '''
  pass
doc+='''
    
 <!-- plugins fin-->
 
</div>
</div>
<aside class="col-md-3 font-ubuntu">
 '''
try: doc+=str(incluir(data,"publicar-box",isglobal=True))
except Exception, e: doc+=str(e)
doc+='''
 <br>
 '''
try: doc+=str(incluir(data,"atributo-de-pagina",isglobal=True))
except Exception, e: doc+=str(e)
doc+='''
 
 <br>
 <div class="bg-white hidden">
  <a href=""  style="text-decoration: none;color:black">
  <div class="b-s1 pad-05">
   <span><b>Imagen destacada</b></span>
  </div>
  </a>
  <div>
  
  <div class="pad-1 font-s12  height-3  text-center">
   <a href="" class="blue" style="text-decoration: none"><b>Asignar imagen destacada</b></a>
  </div>
 </div>
</aside>
</div>
</div>
<div class="hidden bg-white" id="custom" style="width: 80%;height:500px;position: fixed;top:20px;left:10%;z-index: 100 ">
<style type="text/css">
  #custom-close{
  position: absolute;
  right: -10px;
  top:-10px;
  background-color: gray;
  color:white;
  border: solid;
  border-width: 1px;
  border-radius: 15px;
  padding: 5px;
  cursor: pointer;

  }
  .botonera{
    position: absolute;
    padding: 5px;
    bottom: 0px
  }
</style>
<span id="custom-close">x</span>
  <div class="tab" style="overflow-y: scroll;height: 470px">
  '''
for i in range(20):
  doc+='''
  <div class="custom"></div>
  '''
  pass
doc+=''' 
  </div>
  <div class="botonera">
    <button class="insertar">insertar</button>
    <button class="borrar">Borrar</button>
  </div>
</div>
<div class="hidden bg-white" id="custom2" style="width: 80%;height:500px;position: fixed;top:20px;left:10%;z-index: 100 ">
<style type="text/css">
  #custom-close2{
  position: absolute;
  right: -10px;
  top:-10px;
  background-color: gray;
  color:white;
  border: solid;
  border-width: 1px;
  border-radius: 15px;
  padding: 5px;
  cursor: pointer;

  }
  .botonera{
    position: absolute;
    padding: 5px;
    bottom: 0px
  }
</style>
<span id="custom-close2">x</span>
  <div class="tab" style="overflow-y: scroll;height: 470px">
  '''
try: doc+=str(incluir(data,"widget-campo",isglobal=True))
except Exception, e: doc+=str(e)
doc+='''
  <div class="botonera">
    <button class="agregar">insertar</button>
  </div>
</div>

<!--<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/brython/edit.by"></script>-->
</section>
<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/brython/edit-box.by"></script>

'''