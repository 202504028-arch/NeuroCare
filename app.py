# =====================================================
# IMPORTS
# =====================================================
# Flask: el framework en si (crea la app, maneja rutas)
# render_template: para mostrar archivos .html desde templates/
# request: para leer los datos que manda un formulario (POST)
# redirect: para mandar al usuario a otra pagina despues de una accion
# session: para "recordar" quien inicio sesion mientras navega la app
from flask import Flask, render_template, request, redirect, session

# nuestra propia funcion que abre la conexion a MySQL (conexionBD.py)
from conexionBD import obtener_conexion

# funciones de seguridad para contraseñas:
# generate_password_hash -> convierte "1234" en un texto irreconocible antes de guardarlo
# check_password_hash -> compara lo que el paciente escribe contra ese texto guardado
from werkzeug.security import generate_password_hash, check_password_hash


# =====================================================
# CREAR LA APLICACION
# =====================================================
# OJO: esto va UNA SOLA VEZ en todo el archivo.
# Si se repite mas abajo, la segunda vez "borra" todas las
# rutas que ya se habian registrado arriba.
app = Flask(__name__)

# la secret_key es necesaria para poder usar session[] de forma segura.
# puede ser cualquier texto largo, entre mas dificil de adivinar mejor.
app.secret_key = "cambia_esto_por_algo_secreto"


# =====================================================
# RUTA: LOGIN (mostrar la pagina)
# =====================================================
# Esta ruta solo MUESTRA el formulario de login cuando alguien
# entra a la pagina principal (http://127.0.0.1:5000/)
@app.route("/")
def sistema_bienvenida():
    return render_template("sistema_Bienvenid.html")


# =====================================================
# RUTA: PRUEBA DE CONEXION A LA BASE DE DATOS
# =====================================================
# Ruta temporal, solo para confirmar que Flask si puede hablar
# con MySQL. Cuenta cuantos pacientes hay registrados.
@app.route("/test-db")
def test_db():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM paciente")
    resultado = cursor.fetchone()
    conexion.close()
    return f"Conexión exitosa. Pacientes registrados: {resultado[0]}"

@app.route("/seleccionRoll")
def seleccion_roll():
    return render_template("seleccionRoll.html")

# =====================================================
# RUTA: REGISTRO DE PACIENTE
# =====================================================
# methods=["GET", "POST"] porque esta MISMA ruta hace 2 cosas:
# - GET  -> cuando alguien entra a la pagina, solo muestra el formulario vacio
# - POST -> cuando le dan clic a "Crear cuenta", recibe y guarda los datos
@app.route("/registroPaciente", methods=["GET", "POST"])
def registro_paciente():

    # si el navegador esta ENVIANDO datos (le dieron submit al formulario)...
    if request.method == "POST":

        # ---- leer cada campo del formulario por su "name" ----
        nombreCompleto = request.form["nombreCompleto"]
        fechaNacimiento = request.form["fechaNacimiento"]
        telefono = request.form["telefono"]
        correo = request.form["correo"]
        sexo = request.form["sexo"]
        peso = request.form["peso"]
        altura = request.form["altura"]
        tipoSangre = request.form["tipoSangre"]
        alergias = request.form["alergias"]
        enfermedadCronica = request.form["enfermedadCronica"]
        contrasena = request.form["contrasena"]
        confirmar_contrasena = request.form["confirmar_contrasena"]

        # ---- validacion simple: las 2 contraseñas deben coincidir ----
        if contrasena != confirmar_contrasena:
            return "Las contraseñas no coinciden. Regresa e inténtalo de nuevo."

        # ---- encriptar la contraseña antes de guardarla ----
        # nunca se guarda la contraseña real, solo este "hash"
        contrasena_hash = generate_password_hash(contrasena)

        # ---- abrir conexion a MySQL ----
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # try/except: si algo falla a la mitad, evita que la conexion
        # se quede "atorada" bloqueando la tabla para siempre
        try:
            # 1) insertar al paciente en la tabla "paciente"
            cursor.execute(
                "INSERT INTO paciente (nombreCompleto, fechaNacimiento, correo, telefono, contrasena) VALUES (%s, %s, %s, %s, %s)",
                (nombreCompleto, fechaNacimiento, correo, telefono, contrasena_hash)
            )

            # MySQL le acaba de asignar un idPaciente automatico (AUTO_INCREMENT)
            # esta linea nos dice cual fue, para poder usarlo abajo
            idPaciente = cursor.lastrowid

            # 2) insertar sus caracteristicas medicas, ligadas a ese idPaciente
            cursor.execute(
                "INSERT INTO caracteristicaspaciente (idPaciente, sexo, peso, altura, tipoSangre, alergias, enfermedadCronica) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (idPaciente, sexo, peso, altura, tipoSangre, alergias, enfermedadCronica)
            )

            # si ambos INSERT salieron bien, confirmar los cambios de verdad
            conexion.commit()
            conexion.close()

            # mandar de regreso al login para que inicie sesion con su cuenta nueva
            return redirect("/login")

        except Exception as error:
            # si algo tronó a la mitad: deshacer cualquier cambio a medias
            # y cerrar la conexion, para no dejarla bloqueada
            conexion.rollback()
            conexion.close()
            return f"Ocurrió un error al registrar: {error}"

    # si la peticion fue GET (solo entraron a ver la pagina), mostrar el formulario vacio
    return render_template("registroPaciente.html")


# =====================================================
# RUTA: LOGIN (recibir los datos del formulario)
# =====================================================
# Esta es distinta a la de arriba ("login"): esa MUESTRA la pagina,
# esta RECIBE lo que el paciente escribio y lo valida.
# Por eso se llaman distinto en Python, aunque ambas usan la URL /login y /
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        telefono = request.form["telefono"]
        contrasena = request.form["contrasena"]

        if telefono == "" or contrasena == "":
            return "Por favor completa el número de teléfono y la contraseña."

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT idPaciente, contrasena FROM paciente WHERE telefono = %s",
            (telefono,)
        )
        resultado = cursor.fetchone()
        conexion.close()

        if resultado is None:
            return "Ese número de teléfono no está registrado."

        idPaciente, contrasena_guardada = resultado

        if not check_password_hash(contrasena_guardada, contrasena):
            return "Contraseña incorrecta."

        session["idPaciente"] = idPaciente
        return redirect("/inicio")

    return render_template("login.html")
#Inicio de la aplicacion#

@app.route("/inicio")
def inicio():
    # si nadie inicio sesion (no hay idPaciente guardado), regresa al login
    if "idPaciente" not in session:
        return redirect("/")

    idPaciente = session["idPaciente"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # nombre del paciente
    cursor.execute("SELECT nombreCompleto FROM paciente WHERE idPaciente = %s", (idPaciente,))
    nombreCompleto = cursor.fetchone()[0]

    # cuantas veces jugo Memorama/Rompecabezas HOY
    cursor.execute(
        "SELECT COUNT(*) FROM historialactividad WHERE idPaciente = %s AND fecha = CURDATE()",
        (idPaciente,)
    )
    totalActividades = cursor.fetchone()[0]

    # cuantos recordatorios tiene para HOY
    cursor.execute(
        "SELECT COUNT(*) FROM recordatorios WHERE idPaciente = %s AND DATE(fechaHora) = CURDATE()",
        (idPaciente,)
    )
    totalRecordatorios = cursor.fetchone()[0]

    conexion.close()

    return render_template(
        "INICIO_PACIENTE.html",
        nombreCompleto=nombreCompleto,
        totalActividades=totalActividades,
        totalRecordatorios=totalRecordatorios
    )




#ACTVIDADES ***********#
@app.route("/actividades")
def actividades():
    if "idPaciente" not in session:
        return redirect("/")

    idPaciente = session["idPaciente"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # cuantas veces jugo Memorama (idActividad = 1)
    cursor.execute(
        "SELECT COUNT(*) FROM historialactividad WHERE idPaciente = %s AND idActividad = 1",
        (idPaciente,)
    )
    vecesMemorama = cursor.fetchone()[0]

    # cuantas veces jugo Rompecabezas (idActividad = 2)
    cursor.execute(
        "SELECT COUNT(*) FROM historialactividad WHERE idPaciente = %s AND idActividad = 2",
        (idPaciente,)
    )
    vecesRompecabezas = cursor.fetchone()[0]

    conexion.close()

    return render_template(
        "actividades.html",
        vecesMemorama=vecesMemorama,
        vecesRompecabezas=vecesRompecabezas
    )

#---------------Memorama y rompecabezas-----------------------#
@app.route("/guardar-resultado", methods=["POST"])
def guardar_resultado():
    if "idPaciente" not in session:
        return {"error": "No hay sesión activa"}, 401

    datos = request.get_json()
    idPaciente = session["idPaciente"]
    idActividad = datos["idActividad"]
    intentos = datos["intentos"]
    tiempoRealizado = datos["tiempo"]

    puntuacion = max(0, 100 - (intentos - 8) * 5)

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO historialactividad (idPaciente, idActividad, fecha, puntuacion, tiempoRealizado, completada) VALUES (%s, %s, CURDATE(), %s, %s, %s)",
        (idPaciente, idActividad, puntuacion, tiempoRealizado, True)
    )

    conexion.commit()
    conexion.close()

    return {"ok": True, "puntuacion": puntuacion}

#=============Memorama====================#

@app.route("/memorama")
def memorama():
    if "idPaciente" not in session:
        return redirect("/")
    return render_template("memorama.html")


#=============Rompecabezas====================#
@app.route("/rompecabezas")
def rompecabezas():
    if "idPaciente" not in session:
        return redirect("/")
    return render_template("rompecabezas.html")




#================avisos pagina========================#
@app.route("/avisos")
def avisos():
    if "idPaciente" not in session:
        return redirect("/")

    idPaciente = session["idPaciente"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT idRecordatorio, titulo, fechaHora, estado FROM recordatorios WHERE idPaciente = %s ORDER BY fechaHora",
        (idPaciente,)
    )
    filas = cursor.fetchall()
    conexion.close()

    # convertir cada fila a un formato que el JS ya entiende (igual al array que tenias)
    avisos_lista = []
    for fila in filas:
        idRecordatorio, titulo, fechaHora, estado = fila
        avisos_lista.append({
            "id": idRecordatorio,
            "titulo": titulo,
            "hora": fechaHora.strftime("%H:%M"),
            "completado": estado == "Completado"
        })

    return render_template("avisos.html", avisos=avisos_lista)


#================La ruta que guarda un aviso nuevo (llamada por el botón "+"):========================#

@app.route("/guardar-aviso", methods=["POST"])
def guardar_aviso():
    if "idPaciente" not in session:
        return {"error": "No hay sesión activa"}, 401

    idPaciente = session["idPaciente"]
    datos = request.get_json()
    titulo = datos["titulo"]
    hora = datos["hora"]  # viene como "14:30"

    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO recordatorios (idPaciente, titulo, tipoRecordatorio, fechaHora, estado) VALUES (%s, %s, 'Actividad', CONCAT(CURDATE(), ' ', %s), 'Pendiente')",
        (idPaciente, titulo, hora)
    )
    conexion.commit()
    idNuevo = cursor.lastrowid
    conexion.close()

    return {"ok": True, "id": idNuevo}

#==La ruta que marca/desmarca un aviso como completado (llamada al tocar el círculo)============#

@app.route("/completar-aviso/<int:idRecordatorio>", methods=["POST"])
def completar_aviso(idRecordatorio):
    if "idPaciente" not in session:
        return {"error": "No hay sesión activa"}, 401

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # obtener el estado actual para saber a cual cambiar
    cursor.execute("SELECT estado FROM recordatorios WHERE idRecordatorio = %s", (idRecordatorio,))
    estadoActual = cursor.fetchone()[0]

    nuevoEstado = "Pendiente" if estadoActual == "Completado" else "Completado"

    cursor.execute(
        "UPDATE recordatorios SET estado = %s WHERE idRecordatorio = %s",
        (nuevoEstado, idRecordatorio)
    )
    conexion.commit()
    conexion.close()

    return {"ok": True, "nuevoEstado": nuevoEstado}

#================Perfil========================#
@app.route("/perfil")
def perfil():
    if "idPaciente" not in session:
        return redirect("/")

    idPaciente = session["idPaciente"]

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # datos del paciente + sus caracteristicas, en un solo query con JOIN
    cursor.execute("""
        SELECT p.nombreCompleto, p.telefono,
               TIMESTAMPDIFF(YEAR, p.fechaNacimiento, CURDATE()) AS edad,
               c.sexo, c.peso, c.altura, c.tipoSangre, c.alergias
        FROM paciente p
        JOIN caracteristicaspaciente c ON p.idPaciente = c.idPaciente
        WHERE p.idPaciente = %s
    """, (idPaciente,))
    fila = cursor.fetchone()
    nombreCompleto, telefono, edad, sexo, peso, altura, tipoSangre, alergias = fila

    # cuantas actividades jugo en los ultimos 7 dias (semanal, a diferencia de Inicio que es solo hoy)
    cursor.execute(
        "SELECT COUNT(*) FROM historialactividad WHERE idPaciente = %s AND fecha >= DATE_SUB(CURDATE(), INTERVAL 6 DAY)",
        (idPaciente,)
    )
    ejerciciosSemana = cursor.fetchone()[0]

    conexion.close()

    return render_template(
        "perfil.html",
        nombreCompleto=nombreCompleto,
        telefono=telefono,
        edad=edad,
        sexo=sexo,
        peso=peso,
        altura=altura,
        tipoSangre=tipoSangre,
        alergias=alergias,
        ejerciciosSemana=ejerciciosSemana
    )
# =====================================================
# ARRANCAR EL SERVIDOR
# =====================================================
# esto SIEMPRE va hasta el final del archivo, despues de
# haber declarado todas las rutas de arriba
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")