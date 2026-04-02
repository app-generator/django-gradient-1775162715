# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Livro(models.Model):

    #__Livro_FIELDS__
    isbn = models.IntegerField(null=True, blank=True)
    titulo = models.CharField(max_length=255, null=True, blank=True)
    resumo_sinopse = models.TextField(max_length=255, null=True, blank=True)
    ano_publicacao = models.DateTimeField(blank=True, null=True, default=timezone.now)
    edicao = models.IntegerField(null=True, blank=True)
    preco_venda = models.IntegerField(null=True, blank=True)
    preco_compra = models.IntegerField(null=True, blank=True)
    quantidade_esqtoque = models.IntegerField(null=True, blank=True)
    formato = models.CharField(max_length=255, null=True, blank=True)
    id_editora = models.IntegerField(null=True, blank=True)
    id_autor = models.IntegerField(null=True, blank=True)

    #__Livro_FIELDS__END

    class Meta:
        verbose_name        = _("Livro")
        verbose_name_plural = _("Livro")



#__MODELS__END
