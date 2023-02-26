"""Modulos/Paquetes"""
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session

"""Variables"""
app = Flask(__name__)
app.secret_key = "MCS10AED_JJ"
piezas = ["3f", "53", "49", "72", "f4", "0f", "9b", "58", "54", "07", "3c", "2e", "4e", "ea", "fe", "f6"]

"""Funciones Globales"""
#Establecer conexion a la base de datos
def conexion_db():
	conexion = sqlite3.connect('static/db/database.db')
	conexion.row_factory = sqlite3.Row
	return conexion

#Apertura de Cofre
def recompensa(clave=0):
	data = request.form.get("iRespuesta")
	if data == clave:
		return "img/chest_open_bgl.png"
	else:
		return "img/chest_closed_bgl.png"

#Limpiar Sesion
def limpiar_sesion():
	session.pop('username', default=None)
	session.pop('guestpwd', default=None)
	session.pop('adminpwd', default=None)

#Cargar la pagina con contenido dinamico
def carga(indice, nombre, identificador, clave=0):
	data = request.form.get("iRespuesta")
	if data == clave:
		flash("ENHORABUENA! Esta es tu pieza: " + piezas[indice], "recompensa")
	elif data != None:
		flash("Responde la clave en el campo arriba para obtener tu recompensa!", "ayuda")
		flash("La clave ingresada no fue correcta.", "error")
	else:
		flash("Responde la clave en el campo arriba para obtener tu recompensa!", "ayuda")
	if nombre+identificador != "CSRF1":
		limpiar_sesion()
	return nombre+identificador+".html"

"""Llamadas por pagina/ejercicio"""
#Landing Page
#@app.route("/")
#def landing():
	#return render_template(carga(0, "fugas", "1"), chest=recompensa())

#Fugas de Informacion 1
@app.route("/fugas1", methods=["POST", "GET"])
def fugas1():
	clave="848d85f801e989c68a4df01d9d4c1e9e"
	return render_template(carga(0, "fugas", "1", clave), chest=recompensa(clave))

#Fugas de Informacion 2
@app.route("/fugas2", methods=["POST", "GET"])
def fugas2():
	clave="d82c8d1619ad8176d665453cfb2e55f0"
	return render_template(carga(1, "fugas", "2", clave), chest=recompensa(clave))

#Fugas de Informacion 3
@app.route("/fugas3", methods=["POST", "GET"])
def fugas3():
	clave="f457c545a9ded88f18ecee47145a72c0"
	return render_template(carga(2, "fugas", "3", clave), chest=recompensa(clave))

#Fugas de Informacion 4
@app.route("/fugas4", methods=["POST", "GET"])
def fugas4():
	clave="32bb90e8976aab5298d5da10fe66f21d"
	return render_template(carga(3, "fugas", "4", clave), chest=recompensa(clave))

#SQL Injection 1
@app.route("/SQLi1", methods=["POST", "GET"])
def SQLi1():
	clave="6e1fcd704528ad8bf6d6bbedb9210096"
	return render_template(carga(4, "SQLi", "1", clave), chest=recompensa(clave))

#SQL Injection 2
@app.route("/SQLi2", methods=["POST", "GET"])
def SQLi2():
	clave="7dff51ca8eb990122513f24ffdaa4d9a"
	#conexion= conexion_db()
	#posts = conexion.execute('SELECT * FROM posts').fetchall()
	#conexion.close()
	return render_template(carga(5, "SQLi", "2", clave), chest=recompensa(clave), posts=posts)

#SQL Injection 3
@app.route("/SQLi3", methods=["POST", "GET"])
def SQLi3():
	clave="738c8372fab9160336f3daad7fcc7e2a"
	return render_template(carga(6, "SQLi", "3", clave), chest=recompensa(clave))

#SQL Injection 4
@app.route("/SQLi4", methods=["POST", "GET"])
def SQLi4():
	clave="66f041e16a60928b05a7e228a89c3799"
	return render_template(carga(7, "SQLi", "4", clave), chest=recompensa(clave))

#Cross Site Scripting 1
@app.route("/XSS1", methods=["POST", "GET"])
def XSS1():
	clave="a684eceee76fc522773286a895bc8436"
	return render_template(carga(8, "XSS", "1", clave), chest=recompensa(clave))

#Cross Site Scripting 2
@app.route("/XSS2", methods=["POST", "GET"])
def XSS2():
	clave="d72d187df41e10ea7d9fcdc7f5909205"
	return render_template(carga(9, "XSS", "2", clave), chest=recompensa(clave))

#Cross Site Scripting 3
@app.route("/XSS3", methods=["POST", "GET"])
def XSS3():
	clave="5fcfcb7df376059d0075cb892b2cc37f"
	return render_template(carga(10, "XSS", "3", clave), chest=recompensa(clave))

#Cross Site Scripting 4
@app.route("/XSS4", methods=["POST", "GET"])
def XSS4():
	clave="bba19fea927b71d74e753f2487e107fd"
	return render_template(carga(11, "XSS", "4", clave), chest=recompensa(clave))

#Cross Site Request Forgery 1
@app.route("/CSRF1", methods=["POST", "GET"])
def CSRF1():
	clave="aea07c4d3d1709313c4bb2d07a47027d"
	dLogin = request.form.get("iUsuario")
	dPassword = request.form.get("iContrasena")
	dCambio = request.form.get("iCambio")
	dLogout = request.form.get("iLogout")
	dUsuario = request.args.get('usuario')
	dURLpwd = request.args.get('contrasena')
	if dLogout != None:
		session.pop('username', default=None)
	if (dLogin != None and dPassword != None 
		and ((dLogin == "admin" and dPassword == session['adminpwd']) 
		or (dLogin == "guest" and dPassword == session['guestpwd']))):
		
		flash("change", "display")
		session['username'] = dLogin
		flash(session['username'], "session") 
		if dLogin == "admin" and dPassword == session['adminpwd']:
			flash("Buen Dia Administrador, recordatorio que la clave del acertijo es " + "aea07c4d3d1709313c4bb2d07a47027d", "clave")
		return render_template(carga(12, "CSRF", "1", clave), chest=recompensa(clave))

	elif dCambio != None:
		return redirect("/CSRF1?usuario=" + session['username'] + "&contrasena=" + dCambio)
	
	elif dUsuario != None and dURLpwd != None:
		if session.get('username') != None:
			flash("change", "display")
			if session.get('username') != None:
				flash(session['username'], "session")
		else:
			flash("login", "display")
		if dUsuario == "admin":
			session['adminpwd'] = dURLpwd
		elif dUsuario == "guest":
			session['guestpwd'] = dURLpwd
		if session.get('guestpwd') == None:
			session['guestpwd'] = "12345"
		if session.get('adminpwd') == None:
			session['adminpwd'] = "e661e42b6cd1a627512d70462074fa22"
		flash(session['guestpwd'], "guestpwd")
		flash(dUsuario, "user")
		flash(dURLpwd, "password")
		return render_template(carga(12, "CSRF", "1", clave), chest=recompensa(clave))
	
	else:
		if session.get('guestpwd') == None:
			session['guestpwd'] = "12345"
		if session.get('adminpwd') == None:
			session['adminpwd'] = "e661e42b6cd1a627512d70462074fa22"
		flash("login", "display")
		flash(session['guestpwd'], "guestpwd")
		return render_template(carga(12, "CSRF", "1", clave), chest=recompensa(clave))
	

#Cross Site Request Forgery 2
@app.route("/CSRF2", methods=["POST", "GET"])
def CSRF2():
	clave="5b344ac52a0192941b46a8bf252c859c"
	return render_template(carga(13, "CSRF", "2", clave), chest=recompensa(clave))

#Cross Site Request Forgery 3
@app.route("/CSRF3", methods=["POST", "GET"])
def CSRF3():
	clave="2d917f5d1275e96fd75e6352e26b1387"
	return render_template(carga(14, "CSRF", "3", clave), chest=recompensa(clave))

#Cross Site Request Forgery 4
@app.route("/CSRF4", methods=["POST", "GET"])
def CSRF4():
	clave="64e4cda19b3f3ea4a7a56b5ba8cc33ca"
	return render_template(carga(15, "CSRF", "4", clave), chest=recompensa(clave))