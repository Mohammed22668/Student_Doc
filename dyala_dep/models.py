from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tokenize import Decnumber
from django.db import models

# Create your models here.

class Asol_ALdeen(models.Model):
    dNumber = models.CharField(max_length=50,verbose_name="رقم الوثيقة")
    dDate= models.DateField(verbose_name="تاريخ الوثيقة")
    dTitle=models.CharField(max_length=300,verbose_name="عنوان الوثيقة")
    dName=models.CharField(max_length=300,verbose_name="اسم الطالب")
    dYear_grad = models.CharField(max_length=50,verbose_name="سنة التخرج")
    dDepartment=models.CharField(max_length=300,default="اصول الدين/ديالى",verbose_name="القسم")
    dNote = models.CharField(max_length=300, verbose_name="الملاحظات", null=True, blank=True)
    dImg = models.ImageField(upload_to="photos/Dyala/%y", verbose_name="صورة الوثيقة",null=True, blank=True)
    


    def __str__(self):
        return self.dName

    class Meta:
        verbose_name = 'اصول الدين'
        verbose_name_plural = 'اصول الدين'
