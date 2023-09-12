# from django.db import models
#
# class Produit(models.Model):
#     nom=models.CharField(max_lenght=200, null=True)
#     prix=models.FloatField(null=True)
#     date_creation = models.DateTimeField(auto_now_add=True)
#
#


from django.db import models


class Tag(models.Model):
    nom = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.nom
class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    prix = models.FloatField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    tag= models.ManyToManyField(Tag)

    def __str__(self):
        return self.nom
