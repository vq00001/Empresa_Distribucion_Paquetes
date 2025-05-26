## COMANDOS PARA DJANGO

Crear virtualenvironment (en carpeta objetivo)
- pip install virtualenv
- virtualenv venv
- cd venv/Scripts
- activate.bat

Instalar Django y verificar 
- pip install django
- django-admin --version

Crear proyecto
- django-admin startproject nombre

Crear proyecto con archivos en la carpeta raiz 
- django-admin startproject nombre . 

Correr servidor
- python manage.py runserver

Correr servidor en el puerto 3000
- python manage.py runserver 3000

Crear aplicacion dentro del proyecto
- python manage.py startapp nombre

Usar PostgreSQL 
- pip install psycopg2 (instalar psycopg2)

"Compilar" los cambios hechos a la base de datos
- python manage.py makemigrations [app]

Actualizar la base de datos
- python manage.py migrate

Shell de Django
- python manage.py shell