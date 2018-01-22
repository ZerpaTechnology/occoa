#!/usr/bin/python
# -*- coding: utf-8 -*-
doc+='''<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8" />\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">\n<title>Cyrus Studio</title>\n\n<!-- Google fonts -->\n<link href='http://fonts.googleapis.com/css?family=Roboto:400,300,700' rel='stylesheet' type='text/css'>\n\n<!-- font awesome -->\n<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">\n\n<!-- bootstrap -->\n<link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/bootstrap/css/bootstrap.min.css" />\n\n<!-- animate.css -->\n<link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/animate/animate.css" />\n<link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/animate/set.css" />\n\n<!-- gallery -->\n<link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/gallery/blueimp-gallery.min.css">\n\n<!-- favicon -->\n<link rel="shortcut icon" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/favicon.ico" type="image/x-icon">\n<link rel="icon" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/favicon.ico" type="image/x-icon">\n\n\n<link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/style.css">\n\n</head>\n\n<body>\n<div class="topbar animated fadeInLeftBig"></div>\n\n<!-- Header Starts -->\n<div class="navbar-wrapper">\n      <div class="container">\n\n        <div class="navbar navbar-default navbar-fixed-top" role="navigation" id="top-nav">\n          <div class="container">\n            <div class="navbar-header">\n              <!-- Logo Starts -->\n              <a class="navbar-brand" href="#home"><img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/logo.png" alt="logo"></a>\n              <!-- #Logo Ends -->\n\n\n              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n\n            </div>\n\n\n            <!-- Nav Starts -->\n            <div class="navbar-collapse  collapse">\n              <ul class="nav navbar-nav navbar-right scroll">\n                 <li class="active"><a href="#works">Home</a></li>\n                 <li ><a href="#about">About</a></li>\n                 <li ><a href="#partners">Partners</a></li>\n                 <li ><a href="#contact">Contact</a></li>\n              </ul>\n            </div>\n            <!-- #Nav Ends -->\n\n          </div>\n        </div>\n\n      </div>\n    </div>\n<!-- #Header Starts -->\n\n\n\n\n\n<section id="portafolio-comp" class="Components">\n  \n</section>\n'''
#incluir(data,"test")
doc+='''\n<!-- works -->\n'''
try: doc+=str(do_shortcode("[Portafolio-estilo1]"))
except Exception as e: doc+=str(e)
doc+='''\n<!-- works -->\n\n\n\n\n\n\n<!-- Cirlce Starts -->\n<div id="about"  class="container spacer about">\n<h2 class="text-center wowload fadeInUp">Creative digital agency based on London</h2>  \n  <div class="row">\n  <div class="col-sm-6 wowload fadeInLeft">\n    <h4><i class="fa fa-paint-brush"></i> Design</h4>\n    <p>Creative digital agency for sleek and sophisticated solutions for mobile, websites and software designs, lead by passionate and uber progressive team that lives and breathes design. Creative digital agency for sleek and sophisticated solutions for mobile, websites and software designs.</p>\n    \n\n  </div>\n  <div class="col-sm-6 wowload fadeInRight">\n  <h4><i class="fa fa-code"></i> Frontend & Backend Development</h4>\n  <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.</p>    \n  </div>\n  </div>\n\n  <div class="process">\n  <h3 class="text-center wowload fadeInUp">Process</h3>\n  <ul class="row text-center list-inline  wowload bounceInUp">\n      <li>\n            <span><i class="fa fa-history"></i><b>Research</b></span>\n        </li>\n        <li>\n            <span><i class="fa fa-puzzle-piece"></i><b>Plan</b></span>\n        </li>\n        <li>\n            <span><i class="fa fa-database"></i><b>Develop</b></span>\n        </li>\n        <li>\n            <span><i class="fa fa-magic"></i><b>Integration</b></span>\n        </li>        \n        <li>\n            <span><i class="fa fa-cloud-upload"></i><b>Deliver</b></span>\n        </li>\n    </ul>\n  </div>\n</div>\n<!-- #Cirlce Ends -->\n\n\n\n<!-- About Starts -->\n<div class="highlight-info">\n<div class="overlay spacer">\n<div class="container">\n<div class="row text-center  wowload fadeInDownBig">\n  <div class="col-sm-3 col-xs-6">\n  <i class="fa fa-smile-o  fa-5x"></i><h4>24 Clients</h4>\n  </div>\n  <div class="col-sm-3 col-xs-6">\n  <i class="fa fa-rocket  fa-5x"></i><h4>75 Projects</h4>\n  </div>\n  <div class="col-sm-3 col-xs-6">\n  <i class="fa fa-cloud-download  fa-5x"></i><h4>454 Downloads</h4>\n  </div>\n  <div class="col-sm-3 col-xs-6">\n  <i class="fa fa-map-marker fa-5x"></i><h4>2 Offices</h4>\n  </div>\n</div>\n</div>\n</div>\n</div>\n<!-- About Ends -->\n\n\n\n\n\n\n\n<div id="partners" class="container spacer ">\n	<h2 class="text-center  wowload fadeInUp">Some of our happy clients</h2>\n  <div class="clearfix">\n    <div class="col-sm-6 partners  wowload fadeInLeft">\n         <img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/partners/1.jpg" alt="partners">\n         <img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/partners/2.jpg" alt="partners">\n         <img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/partners/3.jpg" alt="partners">\n         <img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/partners/4.jpg" alt="partners">\n    </div>\n    <div class="col-sm-6">\n\n\n    <div id="carousel-testimonials" class="carousel slide testimonails  wowload fadeInRight" data-ride="carousel">\n    <div class="carousel-inner">  \n      <div class="item active animated bounceInRight row">\n      <div class="animated slideInLeft col-xs-2"><img alt="portfolio" src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/team/1.jpg" width="100" class="img-circle img-responsive"></div>\n      <div  class="col-xs-10">\n      <p> I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. </p>      \n      <span>Angel Smith - <b>eshop Canada</b></span>\n      </div>\n      </div>\n      <div class="item  animated bounceInRight row">\n      <div class="animated slideInLeft col-xs-2"><img alt="portfolio" src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/team/2.jpg" width="100" class="img-circle img-responsive"></div>\n      <div  class="col-xs-10">\n      <p>No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful.</p>\n      <span>John Partic - <b>Crazy Pixel</b></span>\n      </div>\n      </div>\n      <div class="item  animated bounceInRight row">\n      <div class="animated slideInLeft  col-xs-2"><img alt="portfolio" src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/team/3.jpg" width="100" class="img-circle img-responsive"></div>\n      <div  class="col-xs-10">\n      <p>On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue.</p>\n      <span>Harris David - <b>Jet London</b></span>\n      </div>\n      </div>\n  </div>\n\n   <!-- Indicators -->\n   	<ol class="carousel-indicators">\n    <li data-target="#carousel-testimonials" data-slide-to="0" class="active"></li>\n    <li data-target="#carousel-testimonials" data-slide-to="1"></li>\n    <li data-target="#carousel-testimonials" data-slide-to="2"></li>\n  	</ol>\n  	<!-- Indicators -->\n  </div>\n\n\n\n    </div>\n  </div>\n\n\n<!-- team -->\n<h3 class="text-center  wowload fadeInUp">Our team</h3>\n<p class="text-center  wowload fadeInLeft">Our creative team that is making everything possible</p>\n<div class="row grid team  wowload fadeInUpBig">	\n	<div class=" col-sm-3 col-xs-6">\n	<figure class="effect-chico">\n        <img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/team/8.jpg" alt="img01" class="img-responsive" />\n        <figcaption>\n            <p><b>Barbara Husto</b><br>Senior Designer<br><br><a href="#"><i class="fa fa-dribbble"></i></a> <a href="#"><i class="fa fa-facebook"></i></a> <a href="#"><i class="fa fa-twitter"></i></a></p>            \n        </figcaption>\n    </figure>\n    </div>\n\n    <div class=" col-sm-3 col-xs-6">\n	<figure class="effect-chico">\n        <img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/team/10.jpg" alt="img01"/>\n        <figcaption>            \n            <p><b>Barbara Husto</b><br>Senior Designer<br><br><a href="#"><i class="fa fa-dribbble"></i></a> <a href="#"><i class="fa fa-facebook"></i></a> <a href="#"><i class="fa fa-twitter"></i></a></p>            \n        </figcaption>\n    </figure>\n    </div>\n\n    <div class=" col-sm-3 col-xs-6">\n	<figure class="effect-chico">\n        <img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/team/12.jpg" alt="img01"/>\n        <figcaption>\n            <p><b>Barbara Husto</b><br>Senior Designer<br><br><a href="#"><i class="fa fa-dribbble"></i></a> <a href="#"><i class="fa fa-facebook"></i></a> <a href="#"><i class="fa fa-twitter"></i></a></p>          \n        </figcaption>\n    </figure>\n    </div>\n\n    <div class=" col-sm-3 col-xs-6">\n	<figure class="effect-chico">\n        <img src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/images/team/17.jpg" alt="img01"/>\n        <figcaption>\n            <p><b>Barbara Husto</b><br>Senior Designer<br><br><a href="#"><i class="fa fa-dribbble"></i></a> <a href="#"><i class="fa fa-facebook"></i></a> <a href="#"><i class="fa fa-twitter"></i></a></p>\n        </figcaption>\n    </figure>\n    </div>\n\n \n</div>\n<!-- team -->\n\n</div>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<!--Contact Starts-->\n<div id="contact" class="spacer">\n\n<div class="container contactform center">\n<h2 class="text-center  wowload fadeInUp">Get in touch to start your project</h2>\n  <div class="row wowload fadeInLeftBig">      \n      <div class="col-sm-6 col-sm-offset-3 col-xs-12">      \n        <input type="text" placeholder="Name">\n        <input type="text" placeholder="Company">\n        <textarea rows="5" placeholder="Message"></textarea>\n        <button class="btn btn-primary"><i class="fa fa-paper-plane"></i> Send</button>\n      </div>\n  </div>\n\n\n\n</div>\n</div>\n<!--Contact Ends-->\n\n\n\n<!-- Footer Starts -->\n<div class="footer text-center spacer">\n<p class="wowload flipInX"><a href="#"><i class="fa fa-facebook fa-2x"></i></a> <a href="#"><i class="fa fa-instagram fa-2x"></i></a> <a href="#"><i class="fa fa-twitter fa-2x"></i></a> <a href="#"><i class="fa fa-flickr fa-2x"></i></a> </p>\nCopyright 2014 Cyrus Creative Studio. All rights reserved.\n</div>\n<!-- # Footer Ends -->\n<a href="#works" class="gototop "><i class="fa fa-angle-up  fa-3x"></i></a>\n\n\n\n\n\n<!-- The Bootstrap Image Gallery lightbox, should be a child element of the document body -->\n<div id="blueimp-gallery" class="blueimp-gallery blueimp-gallery-controls">\n    <!-- The container for the modal slides -->\n    <div class="slides"></div>\n    <!-- Controls for the borderless lightbox -->\n    <h3 class="title">Title</h3>\n    <a class="prev">‹</a>\n    <a class="next">›</a>\n    <a class="close">×</a>\n    <!-- The modal dialog, which will be used to wrap the lightbox content -->    \n</div>\n\n\n\n<!-- jquery -->\n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/jquery.js"></script>\n\n<!-- wow script -->\n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/wow/wow.min.js"></script>\n\n\n<!-- boostrap -->\n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/bootstrap/js/bootstrap.js" type="text/javascript" ></script>\n\n<!-- jquery mobile -->\n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/mobile/touchSwipe.min.js"></script>\n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/respond/respond.js"></script>\n\n<!-- gallery -->\n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/gallery/jquery.blueimp-gallery.min.js"></script>\n\n<!-- custom script -->\n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/assets/script.js"></script>\n<script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/python/__javascript__/portafolio.js"></script>\n\n\n</body>\n</html>'''