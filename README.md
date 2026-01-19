# MiPrimeraPagina-AyalaMarisa
Curso Python Flex - Comision 84995 - Entrega Final (23/01/2026)

Pasos a seguir para completar mi proyecto "IberaGym":

1) crear repositorio GitHub: https://github.com/marisalej/MiPrimeraPagina-AyalaMarisa.git

2) crear carpeta local: C:/MARISALEJ/varios/_coderhouse/Python_EntregaTP3

3) abrir VSC en la carpeta local y clonar el repositorio github desde la terminal Git Bash (git clone https://github.com/marisalej/MiPrimeraPagina-AyalaMarisa.git .)

4) crear el entorno virtual (python -m venv .venv)

5) desde la terminal Powershell, activar entorno virtual (.venv/Scripts/activate)

6) instalar Django 5 (pip install django==5)

7) crear el archivo requirements.txt (pip freeze > requirements.txt)

8) crear el proyecto (django-admin startproject IberaGym .)

9) dentro de la carpeta Python_EntregaTP3 crear las apps Socio, Entrenador y Plan (python manage.py startapp 'nombre_app'), para la entrega final crear la app Users para manejar login, logout y registro de usuarios, con posibilidad de cambiar la contraseña

10) registrar las 4 apps en Installed_Apps del archivo settings.py

11) crear los 4 modelos en el archivo models.py de cada app, para la entrega final modifiqué el modelo socio agregando el campo "foto", para lo cual tuve que instalar pillow para poder procesar las imagenes (pip install pillow)

12) hacer las migraciones (python manage.py makemigrations) y luego migrarlas (python manage.py migrate) - se crean 4 tablas (entrenador_entrenador, plan_plan, socio_socio y users_user)

13) registrar los modelos en admin.py de cada app usando @admin.register

14) crear usuario admin (python manage.py createsuperuser) (marisa-marisa@iberagym.com-cursocoder25)

15) generar el archivo forms.py en cada app

16) crear las vistas en views.py para cada app aplicando CRUD (entrenador tiene vistas basadas en funciones mientras que plan y socio tienen vistas basadas en clases), usando el decorador @login_required en las vistas basadas en funciones y LoginRequiredMixin en las vistas basadas en clases

17) crear urls.py de cada app (usando app_name) y modificar urls.py del proyecto 

18) crear los templates de cada app para cargar, listar, buscar, actualizar y eliminar registros

19) agregar en el navbar una acceso Acerca de mí

20) verificar que .gitignore tenga incluidos a pycache, db.sqlite3, media

21) correr el servidor (python manage.py runserver)

22) navegar por el proyecto IberaGym usando las vistas definidas

23) luego de verificar que todo funcione hacer los commits y actualizar mi repositorio de GitHub (git push)
