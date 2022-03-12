from django.db import models

# Create your models here.

########################### ASOL ALDEEN - BOYS #############################

class Asol_ALdeen_Boys(models.Model):
    dNumber = models.CharField(max_length=50, verbose_name="رقم الوثيقة")
    dDate = models.DateField(verbose_name="تاريخ الوثيقة")
    dTitle = models.CharField(max_length=300, verbose_name="عنوان الوثيقة")
    dName = models.CharField(max_length=300, verbose_name="اسم الطالب")
    dYear_grad = models.CharField(max_length=50, verbose_name="سنة التخرج")
    dDepartment = models.CharField(
        max_length=300, default="اصول الدين/بنين-بغداد", verbose_name="القسم")
    dNote = models.CharField(max_length=300, verbose_name="الملاحظات", null=True, blank=True)
    dImg = models.ImageField(upload_to="photos/Baqhdad/Asol-Boys/%y",
                             verbose_name="صورة الوثيقة", null=True, blank=True)

    def __str__(self):
        return self.dName

    class Meta:
        verbose_name = 'اصول الدين/بنين-بغداد'
        verbose_name_plural = 'اصول الدين/بنين-بغداد'


########################### ASOL ALDEEN - Girls ##############################

class Asol_ALdeen_Girls(models.Model):
    dNumber = models.CharField(max_length=50, verbose_name="رقم الوثيقة")
    dDate = models.DateField(verbose_name="تاريخ الوثيقة")
    dTitle = models.CharField(max_length=300, verbose_name="عنوان الوثيقة")
    dName = models.CharField(max_length=300, verbose_name="اسم الطالبة")
    dYear_grad = models.CharField(max_length=50, verbose_name="سنة التخرج")
    dDepartment = models.CharField(
        max_length=300, default="اصول الدين/بنات-بغداد", verbose_name="القسم")
    dNote = models.CharField(
        max_length=300, verbose_name="الملاحظات", null=True, blank=True)
    dImg = models.ImageField(upload_to="photos/Baqhdad/Asol-Girls/%y",
                             verbose_name="صورة الوثيقة", null=True, blank=True)

    def __str__(self):
        return self.dName

    class Meta:
        verbose_name = 'اصول الدين/بنات-بغداد'
        verbose_name_plural = 'اصول الدين/بنات-بغداد'

########################### English #######################################

class English(models.Model):
    dNumber = models.CharField(max_length=50, verbose_name="رقم الوثيقة")
    dDate = models.DateField(verbose_name="تاريخ الوثيقة")
    dTitle = models.CharField(max_length=300, verbose_name="عنوان الوثيقة")
    dName = models.CharField(max_length=300, verbose_name="اسم الطالبة")
    dYear_grad = models.CharField(max_length=50, verbose_name="سنة التخرج")
    dDepartment = models.CharField(
        max_length=300, default="الدراسات الاسلامية باللغة الانكليزية", verbose_name="القسم")
    dNote = models.CharField(
        max_length=300, verbose_name="الملاحظات", null=True, blank=True)
    dImg = models.ImageField(upload_to="photos/Baqhdad/EN/%y",
                             verbose_name="صورة الوثيقة", null=True, blank=True)

    def __str__(self):
        return self.dName

    class Meta:
        verbose_name = 'اللغة الانكليزية'
        verbose_name_plural = 'اللغة الانكليزية'

########################### Fiqh #############################################

class FiqhFound(models.Model):
    dNumber = models.CharField(max_length=50, verbose_name="رقم الوثيقة")
    dDate = models.DateField(verbose_name="تاريخ الوثيقة")
    dTitle = models.CharField(max_length=300, verbose_name="عنوان الوثيقة")
    dName = models.CharField(max_length=300, verbose_name="اسم الطالبة")
    dYear_grad = models.CharField(max_length=50, verbose_name="سنة التخرج")
    dDepartment = models.CharField(
        max_length=300, default="الفقه واصوله/بغداد", verbose_name="القسم")
    dNote = models.CharField(
        max_length=300, verbose_name="الملاحظات", null=True, blank=True)
    dImg = models.ImageField(upload_to="photos/Baqhdad/Fiqh/%y",
                             verbose_name="صورة الوثيقة", null=True, blank=True)

    def __str__(self):
        return self.dName

    class Meta:
        verbose_name = 'الفقه واصوله'
        verbose_name_plural = 'الفقه واصوله'


########################### History ##############################

class History(models.Model):
    dNumber = models.CharField(max_length=50, verbose_name="رقم الوثيقة")
    dDate = models.DateField(verbose_name="تاريخ الوثيقة")
    dTitle = models.CharField(max_length=300, verbose_name="عنوان الوثيقة")
    dName = models.CharField(max_length=300, verbose_name="اسم الطالبة")
    dYear_grad = models.CharField(max_length=50, verbose_name="سنة التخرج")
    dDepartment = models.CharField(
        max_length=300, default="قسم التاريخ-بغداد", verbose_name="القسم")
    dNote = models.CharField(
        max_length=300, verbose_name="الملاحظات", null=True, blank=True)
    dImg = models.ImageField(upload_to="photos/Baqhdad/History/%y",
                             verbose_name="صورة الوثيقة", null=True, blank=True)

    def __str__(self):
        return self.dName

    class Meta:
        verbose_name = 'قسم التاريخ'
        verbose_name_plural = 'قسم التاريخ'


########################### ArabicLan ##############################

class ArabicLan(models.Model):
    dNumber = models.CharField(max_length=50, verbose_name="رقم الوثيقة")
    dDate = models.DateField(verbose_name="تاريخ الوثيقة")
    dTitle = models.CharField(max_length=300, verbose_name="عنوان الوثيقة")
    dName = models.CharField(max_length=300, verbose_name="اسم الطالبة")
    dYear_grad = models.CharField(max_length=50, verbose_name="سنة التخرج")
    dDepartment = models.CharField(
        max_length=300, default="قسم اللغة العربية", verbose_name="القسم")
    dNote = models.CharField(
        max_length=300, verbose_name="الملاحظات", null=True, blank=True)
    dImg = models.ImageField(upload_to="photos/Baqhdad/ArabicLan/%y",
                             verbose_name="صورة الوثيقة", null=True, blank=True)

    def __str__(self):
        return self.dName

    class Meta:
        verbose_name = 'قسم اللغة العربية'
        verbose_name_plural = 'قسم اللغة العربية'


########################### Law ##############################

class Law(models.Model):
    dNumber = models.CharField(max_length=50, verbose_name="رقم الوثيقة")
    dDate = models.DateField(verbose_name="تاريخ الوثيقة")
    dTitle = models.CharField(max_length=300, verbose_name="عنوان الوثيقة")
    dName = models.CharField(max_length=300, verbose_name="اسم الطالبة")
    dYear_grad = models.CharField(max_length=50, verbose_name="سنة التخرج")
    dDepartment = models.CharField(
        max_length=300, default="قسم القانون-بغداد", verbose_name="القسم")
    dNote = models.CharField(
        max_length=300, verbose_name="الملاحظات", null=True, blank=True)
    dImg = models.ImageField(upload_to="photos/Baqhdad/Law/%y",
                             verbose_name="صورة الوثيقة", null=True, blank=True)

    def __str__(self):
        return self.dName

    class Meta:
        verbose_name = 'قسم القانون'
        verbose_name_plural = 'قسم القانون'


########################### Finance Banking ##############################

class FinanceBanking(models.Model):
    dNumber = models.CharField(max_length=50, verbose_name="رقم الوثيقة")
    dDate = models.DateField(verbose_name="تاريخ الوثيقة")
    dTitle = models.CharField(max_length=300, verbose_name="عنوان الوثيقة")
    dName = models.CharField(max_length=300, verbose_name="اسم الطالبة")
    dYear_grad = models.CharField(max_length=50, verbose_name="سنة التخرج")
    dDepartment = models.CharField(max_length=300, default="قسم المالية والمصرفية", verbose_name="القسم")
    dNote = models.CharField(max_length=300, verbose_name="الملاحظات", null=True, blank=True)
    dImg = models.ImageField(upload_to="photos/Baqhdad/FinanceBank/%y",
                             verbose_name="صورة الوثيقة", null=True, blank=True)

    def __str__(self):
        return self.dName

    class Meta:
        verbose_name = 'قسم المالية والمصرفية'
        verbose_name_plural = 'قسم المالية والمصرفية'


###########################    ##############################
