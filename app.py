from functools import wraps
from datetime import datetime, time

from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

from controllers.auth_controller import AuthController
from model.usuario_model import UsuarioModel

app = Flask(
    __name__,
    template_folder="views/templates",
    static_folder="views/templates/static",
    static_url_path="/static"
)
app.secret_key = "segredo_de_estado"

# configuração do banco de dados
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "admin",
    "database": "sistema_login"
}

db = mysql.connector.connect(**DB_CONFIG)
model = UsuarioModel(db)
controller = AuthController(model)

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("user_id"):
            flash("Faça login para acessar essa página.", "warning")
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapper

@app.route("/")
def home():
    if session.get("user_id"):
        return redirect(url_for("dashboard"))
    return redirect(url_for("cadastro"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return controller.login(request)
    return render_template("login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        return controller.cadastrar(request)
    return render_template("cadastro.html")

@app.route("/dashboard")
@login_required
def dashboard():
    usuario = model.buscar_usuario_por_id(session.get("user_id"))
    return render_template("dashboard.html", usuario=usuario)


@app.route("/logout")
@login_required
def logout():
    return controller.logout()

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=True)
