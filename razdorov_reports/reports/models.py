from django.db import models

# Create your models here.
class Managers(models.Model):
    name = models.CharField(max_length=130)
    id_personal = models.IntegerField(max_length=7)
