doc+='''<style>
  @media(max-width:360px){
    .center-xs{
      float:inherit !important;
    }
  }
</style>
<div class="bg-ubuntu_porcelain pad-1">
<div >

<link rel="stylesheet" type="text/css" href="">
<span class="font-s50" id="table-title">'''
try: doc+=str(data["titulo"])
except Exception as e: doc+=str(e)
doc+='''</span><a class="btn bg-gray blue " href="'''
try: doc+=str(data['addNew-enlace'])
except Exception as e: doc+=str(e)
doc+='''">'''
try: doc+=str(data["addNew"])
except Exception as e: doc+=str(e)
doc+='''</a>
<hr class="height-1 bg-ubuntu_green">


<style type="text/css">
  .table-responsive > .paginacion{
    display: none;
  }
</style>
'''
data["table-headers"]=["Nombre","Ultima modificación","Descripción"]
doc+='''
'''
data["vars"]["table-headers"]=["Nombre","Ultima modificación","Descripción"]
doc+='''

<div class="table-responsive" id="tabla-1">
<span><a class="link-status"href="">Todos</a></span>
'''
for elem in data['filtros']:
  doc+='''
 <span> | <a class="link-status" href="">'''
  try: doc+=str(elem)
  except Exception as e:   doc+=str(e)
  doc+='''</a> ('''
  try: doc+=str(len(data['filtros'][elem]))
  except Exception as e:   doc+=str(e)
  doc+=''')</span>
'''
  pass
doc+='''
<nav>

<div class="d-inline-block right center-xs">
 <input type="" placeholder="Buscar..." class="search" name="table-search">
</div>

'''
if data["listar"]==None:
  doc+='''
'''
  data["listar"]=[]
  doc+='''
'''
  data["vars"]["listar"]=[]
  doc+='''
'''
  pass
doc+='''

<div class="width-60p d-inline-block width-20-xs">
 <select class="table-actions">
  '''
for elem in data["acciones"].keys():
  doc+='''
  <option >'''
  try: doc+=str(elem)
  except Exception as e:   doc+=str(e)
  doc+='''</option>
  '''
  pass
doc+='''
  
 </select>
 <button class="btn-aplicar">Aplicar</button>

 <select class="hidden">
  
  '''
for opciones in data["filtrar"]:
  doc+='''
  <option>'''
  try: doc+=str(opciones)
  except Exception as e:   doc+=str(e)
  doc+='''</option>
  '''
  pass
doc+='''
 </select>
 
 <button class="hidden">Filtrar</button>
</div>
'''
data['pag']=1
doc+='''
'''
data["vars"]['pag']=1
doc+='''

<div class="d-inline-block">
<span class="table-before"> </span>
 <button class="table-firt"><<</button>
 <button class="table-back"><</button>
 <input type="number" name="table-indice" value="'''
try: doc+=str(data['pag'])
except Exception as e: doc+=str(e)
doc+='''" class="table-pag width-5" max="'''
try: doc+=str(len(data['listar'])/data['n-pag']+1)
except Exception as e: doc+=str(e)
doc+='''" min="0" step="0"> de <span name="from-indice">'''
try: doc+=str((len(data['listar'])/data['n-pag']))
except Exception as e: doc+=str(e)
doc+='''</span>
 <span class="n-pag"></span>
 <button class="table-next">></button>
 <button class="table-last">>></button>
</div>
</nav> 

'''
try: doc+=str(incluir(data,"tabla-contenido"))
except Exception as e: doc+=str(e)
doc+='''
</div>
<nav class="tabla-nav">
 
</nav>
<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/tablas.by">
</script>
<script type="text/python3">
from browser import window
window.Tabla("#tabla-1")
</script>
</div>
'''