from django.db import models


# Create your models here.
class Headunit(models.Model):
    ident = models.AutoField
    name = models.CharField('Название', max_length=20)
    pic = models.ImageField(upload_to='media', null=True, blank=True)
    width = models.CharField('Ширина', max_length=5, default="0")
    height = models.CharField('Высота', max_length=5, default="0")
    gu_diag = models.CharField('Диагональ', max_length=5, default="0")
    gu_diag_int = models.IntegerField('Приближенная диагональ', default=0)
    osys = models.CharField('Операционная система', max_length=20, default="Android")
    object_hu = models.Manager()
    DoesNotExist = models.Manager
    def __str__(self):
        return self.name


