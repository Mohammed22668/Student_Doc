# Generated by Django 4.0.3 on 2022-03-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyala_dep', '0002_alter_asol_aldeen_options_alter_asol_aldeen_dimg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asol_aldeen',
            name='dImg',
            field=models.ImageField(blank=True, null=True, upload_to='photos/Dyala/%y', verbose_name='صورة الوثيقة'),
        ),
    ]
