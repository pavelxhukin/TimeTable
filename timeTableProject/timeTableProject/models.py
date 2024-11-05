from django.db import models


class Building(models.Model):
    buildingId = models.AutoField()
    buildingAdres = models.TextField('Adres')
    

    def __str__(self):
        return self.title
