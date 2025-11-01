Iniciar o projeto Django

python -m venv nomeprojeto
. venv/bin/activate
pip install django
django-admin startproject nomeprojeto .
py manage.py startapp nomeapp

Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT git@github.com:FabioCarmo/projeto-agenda-django-25.git
git push 


Migrando a base de dados do Django

python manage.py makemigrations
python manage.py migrate

Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME