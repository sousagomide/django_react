# Build a Learning Management System with Django and React

Download source code: 

https://drive.google.com/drive/u/0/folders/1mVEWElDOtiTrkbIAqoTSoMoue79e65Rv

Libs Python

python -m pip install Django

Steps

1) Criar projeto Django

django-admin startproject core .

2) Instalação dos requerimentos

pip install -r requirements.txt
pip freeze

3) Módulos

<pre>
    python manage.py startapp main 
    python manage.py startapp userauths
    python manage.py startapp api
</pre>

4) Criar superusuário

python manage.py createsuperuser

5) Configurar Static, Media e Template Files

<pre>
    import os

    TEMPLATES = [
        {
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
        },
    ]

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = BASE_DIR / 'templates'
    MEDIA_URL = '/media/' #127.0.0.1/media/avatar.jpg
    MEDIA_ROOT = BASE_DIR / 'media'
</pre>

6) Criar as pastas: <pre>templates, media e static</pre>

7) Em urls.py no core

<pre>
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
</pre>

