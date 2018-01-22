doc+='''<iframe src="'''
try: doc+=str(config.base_url)
except Exception as e: doc+=str(e)
doc+='''" style="width: 100%;height: 100%;border: none">
	
</iframe>'''