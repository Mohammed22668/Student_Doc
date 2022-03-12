# Generated by Django 4.0.3 on 2022-03-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyala_dep', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asol_aldeen',
            options={'verbose_name': 'اصول الدين', 'verbose_name_plural': 'اصول الدين'},
        ),
        migrations.AlterField(
            model_name='asol_aldeen',
            name='dImg',
            field=models.ImageField(blank=True, null=True, upload_to='photos/Dyala/%y/%m/%d', verbose_name='صورة الوثيقة'),
        ),
        migrations.AlterField(
            model_name='asol_aldeen',
            name='dNote',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='الملاحظات'),
        ),
    ]