"""
WSGI config for Supermarket project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

# Add BestPrice directory to Python path for Vercel
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Supermarket.settings')

application = get_wsgi_application()

# Vercel serverless function handler
app = application
=======
>>>>>>> be08d98730b581d040c432365cebcb1271a58c1f
