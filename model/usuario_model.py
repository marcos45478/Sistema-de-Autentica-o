class UsuarioModel:
    def __init__(self, db):
        self.db = db

    def criar_usuario(self, email, senha_hash, nome):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (email, senha, nome) VALUES (%s, %s, %s)",
                (email, senha_hash, nome)
            )
            self.db.commit()
            return True
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return False
        finally:
            cursor.close()

    def buscar_usuario(self, email):
        cursor = self.db.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT id, email, senha, nome, ativo, tentativas_login, ultimo_login FROM usuarios WHERE email = %s",
                (email,)
            )
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
        finally:
            cursor.close()

    def buscar_usuario_por_id(self, user_id):
        cursor = self.db.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT id, email, nome, ativo, tentativas_login, ultimo_login FROM usuarios WHERE id = %s",
                (user_id,)
            )
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar usuário por ID: {e}")
            return None
        finally:
            cursor.close()

    def incrementar_tentativas(self, email):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "UPDATE usuarios SET tentativas_login = tentativas_login + 1 WHERE email = %s",
                (email,)
            )
            self.db.commit()
        except Exception as e:
            print(f"Erro ao incrementar tentativas: {e}")
        finally:
            cursor.close()

    def resetar_tentativas(self, email):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "UPDATE usuarios SET tentativas_login = 0 WHERE email = %s",
                (email,)
            )
            self.db.commit()
        except Exception as e:
            print(f"Erro ao resetar tentativas: {e}")
        finally:
            cursor.close()

    def bloquear_usuario(self, email):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "UPDATE usuarios SET ativo = FALSE WHERE email = %s",
                (email,)
            )
            self.db.commit()
        except Exception as e:
            print(f"Erro ao bloquear usuário: {e}")
        finally:
            cursor.close()

    def atualizar_ultimo_login(self, email):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "UPDATE usuarios SET ultimo_login = NOW(), tentativas_login = 0 WHERE email = %s",
                (email,)
            )
            self.db.commit()
        except Exception as e:
            print(f"Erro ao atualizar último login: {e}")
        finally:
            cursor.close()

    def atualizar_senha(self, email, senha_hash):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "UPDATE usuarios SET senha = %s WHERE email = %s",
                (senha_hash, email)
            )
            self.db.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar senha: {e}")
            return False
        finally:
            cursor.close()
