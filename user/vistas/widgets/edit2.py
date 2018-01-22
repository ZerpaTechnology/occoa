doc+='''<div class="box text-left">
<div class="row">
<div class="col-md-2 col-xs-12">



<style type="text/css">
  .CodeMirror {border-top: 1px solid #eee; border-bottom: 1px solid #eee; line-height: 1.3; height: 500px}
  .CodeMirror-linenumbers { padding: 0 8px; }

  .folderclass:before{
   content: url("'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/imgs/iconos/007-folder.png");
   cursor: pointer;
  }
  .fileclass:before{
   content: url("'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/imgs/iconos/005-file.png");
   cursor: pointer;
  }
  #alert-close{
    position:absolute;
    right:-15px;
    top:-15px;
    border:solid;
    border-width:1px;
    border-color:white;
    border-radius:20px;
    padding:5px;
    background-color:gray;
    color:white;
  }
</style>
  <button id="titulo">
    '''
try: doc+=str(data["titulo"] if "titulo" in data else "")
except Exception, e: doc+=str(e)
doc+=''' <button id="nuevo">Crear Nuevo</button>
  </button>

 <div class="height-50 b-s1 width-100p font-s13 text-left" style="overflow-y: scroll;" id="treefiles">
 
  
  '''
try: doc+=str(data["renderTree"](data["trees"],folderclass="folderclass",fileclass="fileclass",excluir=data["excluir"]))
except Exception, e: doc+=str(e)
doc+='''
  
 
 </div>

</div>
<div class="col-md-10 col-xs-12">
 <div class="height-48 b-s1 width-100p">
<link rel=stylesheet href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/doc/docs.css">

<link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/lib/codemirror.css">
<link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/fold/foldgutter.css">
<link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/dialog/dialog.css">
<link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/theme/monokai.css">
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/lib/codemirror.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/display/autorefresh.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/search/searchcursor.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/search/search.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/dialog/dialog.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/edit/matchbrackets.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/edit/closebrackets.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/comment/comment.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/wrap/hardwrap.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/fold/foldcode.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/fold/brace-fold.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/javascript/javascript.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/python/python.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/keymap/sublime.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/selection/selection-pointer.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/xml/xml.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/javascript/javascript.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/css/css.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/vbscript/vbscript.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/mode/htmlmixed/htmlmixed.js"></script>

<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codemirror-5.27.4/addon/emmet/dist/emmet.js"></script>



<style type="text/css">
 .CodeMirror{
  height: 100% !important;
 }
 .tab-btn{
  background-color: rgb(150,100,150);
  border: none;
  color: white;
 }

</style>

<div id="tabs-btn">
  <span style="padding:2px"><button class="tab-btn">Nuevo Archivo</button><button class="close-btn">x</button></span> 
</div>
<div id="content2">
<!-- tab1-->
<div>
  <div class="tab">
  <div class="path" style="overflow-x:scroll"></div>
    <textarea class="codeEditor" class="CodeMirror cm-s-monokai" style="height: 100%">
    </textarea>  
</div>
</div>

<!-- tab2-->
<div></div>
<!-- tab3-->
<div></div>
<!-- tab4-->
<div></div>
<!-- tab5-->
<div></div>
<!-- tab6-->
<div></div>
<!-- tab7-->
<div></div>
<!-- tab8-->
<div></div>
<!-- tab9-->
<div></div>
<!-- tab10-->
<div></div>
<div id="btns-action">
<button class="bg-blue white" id="guardar">Guardar</button>  
</div>

<div id="alert" class="hidden" style="position: fixed;z-index:100">
</div>
<script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/shortcut.js"></script>
<script src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/js/codeEditor.js">
</script>

<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/brython/menu2.by"></script>

<div class="height-10"></div> 
</div> 
</div>



'''