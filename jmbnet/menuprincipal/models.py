from django.db import models

# Create your models here.

class MenuPrincipal(models.Model):
    nome_menu = models.CharField(max_length=50)
    nome_form_html = models.CharField(max_length=50)

