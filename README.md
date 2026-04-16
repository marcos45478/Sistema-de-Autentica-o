# Sistema de Autenticação

Um sistema web seguro de autenticação desenvolvido em Python com Flask, seguindo a arquitetura MVC (Model-View-Controller). Implementa controle de acesso, validações de segurança e regras de negócio para proteger relatórios críticos da empresa.

## 🚀 Funcionalidades

- **Autenticação Segura**: Login com hash de senha usando Werkzeug
- **Controle de Acesso**: Decorator `@login_required` para rotas protegidas
- **Bloqueio por Tentativas**: Usuário bloqueado após 3 tentativas de login falhadas
- **Horário de Acesso**: Login permitido apenas entre 08h e 18h
- **Primeiro Acesso**: Troca obrigatória de senha no primeiro login
- **Sessão Flask**: Gerenciamento seguro de sessões
- **Flash Messages**: Feedback visual para o usuário
- **Arquitetura MVC**: Separação clara entre Model, View e Controller

## 🏗️ Arquitetura

### Model (model/usuario_model.py)
- Conexão com banco MySQL
- Operações CRUD para usuários
- Validações de segurança (hash de senha, tentativas, bloqueio)
- Atualização de último login

### View (views/templates/)
- Templates HTML responsivos
- Estilos CSS personalizados
- Exibição de mensagens flash
- Formulários de login e cadastro

### Controller (controllers/auth_controller.py)
- Lógica de negócio
- Validações de entrada
- Controle de fluxo (redirecionamentos)
- Integração entre Model e View

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.13+
- **Framework**: Flask 3.1+
- **Banco de Dados**: MySQL 8.0+
- **Segurança**: Werkzeug (hash de senha)
- **Frontend**: HTML5, CSS3
- **Ambiente Virtual**: venv

## 📋 Pré-requisitos

- Python 3.13 ou superior
- MySQL Server 8.0+
- Git (opcional, para versionamento)

## 🚀 Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/sistema-autenticacao.git
cd sistema-autenticacao
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install flask mysql-connector-python werkzeug
```

### 4. Configure o banco de dados MySQL

Crie o banco de dados e a tabela de usuários:

```sql
CREATE DATABASE sistema_autenticacao;

USE sistema_autenticacao;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    ativo BOOLEAN DEFAULT TRUE,
    tentativas_login INT DEFAULT 0,
    ultimo_login DATETIME NULL
);
```

### 5. Configure as credenciais do banco

Edite o arquivo `app.py` e ajuste as configurações do banco:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "seu_usuario_mysql",
    "password": "sua_senha_mysql",
    "database": "sistema_autenticacao"
}
```

## ▶️ Como Executar

1. Ative o ambiente virtual:
```bash
venv\Scripts\activate  # Windows
```

2. Execute o servidor:
```bash
python app.py
```

3. Acesse no navegador:
```
http://127.0.0.1:5001/
```

## 📖 Como Usar

### Fluxo de Autenticação

1. **Cadastro**: Acesse `/` ou `/cadastro` para criar uma conta
2. **Login**: Após cadastro, faça login em `/login`
3. **Primeiro Acesso**: Na primeira vez, será redirecionado para trocar a senha
4. **Dashboard**: Área protegida acessível após autenticação completa

### Rotas Disponíveis

- `GET /` - Página inicial (redireciona para cadastro se não logado)
- `GET/POST /cadastro` - Formulário de cadastro
- `GET/POST /login` - Formulário de login
- `GET/POST /primeiro-acesso` - Troca de senha no primeiro acesso
- `GET /dashboard` - Área protegida (requer login)
- `GET /logout` - Logout do sistema
- `GET /reset` - Limpa sessão (para testes)

## 🔒 Regras de Segurança

- **Hash de Senha**: Senhas armazenadas com hash SHA-256
- **Tentativas Limitadas**: Máximo 3 tentativas de login
- **Horário Restrito**: Acesso permitido apenas das 08h às 18h
- **Sessão Segura**: Uso de `session` do Flask com secret_key
- **Validação de Entrada**: Sanitização de dados de formulário

## 🧪 Testes

Para testar o sistema:

1. Acesse `/reset` para limpar qualquer sessão ativa
2. Vá para `/` (será redirecionado para cadastro)
3. Cadastre um novo usuário
4. Faça login
5. Teste as validações de segurança

## 📁 Estrutura do Projeto

```
sistema-autenticacao/
├── app.py                      # Aplicação principal Flask
├── controllers/
│   ├── __init__.py
│   └── auth_controller.py      # Controller de autenticação
├── model/
│   ├── __init__.py
│   └── usuario_model.py        # Model de usuário
├── views/
│   └── templates/
│       ├── login.html
│       ├── cadastro.html
│       ├── dashboard.html
│       ├── primeiro_acesso.html
│       └── static/
│           ├── login.css
│           ├── cadastro.css
│           └── deshboard.css
├── venv/                       # Ambiente virtual
├── README.md                   # Documentação
└── .git/                       # Controle de versão
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no repositório ou entre em contato com a equipe de desenvolvimento.

---

**Desenvolvido com ❤️ para demonstrar boas práticas de desenvolvimento web seguro.**
