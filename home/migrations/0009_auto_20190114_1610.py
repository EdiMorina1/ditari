# Generated by Django 2.1.5 on 2019-01-14 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190114_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='IdPerioda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.perioda'),
        ),
    ]