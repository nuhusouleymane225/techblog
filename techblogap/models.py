from django.db import models

# Create your models here.
class Category(models.Model):
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='picture')
    description = models.TextField()
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    vues = models.IntegerField()