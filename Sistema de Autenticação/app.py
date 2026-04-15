from flask import Flask, render_template, request
import mysql.connector

from models.usuario_model import UsuarioModel
from controllers.auth_controller import AuthController

app = Flask(__name__)
app.secret_key = "segredo_de_estado"

#conexão
db = mysql.connector.connect(
    host = "localhost"
    user = "root",
    senha = "admin",
    databasse = ""
)

model = UsuarioModel(dp)
controller = AuthController(model)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return controller.logim()
    return render_template('login.html')
