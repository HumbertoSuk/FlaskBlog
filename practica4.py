from flask import Flask, request, render_template


app = Flask(__name__)


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
