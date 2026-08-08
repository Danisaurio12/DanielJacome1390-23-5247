"""
Sistema Académico - Aplicación web con Flask
SERIE II - Examen Desarrollo Web

Estructura de datos en memoria (no se usa base de datos, no lo pide el enunciado).
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------------------------------------------------------------------
# "Base de datos" en memoria: lista de estudiantes de ejemplo
# ---------------------------------------------------------------------------
estudiantes = [
    {"nombre": "Lester Miranda", "carrera": "Ing. en Sistemas", "semestre": 8},
    {"nombre": "Daniel Ramos", "carrera": "Ing. en Ciencias y Sistemas", "semestre": 8},
    {"nombre": "Ana Gómez", "carrera": "Ing. Industrial", "semestre": 5},
    {"nombre": "Carlos Pérez", "carrera": "Ing. en Sistemas", "semestre": 3},
]

# Horario de tutorías para la página de recursos
horario_tutorias = [
    {"dia": "Lunes", "hora": "14:00 - 15:00", "tema": "Bases de Datos"},
    {"dia": "Miércoles", "hora": "16:00 - 17:00", "tema": "Programación Web"},
    {"dia": "Viernes", "hora": "10:00 - 11:00", "tema": "Arquitectura de Computadoras"},
]


# ---------------------------------------------------------------------------
# Rutas
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Página de inicio (Home)."""
    return render_template("index.html", titulo="Inicio")


@app.route("/pagina1", methods=["GET", "POST"])
def pagina1():
    """
    Página de Estudiantes.
    Contiene: Tabla, Formulario (GET/POST) y enlaces a la ruta dinámica
    /estudiante/<nombre>.
    """
    mensaje = None

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        carrera = request.form.get("carrera", "").strip()
        semestre = request.form.get("semestre", "").strip()

        if nombre and carrera and semestre:
            estudiantes.append({
                "nombre": nombre,
                "carrera": carrera,
                "semestre": int(semestre),
            })
            mensaje = f"Estudiante '{nombre}' agregado correctamente."
        else:
            mensaje = "Todos los campos son obligatorios."

    return render_template(
        "pagina1.html",
        titulo="Estudiantes",
        estudiantes=estudiantes,
        mensaje=mensaje,
    )


@app.route("/estudiante/<nombre>")
def perfil_estudiante(nombre):
    """Ruta con parámetro dinámico en la URL."""
    estudiante = next(
        (e for e in estudiantes if e["nombre"].lower() == nombre.lower()), None
    )
    return render_template("estudiante.html", titulo="Perfil de Estudiante",
                            nombre=nombre, estudiante=estudiante)


@app.route("/pagina2")
def pagina2():
    """
    Página de Cursos.
    Contiene: etiquetas semánticas, lista anidada y figure/figcaption.
    """
    cursos = [
        {
            "nombre": "Desarrollo Web",
            "temas": ["HTML5 y CSS3", "Flask y Jinja2", "Bases de datos web"],
        },
        {
            "nombre": "Arquitectura de Computadoras",
            "temas": ["Von Neumann vs Harvard", "Buses del sistema", "Ciclo fetch-decode-execute"],
        },
        {
            "nombre": "Compiladores",
            "temas": ["Análisis léxico", "Análisis sintáctico", "Análisis semántico"],
        },
    ]
    return render_template("pagina2.html", titulo="Cursos", cursos=cursos)


@app.route("/pagina3")
def pagina3():
    """
    Página de Recursos.
    Contiene: etiquetas semánticas (aside), tabla y lista anidada.
    """
    recursos = {
        "Documentación": ["Flask Docs", "MDN Web Docs", "Jinja2 Docs"],
        "Herramientas": ["VS Code", "GitHub Desktop", "Postman"],
    }
    return render_template(
        "pagina3.html",
        titulo="Recursos",
        horario=horario_tutorias,
        recursos=recursos,
    )


@app.route("/pagina4", methods=["GET", "POST"])
def pagina4():
    """
    Página de Contacto.
    Contiene: formulario con distintos type de input, figure/figcaption
    y etiquetas semánticas.
    """
    confirmacion = None

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        email = request.form.get("email", "").strip()
        asunto = request.form.get("asunto", "")
        mensaje_txt = request.form.get("mensaje", "").strip()
        suscribirse = request.form.get("suscribirse")

        confirmacion = {
            "nombre": nombre,
            "email": email,
            "asunto": asunto,
            "mensaje": mensaje_txt,
            "suscribirse": "Sí" if suscribirse else "No",
        }

    return render_template("pagina4.html", titulo="Contacto", confirmacion=confirmacion)


if __name__ == "__main__":
    # debug=True solo debe usarse en desarrollo (ver README.md)
    app.run(debug=True)
