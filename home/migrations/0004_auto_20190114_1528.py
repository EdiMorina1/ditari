# Generated by Django 2.1.5 on 2019-01-14 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_klasa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klasa',
            old_name='idLenda',
            new_name='idProfi',
        ),
    ]