from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Criar tabela category - chave estrangeira de contact
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

# Criar tabela contacts atraves da classe base models
class Contact(models.Model):
    # Criar os campos da tabela atraves do metodo Field
    # id (Primary Key - Criado Automaticamente pelo django)
    # first_name (string), last_name(string), phone(string), email(email)
    # create_date (date), description(text), category(Foreign Key), show(bool)
    # owner(Foreign Key), picture(image)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=499, blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='picture/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'