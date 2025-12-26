# MiPrimeraPagina-AyalaMarisa
Curso Python Flex - Comision 84995 - Entrega TP3

Así fui armando mi proyecto:

1) crear repositorio GitHub: https://github.com/marisalej/MiPrimeraPagina-AyalaMarisa.git

2) crear carpeta local: C:/MARISALEJ/varios/_coderhouse/Python_EntregaTP3

3) abrir VSC en la carpeta local y clonar el repositorio github desde la terminal Git Bash (git clone https://github.com/marisalej/MiPrimeraPagina-AyalaMarisa.git .)

4) crear el entorno virtual (python -m venv .venv)

5) desde la terminal Powershell, activar entorno virtual (.venv/Scripts/activate)

6) instalar Django 5 (pip install django==5)

7) crear el archivo requirements.txt (pip freeze > requirements.txt)

8) crear el proyecto (django-admin startproject IberaGym .)

9) dentro de la carpeta Python_EntregaTP3 crear la app Socio, Entrenador y Plan (python manage.py startapp 'nombre_app')

10) registrar las 3 apps en Installed_Apps del archivo settings.py

11) crear los 3 modelos en el archivo models.py de cada app

12) hacer las migraciones (python manage.py makemigrations) y luego migrarlas (python manage.py migrate) - se crean 3 tablas (entrenador_entrenador, plan_plan y socio_socio)

13) registrar en admin.py de cada app

14) crear usuario admin (python manage.py createsuperuser) (marisa-marisa@iberagym.com-cursocoder25)

15) generar el archivo forms.py en cada app

16) crear las vistas en views.py para cada app (listar, cargar y buscar datos)

17) crear urls.py de cada app (usando app_name) y modificar urls.py del proyecto 

18) crear los templates de cada app para cargar, listar y buscar registros

19) correr el servidor (python manage.py runserver)

20) navegar por el proyecto IberaGym usando las funciones definidas para listar, crear y buscar datos

21) luego de verificar que todo funciones hacer los commits y actualizar mi repositorio de GitHub (git push)
