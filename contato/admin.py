from django.contrib import admin
from contato import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone')
    search_fields = ('first_name' ,'last_name','phone')
    ordering = ('id',)

@admin.register(models.Category)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)