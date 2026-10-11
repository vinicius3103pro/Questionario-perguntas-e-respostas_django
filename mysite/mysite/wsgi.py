"""Configuração WSGI do projeto mysite.

Expõe o objeto WSGI ``application`` para servidores síncronos.

Mais informações:
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
