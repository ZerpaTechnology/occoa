doc+='''<script type="text/javascript" src="'''
try: doc+=str(routes.widget_base_url)
except Exception as e: doc+=str(e)
doc+='''/__javascript__/bootstrap.js"></script>'''