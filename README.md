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
</pre>

