# Generated by Django 2.1.1 on 2018-09-27 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapi', '0004_auto_20180927_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='espaciomodel',
            old_name='latititud',
            new_name='latitud',
        ),
    ]
