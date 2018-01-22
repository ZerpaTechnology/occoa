doc+='''<div class="pad-t2 pad-b2">
<form  action="'''
try: doc+=str(config.base_url+settings.app)
except Exception, e: doc+=str(e)
doc+='''/Sesion/Entrar" target="login">
		<span class="blue font-s30"><b>UNEXPO</b></span> | <span class="font-s25">WebLogin</span>
	</div>
	<div class="bg-gray b-r5 pad-3">
	<label class="font-s20">Expediente:</label>
		<input type="" name="">
	<label class="font-s20">Contraseña:</label>
		<input type="" name="">
	<input type="checkbox" name="" class="width-2 sin-marg"><span class="alg-top">Yo uso esta maquina regularmente</span>
	<input type="submit" name="" value="Entrar">
</form>
<iframe name="login" src=""></iframe>
	</div>'''