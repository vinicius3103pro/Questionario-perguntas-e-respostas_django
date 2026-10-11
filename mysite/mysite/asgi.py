"""Configuração ASGI do projeto mysite.

Expõe o objeto ASGI ``application`` para servidores assíncronos.

Mais informações:
https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_asgi_application()
