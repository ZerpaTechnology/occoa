doc+='''<div class="b-r12 width-100p z-index5" id="nav-main">
'''
constructor2=hacer_constructor(ul_class="dropdown-menu",li_class="dropdown-submenu")
doc+='''
'''
constructor1=hacer_constructor(ul_class="dropdown-menu",li_class="dropdown-submenu",constructor=constructor2,funcion=wapper)
doc+='''

<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">
      '''
if "brand" in data:
  doc+='''
      '''
  try: doc+=str(data["brand"])
  except Exception, e:   doc+=str(e)
  doc+='''
      '''
else:
  doc+='''
      Marca
      '''
  pass
doc+='''
      </a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
    '''
try: doc+=str(main_menu(constructor=constructor1,
      funcion=wapper,
      ul_class="nav navbar-nav")
    )
except Exception, e: doc+=str(e)
doc+='''
    '''
if "main_menu-search" in data and data["main_menu-search"]==True:
  doc+='''
      <form class="navbar-form navbar-left">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
      '''
  pass
doc+='''
      <!-- MY ACCOUNT  MENU
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
          </ul>

        </li>
      </ul>
      -->
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
	<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception, e: doc+=str(e)
doc+='''static/brython/fixed.by">  </script>
'''