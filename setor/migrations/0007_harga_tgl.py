# Generated by Django 3.1.5 on 2021-07-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0006_setoran_harga'),
    ]

    operations = [
        migrations.AddField(
            model_name='harga',
            name='tgl',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
