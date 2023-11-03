# FlaskBlog


## Definición de Rutas:
Utilizamos @app.route("/nombre_de_ruta") para definir rutas en nuestra aplicación. En el código proporcionado, se definieron cuatro rutas: la página principal ("/index") y tres páginas de artículos ("/articulo1", "/articulo2" y "/articulo3"). Cada ruta está asociada a una función de vista específica.

## Funciones de Vista:
Para cada ruta definida, se creó una función de vista que manejará esa ruta. Las funciones de vista son funciones de Python que se ejecutan cuando un usuario accede a una ruta específica. En estas funciones, se utiliza render_template para renderizar plantillas HTML. En la práctica, se renderizan las plantillas "public/index.html", "public/art1.html" y "public/art2.html", respectivamente.

## Uso de url_for:
La principal utilidad de url_for se ilustra al generar enlaces en las plantillas HTML. En la plantilla HTML, podemos usar `{{ url_for('nombre_de_funcion') }}` para generar una URL válida basada en el nombre de la función de vista asociada a una ruta. Por ejemplo, `<a href="{{ url_for('inicio') }}">` genera un enlace a la página principal, y `<a href="{{ url_for('articulo1') }}">` genera un enlace a la página del artículo 1. Esto hace que la generación de enlaces sea dinámica y evita tener que escribir las URLs directamente en el código HTML.


```python

# Index
@app.route("/index")
def inicio():
    return render_template("public/index.html")


# Articulos
@app.route("/articulo1")
def articulo1():
    return render_template("public/art1.html")


@app.route("/articulo2")
def articulo2():
    return render_template("public/Art2.html")


@app.route("/articulo3")
def articulo3():
    return render_template("public/art3.html")
```
