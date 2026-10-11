# Enquete Hashtag

Aplicação web de enquetes desenvolvida com Django. O projeto permite consultar perguntas recentes, escolher uma opção, registrar votos e visualizar os resultados.

## Funcionalidades

- Exibe as cinco perguntas mais recentes.
- Apresenta as opções disponíveis para cada pergunta.
- Registra votos e mostra os totais por opção.
- Disponibiliza o cadastro de perguntas e opções pelo painel administrativo do Django.
- Redireciona a página inicial (`/`) para a lista de enquetes (`/polls/`).

## Tecnologias

- Python 3.14 ou compatível com Django 6.1.1.
- Django 6.1.1.
- SQLite, incluído na configuração padrão do projeto.

## Como executar no Windows

Abra o PowerShell na pasta raiz do repositório e execute:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Set-Location .\mysite
python manage.py migrate
python manage.py runserver
```

Acesse <http://127.0.0.1:8000/>. O endereço `/` encaminha para `/polls/`.

Para criar um usuário do painel administrativo, com o ambiente virtual ativo e dentro da pasta `mysite`, execute:

```powershell
python manage.py createsuperuser
```

Depois, acesse <http://127.0.0.1:8000/admin/>.

## Testes

Com o ambiente virtual ativo e o terminal na pasta `mysite`, execute:

```powershell
python manage.py test polls
```

## Endereços principais

| Endereço | Descrição |
| --- | --- |
| `/` | Redireciona para a lista de enquetes. |
| `/polls/` | Lista as perguntas recentes. |
| `/polls/<id>/` | Exibe a pergunta e o formulário de voto. |
| `/polls/<id>/vote/` | Recebe o voto enviado pelo formulário. |
| `/polls/<id>/results/` | Exibe os votos da pergunta. |
| `/admin/` | Abre o painel administrativo do Django. |

## Estrutura do projeto

```text
EnqueteHashtag/
|-- .gitignore                 # Arquivos locais que não devem ir ao GitHub
|-- README.md                  # Documentação e instruções do projeto
|-- requirements.txt           # Dependências Python do projeto
|-- .venv/                     # Ambiente virtual local (não versionado)
`-- mysite/
    |-- manage.py              # Comandos administrativos do Django
    |-- db.sqlite3              # Banco local (não versionado)
    |-- mysite/
    |   |-- settings.py        # Configurações do projeto
    |   |-- urls.py            # Rotas principais
    |   |-- asgi.py             # Ponto de entrada ASGI
    |   `-- wsgi.py             # Ponto de entrada WSGI
    `-- polls/
        |-- models.py          # Modelos Question e Choice
        |-- views.py           # Lista, detalhes, votação e resultados
        |-- urls.py            # Rotas do app de enquetes
        |-- admin.py           # Registro dos modelos no painel administrativo
        |-- tests.py           # Testes automatizados das views
        |-- migrations/        # Histórico das alterações no banco
        `-- templates/polls/   # Páginas HTML das enquetes
```

## Preparação para produção

As configurações padrão são voltadas ao desenvolvimento local. Antes de publicar o site, configure as variáveis de ambiente `DJANGO_SECRET_KEY` com uma chave privada, `DJANGO_DEBUG=false` e `DJANGO_ALLOWED_HOSTS` com os domínios autorizados separados por vírgulas. Não use o servidor de desenvolvimento do Django em produção.
