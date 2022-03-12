# Generated by Django 4.0.3 on 2022-03-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asol_ALdeen_Boys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dNumber', models.CharField(max_length=50, verbose_name='رقم الوثيقة')),
                ('dDate', models.DateField(verbose_name='تاريخ الوثيقة')),
                ('dTitle', models.CharField(max_length=300, verbose_name='عنوان الوثيقة')),
                ('dName', models.CharField(max_length=300, verbose_name='اسم الطالب')),
                ('dYear_grad', models.CharField(max_length=50, verbose_name='سنة التخرج')),
                ('dDepartment', models.CharField(default='اصول الدين/بنين-بغداد', max_length=300, verbose_name='القسم')),
                ('dNote', models.CharField(blank=True, max_length=300, null=True, verbose_name='الملاحظات')),
                ('dImg', models.ImageField(blank=True, null=True, upload_to='photos/Baqhdad/Asol-Boys/%y/%m/%d', verbose_name='صورة الوثيقة')),
            ],
            options={
                'verbose_name': 'اصول الدين/بنين-بغداد',
                'verbose_name_plural': 'اصول الدين/بنين-بغداد',
            },
        ),
        migrations.CreateModel(
            name='Asol_ALdeen_Girls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dNumber', models.CharField(max_length=50, verbose_name='رقم الوثيقة')),
                ('dDate', models.DateField(verbose_name='تاريخ الوثيقة')),
                ('dTitle', models.CharField(max_length=300, verbose_name='عنوان الوثيقة')),
                ('dName', models.CharField(max_length=300, verbose_name='اسم الطالبة')),
                ('dYear_grad', models.CharField(max_length=50, verbose_name='سنة التخرج')),
                ('dDepartment', models.CharField(default='اصول الدين/بنات-بغداد', max_length=300, verbose_name='القسم')),
                ('dNote', models.CharField(blank=True, max_length=300, null=True, verbose_name='الملاحظات')),
                ('dImg', models.ImageField(blank=True, null=True, upload_to='photos/Baqhdad/Asol-Girls/%y/%m/%d', verbose_name='صورة الوثيقة')),
            ],
            options={
                'verbose_name': 'اصول الدين/بنات-بغداد',
                'verbose_name_plural': 'اصول الدين/بنات-بغداد',
            },
        ),
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dNumber', models.CharField(max_length=50, verbose_name='رقم الوثيقة')),
                ('dDate', models.DateField(verbose_name='تاريخ الوثيقة')),
                ('dTitle', models.CharField(max_length=300, verbose_name='عنوان الوثيقة')),
                ('dName', models.CharField(max_length=300, verbose_name='اسم الطالبة')),
                ('dYear_grad', models.CharField(max_length=50, verbose_name='سنة التخرج')),
                ('dDepartment', models.CharField(default='الدراسات الاسلامية باللغة الانكليزية', max_length=300, verbose_name='القسم')),
                ('dNote', models.CharField(blank=True, max_length=300, null=True, verbose_name='الملاحظات')),
                ('dImg', models.ImageField(blank=True, null=True, upload_to='photos/Baqhdad/EN/%y/%m/%d', verbose_name='صورة الوثيقة')),
            ],
            options={
                'verbose_name': 'اللغة الانكليزية',
                'verbose_name_plural': 'اللغة الانكليزية',
            },
        ),
        migrations.CreateModel(
            name='FiqhFound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dNumber', models.CharField(max_length=50, verbose_name='رقم الوثيقة')),
                ('dDate', models.DateField(verbose_name='تاريخ الوثيقة')),
                ('dTitle', models.CharField(max_length=300, verbose_name='عنوان الوثيقة')),
                ('dName', models.CharField(max_length=300, verbose_name='اسم الطالبة')),
                ('dYear_grad', models.CharField(max_length=50, verbose_name='سنة التخرج')),
                ('dDepartment', models.CharField(default='الفقه واصوله/بغداد', max_length=300, verbose_name='القسم')),
                ('dNote', models.CharField(blank=True, max_length=300, null=True, verbose_name='الملاحظات')),
                ('dImg', models.ImageField(blank=True, null=True, upload_to='photos/Baqhdad/Fiqh/%y/%m/%d', verbose_name='صورة الوثيقة')),
            ],
            options={
                'verbose_name': 'الفقه واصوله',
                'verbose_name_plural': 'الفقه واصوله',
            },
        ),
    ]