import sys
import os

# Add the BestPrice directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'BestPrice'))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Supermarket.settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Vercel expects 'app'
app = application
