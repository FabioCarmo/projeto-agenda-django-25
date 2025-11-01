from django.urls import path
from contato import views as contato

# HTTPRequest <-> HTTPResponse
# Arquitetura MVT (MODEL-VIEW-TEMPLATE)

app_name = 'contato'

urlpatterns = [
    path('<int:contato_id>/', contato.contato_view, name="contato"),
    path('buscar/', contato.buscar, name="buscar"),
    path('', contato.index, name="index"),
]