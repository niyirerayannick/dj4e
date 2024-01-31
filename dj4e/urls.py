import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.contrib.auth import views as auth_views
from django.urls import re_path  # Use re_path instead of url

urlpatterns = [
    path('', include('ads.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Use path for consistency
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
]

# Serve static files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve, {
        'document_root': os.path.join(BASE_DIR, 'site'),
        'show_indexes': True,
    }, name='site_path'),

    # Serve favicon
    path('favicon.ico', serve, {
        'path': 'favicon.ico',
        'document_root': os.path.join(BASE_DIR, 'home/static'),
    }),
]

# Switch to social login if configured
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,  # Insert at the beginning for higher priority
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except ImportError:
    print('Using registration/login.html as the login template')
