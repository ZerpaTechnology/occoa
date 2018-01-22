doc+='''
<header id="header" style="background-image: url('''
try: doc+=str(data['base_url']+'static/img/')
except Exception, e: doc+=str(e)
doc+='''logo_unexpo_blanco.png)  !important;">
	  <!--Menu-->
		  <div class="content-menu">
		  	<div class="container">
		  		<div class="row web-cross-center">
		  			<div class="col-lg-4">
		  				<div class="logo">
		  					<img class="logo__img" src="'''
try: doc+=str(data['base_url']+'static/img/')
except Exception, e: doc+=str(e)
doc+='''logo_unexpo.png" alt="logo">
		  				</div>
		  			</div>
		  			<div class="col-lg-8">
		  				<ul class="menu">
		  					<li><a href="#">Home</a></li>
		  					<li><a href="#">About</a></li>
		  					<li><a href="portafolio.html">Portafolio</a></li>
		  					<li><a href="#">Blog</a></li>
		  					<li><a href="#">Contacto</a></li>
		  				</ul>
		  			</div>
		  		</div>
		  	</div>
		  </div>
		  <!--end Menu-->
</header>'''