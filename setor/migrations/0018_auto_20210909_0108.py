# Generated by Django 3.1.5 on 2021-09-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0017_auto_20210909_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setoran',
            name='tgl',
            field=models.DateField(null=True),
        ),
    ]
