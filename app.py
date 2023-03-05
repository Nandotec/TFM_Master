"""Modulos/Paquetes"""
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, make_response

"""Variables"""
app = Flask(__name__)
app.secret_key = "MCS10AED_JJ"
piezas = ["3f5", "349", "72f", "40f", "9b5", "854", "073", "c2e", "4ee", "afe", "f6"]

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
	return nombre+identificador+".html"

"""Llamadas por pagina/ejercicio"""
#Landing Page
@app.route("/")
def landing():
	return render_template("home.html")

#Fugas de Informacion 1
@app.route("/fugas1", methods=["POST", "GET"])
def fugas1():
	clave="a92263c38f1d4427e98d0a4a163d5c97"
	return render_template(carga(0, "fugas", "1", clave), chest=recompensa(clave))

#Fugas de Informacion 2
@app.route("/fugas2", methods=["POST", "GET"])
def fugas2():
	clave="0bb4aec1710521c12ee76289d9440817"
	return render_template(carga(1, "fugas", "2", clave), chest=recompensa(clave))

#Fugas de Informacion 3
@app.route("/fugas3", methods=["POST", "GET"])
def fugas3():
	clave="8b3491a66166e4ae03787085b30896c1"
	return render_template(carga(2, "fugas", "3", clave), chest=recompensa(clave))

#SQL Injection 1
@app.route("/SQLi1", methods=["POST", "GET"])
def SQLi1():
	clave="d5233f38eed5ca5a5fe20a3da852a3cb"
	data = request.form.get("isqli01")
	if data != None:
		conn = sqlite3.connect('static/db/SQLI01.db')
		conn.row_factory = sqlite3.Row
		resultados = conn.execute('SELECT * FROM SALON WHERE id='+data).fetchall()
		conn.close()
		return render_template(carga(3, "SQLi", "1", clave), chest=recompensa(clave), resultados=resultados)
	else:
		return render_template(carga(3, "SQLi", "1", clave), chest=recompensa(clave))


#SQL Injection 2
@app.route("/SQLi2", methods=["POST", "GET"])
def SQLi2():
	clave="5eaababec40751903437c1ee9c4f7e94"
	data = request.form.get("isqli02")
	if data != None:
		conn = sqlite3.connect('static/db/SQLI02.db')
		conn.row_factory = sqlite3.Row
		try:
			resultados = conn.execute('SELECT * FROM SALON WHERE id='+data).fetchall()
			flash("Success", "SQLSuccess")
			return render_template(carga(4, "SQLi", "2", clave), chest=recompensa(clave), resultados=resultados)
		except sqlite3.DatabaseError:
			flash("Database error: No elements found for id=" + data + " for table SALON, check syntax. Error code:" + clave, "SQLError")
			return render_template(carga(4, "SQLi", "2", clave), chest=recompensa(clave))

		conn.close()		
	else:
		return render_template(carga(4, "SQLi", "2", clave), chest=recompensa(clave))

#SQL Injection 3
@app.route("/SQLi3", methods=["POST", "GET"])
def SQLi3():
	clave="f7e9050c92a851b0016442ab604b0488"
	data = request.form.get("isqli03")
	if data != None:
		conn = sqlite3.connect('static/db/SQLI03.db')
		conn.row_factory = sqlite3.Row
		resultados = conn.execute('SELECT nombre,apellido,calificacion FROM SALON WHERE id='+data).fetchall()
		conn.close()
		return render_template(carga(5, "SQLi", "3", clave), chest=recompensa(clave), resultados=resultados)
	else:
		return render_template(carga(5, "SQLi", "3", clave), chest=recompensa(clave))

#Cross Site Scripting 1
@app.route("/XSS1", methods=["POST", "GET"])
def XSS1():
	clave="871c14878fa75bc327ba87d2d284d596"
	return render_template(carga(6, "XSS", "1", clave), chest=recompensa(clave))

#Cross Site Scripting 2
@app.route("/XSS2", methods=["POST", "GET"])
def XSS2():
	clave="d8ae1f0b868d69547dd6377f7538eec6"
	data = request.form.get("iHola")
	if data != None:
		flash(data, "hola")
	return render_template(carga(7, "XSS", "2", clave), chest=recompensa(clave), holaM=data)

#Cross Site Scripting 3
@app.route("/XSS3", methods=["POST", "GET"])
def XSS3():
	clave="625f96daee918472f22d00a89da74b55"
	data = request.form.get("iHola")
	if data != None:
		flash(data, "hola")
	return render_template(carga(8, "XSS", "3", clave), chest=recompensa(clave), holaM=data)

#Cookie version
@app.route("/CSRF1", methods=["POST", "GET"])
def CSRF1():
	#"Base de Datos Hard Code"
	clave="9972fa89a49bd697185da4788172a1a8"
	cAdminOriginal="e661e42b6cd1a627512d70462074fa22"

	#Interacciones con botones
	dLogin = request.form.get("iUsuario")
	dPassword = request.form.get("iContrasena")
	dCambio = request.form.get("iCambio")
	dLogout = request.form.get("iLogout")
	dURLpwd = request.args.get('contrasena')
	
	if dLogout != None:
		flash(request.cookies.get('guestpwd'), "guestpwd")
		flash(request.cookies.get('adminpwd'), "adminpwd")
		flash("login", "display")
		response = make_response(render_template(carga(9, "CSRF", "1", clave), chest=recompensa(clave)))
		response.set_cookie('username', "0", max_age=0)
		return response

	elif (dLogin != None and dPassword != None 
		and ((dLogin == "admin" and dPassword == request.cookies.get('adminpwd')) 
		or (dLogin == "guest" and dPassword == request.cookies.get('guestpwd')))):
		
		if(dLogin == "admin"):
			flash("admin", "display")
		else:
			flash("change", "display")
		if(dLogin == request.cookies.get('username')):
			flash(request.cookies.get('username'), "session")
		else:
			flash(dLogin, "session")
		if dLogin == "admin" and dPassword != cAdminOriginal:
			flash("Parece que la contraseña cambio :) Clave del reto: " + "9972fa89a49bd697185da4788172a1a8", "clave")
		response = make_response(render_template(carga(9, "CSRF", "1", clave), chest=recompensa(clave)))
		response.set_cookie('username', dLogin, max_age=1800)

		return response

	elif dCambio != None:
		return redirect("/CSRF1?contrasena=" + dCambio)
	
	elif dURLpwd != None:
		if request.cookies.get('username') == "admin":
			flash("admin", "display")
			flash(request.cookies.get('username'), "session")
		elif request.cookies.get('username') == "guest":
			flash("change", "display")
			flash(request.cookies.get('username'), "session")
		else:
			flash("login", "display")
		flash(request.cookies.get('username'), "user")
		flash(dURLpwd, "password")
		if request.cookies.get('username') == "admin" and dURLpwd != cAdminOriginal:
			flash("Parece que la contraseña cambio :) Clave del reto: " + "9972fa89a49bd697185da4788172a1a8", "clave")
		response = make_response(render_template(carga(9, "CSRF", "1", clave), chest=recompensa(clave)))
		if request.cookies.get('username') == "admin":
			response.set_cookie('adminpwd', dURLpwd, max_age=1800)
		elif request.cookies.get('username') == "guest":
			response.set_cookie('guestpwd', dURLpwd, max_age=1800)
		return response
	
	elif request.cookies.get('username') != None:
		if(request.cookies.get('username') == "admin"):
			flash("admin", "display")
		else:
			flash("change", "display")
		flash(request.cookies.get('username'), "session")
		if request.cookies.get('username') == "admin" and request.cookies.get('adminpwd') != cAdminOriginal:
			flash("Parece que la contraseña cambio :) Clave del reto: " + "9972fa89a49bd697185da4788172a1a8", "clave")
		response = make_response(render_template(carga(9, "CSRF", "1", clave), chest=recompensa(clave)))
		return response

	else:
		flash("login", "display")
		if request.cookies.get('guestpwd') == None:
			flash("12345", "guestpwd")
			flash("e661e42b6cd1a627512d70462074fa22", "adminpwd")
		else:
			flash(request.cookies.get('guestpwd'), "guestpwd")
			flash(request.cookies.get('adminpwd'), "adminpwd")
		response = make_response(render_template(carga(9, "CSRF", "1", clave), chest=recompensa(clave)))
		if request.cookies.get('guestpwd') == None:
			response.set_cookie('guestpwd', "12345", max_age=1800)
		if request.cookies.get('adminpwd') == None:
			response.set_cookie('adminpwd', "e661e42b6cd1a627512d70462074fa22", max_age=1800) 
		return response

#Cross Site Request Forgery 2
@app.route("/CSRF2", methods=["POST", "GET"])
def CSRF2():
	clave="64e4cda19b3f3ea4a7a56b5ba8cc33ca"
	return render_template(carga(10, "CSRF", "2", clave), chest=recompensa(clave))