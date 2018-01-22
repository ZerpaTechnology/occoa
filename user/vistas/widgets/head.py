doc+='''<head>\n    <title>Privacy Policy</title>\n    <meta charset="utf-8">\n    <meta name="format-detection" content="telephone=no">\n    <link rel="icon" href="images/favicon.ico" type="image/x-icon">\n    <link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/css/grid.css">\n    <link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/css/style.css">\n    <link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/css/google-map.css">\n    <link rel="stylesheet" href="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/css/mailform.css">\n    <script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/js/jquery.js"></script>\n    <script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/js/jquery-migrate-1.2.1.js"></script>\n    \n    <script src="'''
try: doc+=str(data['base_url'])
except Exception as e: doc+=str(e)
doc+='''static/js/device.min.js"></script>\n    <head>\n <title>Administrador</title>\n <meta charset="utf-8">\n   <meta http-equiv="pragma" content="no-cache">\n <link rel="icon" type="image/png" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/logos/logoZtec.png" />\n <link rel="shortcut icon" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/imgs/logos/logoZtec.png" />\n <script src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/jquery-3.1.0.js"></script>\n <link rel="stylesheet" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/jquery.mCustomScrollbar.css" />\n <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/jquery.mCustomScrollbar.js"></script>\n <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/estilos.css">\n <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/bootstrap.css">\n <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/flexboxgrid.css">\n <link rel="stylesheet" type="text/css" href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/ff.css">\n \n \n <link href="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/css/perfect-scrollbar.min.css" rel="stylesheet">\n \n  <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/script/file=Config.js&manager=True"></script>\n  \n  <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/Codificador.js"></script>\n  \n  <!--<script type="text/python3" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/brython/nuclear.by"></script>-->\n  <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/py_datos.js"></script>\n  <script type="text/javascript" src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''static/js/python/__javascript__/nuclear.js"></script>\n  \n  <meta name="viewport" content="width=device-width, initial-scale=1">\n \n\n \n'''
try:
 if "vars" in data:
  doc+='''\n\n'''
  try:
   for elem in data["vars"]:
    doc+="""\n<var name='"""
    try: doc+=str(elem)
    except Exception as e:     doc+=str(e)
    doc+="""' style="display: none">"""
    try: doc+=str(decode(str(data["vars"][elem])))
    except Exception as e:     doc+=str(e)
    doc+='''</var>\n'''
    pass
  except Exception as e: doc+=str(e)
  doc+='''\n'''
  pass
except Exception as e: doc+=str(e)
doc+='''\n\n\n\n\n\n\n\n  </head>\n\n'''