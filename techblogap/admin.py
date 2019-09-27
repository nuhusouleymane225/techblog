from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_add', 'date_upd', 'user_id')
    list_filter = (
        'date_add',
        'date_upd',
        'user_id',
        'id',
        'nom',
        'date_add',
        'date_upd',
        'user_id',
    )


class ProduitAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'image',
        'description',
        'category_id',
        'user_id',
        'vues',
    )
    list_filter = (
        'category_id',
        'user_id',
        'id',
        'nom',
        'image',
        'description',
        'category_id',
        'user_id',
        'vues',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Produit, ProduitAdmin)
