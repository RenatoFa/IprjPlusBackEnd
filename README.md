# IPRJ PLUS - Backend

## Português:

O **IPRJ PLUS** é uma aplicação mobile desenvolvida como Trabalho de Conclusão de Curso (TCC) no Instituto Politécnico da UERJ. Seu objetivo é promover a comunicação entre alunos e professores de forma ágil, moderna e funcional, reunindo recursos inspirados em redes sociais para o ambiente acadêmico.

Este repositório contém o backend da aplicação, desenvolvido em **Django** e **Django REST Framework**, responsável por gerenciar autenticação de usuários, gerenciamento de perfis e operações relacionadas a tweets acadêmicos.

### Funcionalidades

- Criação e autenticação de contas com envio de e-mail (via Brevo SMTP).
- Edição de perfil com avatar (integrado ao Cloudinary).
- Publicação, listagem e remoção de tweets acadêmicos.
- Sistema de OTP para verificação de acesso.
- API REST robusta com endpoints organizados e seguros.

### Tecnologias Utilizadas

- Python 3.12
- Django 5
- Django REST Framework
- Cloudinary (upload de imagens)
- Brevo SMTP (envio de e-mails)
- SQLite (banco local para testes)

### Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/IprjPlusBackEnd.git
cd IprjPlusBackEnd
```

2. Instale as dependências com o [uv](https://github.com/astral-sh/uv):
```bash
uv sync
```

3. Execute as migrações e o servidor:
```bash
python manage.py migrate
python manage.py runserver
```

## English:

**IPRJ PLUS** is a mobile application developed as a Graduation Project at the Polytechnic Institute of UERJ. Its purpose is to foster agile and modern communication between students and professors, incorporating features inspired by social media into the academic environment.

This repository hosts the backend, built using **Django** and **Django REST Framework**, which handles user authentication, notifications, profile management, and academic tweet operations.

### Features

- Account creation and login with email verification (via Brevo SMTP).
- Profile editing with avatar support (Cloudinary integration).
- Publishing, listing, and deleting academic tweets.
- OTP-based access verification.
- Secure and well-structured RESTful API.

### Technologies Used

- Python 3.12
- Django 5
- Django REST Framework
- Cloudinary (image upload)
- Brevo SMTP (email sending)
- SQLite (local testing database)

### How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/IprjPlusBackEnd.git
cd IprjPlusBackEnd
```

2. Install dependencies using [uv](https://github.com/astral-sh/uv):
```bash
uv sync
```

3. Run migrations and start the server:
```bash
python manage.py migrate
python manage.py runserver
```
