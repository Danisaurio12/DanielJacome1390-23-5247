# Sistema Académico — Proyecto Serie II (Desarrollo Web)

Aplicación web construida con **Flask** y **Jinja2** que cumple con los
requisitos del examen: estructura de proyecto, página de inicio con
navegación real, 4 páginas adicionales con elementos semánticos/tabla/
formulario/lista anidada/figure/ruta dinámica, CSS externo y rutas Flask.

## Estructura del proyecto

```
proyecto/
├── app.py
├── requirements.txt
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── pagina1.html      (Estudiantes)
│   ├── pagina2.html      (Cursos)
│   ├── pagina3.html      (Recursos)
│   ├── pagina4.html      (Contacto)
│   └── estudiante.html   (perfil dinámico /estudiante/<nombre>)
└── static/
    ├── estilos.css
    └── img/
        ├── logo.png
        ├── cursos.png
        └── contacto.png
```

## Instalación y ejecución

1. Crear y activar un entorno virtual:
   ```
   python -m venv venv
   venv\Scripts\activate      (Windows)
   source venv/bin/activate   (Linux/Mac)
   ```
2. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Ejecutar el servidor:
   ```
   python app.py
   ```
4. Abrir en el navegador: `http://127.0.0.1:5000`

## Nota sobre `debug=True`

En `app.py`, `app.run(debug=True)` se utiliza **únicamente para desarrollo**,
ya que habilita el recargador automático y muestra información detallada
de errores. **Debe cambiarse a `debug=False` (o eliminarse) antes de
desplegar la aplicación en un entorno de producción**, porque el modo
debug expone un depurador interactivo que permite ejecutar código en el
servidor y representa un riesgo de seguridad.

## Rutas disponibles

| Ruta                     | Método(s)   | Descripción                              |
|---------------------------|-------------|-------------------------------------------|
| `/`                        | GET         | Página de inicio                          |
| `/pagina1`                 | GET, POST   | Listado de estudiantes + formulario alta  |
| `/estudiante/<nombre>`     | GET         | Perfil dinámico de un estudiante          |
| `/pagina2`                 | GET         | Cursos                                    |
| `/pagina3`                 | GET         | Recursos y horario de tutorías            |
| `/pagina4`                 | GET, POST   | Formulario de contacto                    |

## Elementos incluidos por página (sin repetir el mismo conjunto)

- **Página 1 — Estudiantes:** tabla, formulario (GET/POST), ruta dinámica con Jinja2.
- **Página 2 — Cursos:** etiquetas semánticas (`article`), lista anidada, `figure`/`figcaption`.
- **Página 3 — Recursos:** etiquetas semánticas (`aside`), tabla, lista anidada.
- **Página 4 — Contacto:** formulario con varios `type` de `input`, `figure`/`figcaption`, etiquetas semánticas (`article`).
