from datetime import datetime, time

from flask import session, redirect, url_for, flash, render_template
from werkzeug.security import generate_password_hash, check_password_hash

class AuthController:
    def __init__(self, model):
        self.model = model

    def login(self, request):
        email = request.form.get("email")
        senha = request.form.get("senha")

        usuario = self.model.buscar_usuario(email)
        if not usuario:
            flash("Usuário ou senha inválidos", "error")
            return redirect(url_for("login"))

        if not usuario["ativo"]:
            flash("Usuário bloqueado", "warning")
            return redirect(url_for("login"))

        if not self._horario_permitido():
            flash("Login permitido apenas entre 08h e 18h", "warning")
            return redirect(url_for("login"))

        if not check_password_hash(usuario["senha"], senha):
            self.model.incrementar_tentativas(email)
            if usuario["tentativas_login"] + 1 >= 3:
                self.model.bloquear_usuario(email)
                flash("Usuário bloqueado", "warning")
            else:
                flash("Usuário ou senha inválidos", "error")
            return redirect(url_for("login"))

        self.model.resetar_tentativas(email)
        self.model.atualizar_ultimo_login(email)
        session["user_id"] = usuario["id"]
        session["email"] = usuario["email"]
        session["nome"] = usuario.get("nome", "")

        flash("Login realizado com sucesso", "success")
        return redirect(url_for("dashboard"))

    def cadastrar(self, request):
        email = request.form.get("email")
        senha = request.form.get("senha")
        nome = request.form.get("nome")

        if self.model.buscar_usuario(email):
            flash("Email já está em uso.", "warning")
            return redirect(url_for("cadastro"))

        senha_hash = generate_password_hash(senha)
        if self.model.criar_usuario(email, senha_hash, nome):
            flash("Cadastro realizado com sucesso", "success")
            return redirect(url_for("login"))

        flash("Erro ao criar usuário", "error")
        return redirect(url_for("cadastro"))

    def logout(self):
        session.clear()
        flash("Logout realizado com sucesso", "success")
        return redirect(url_for("login"))

    def _horario_permitido(self):
        agora = datetime.now().time()
        inicio = time(8, 0)
        fim = time(18, 0)
        return inicio <= agora <= fim
