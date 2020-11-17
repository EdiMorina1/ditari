# Generated by Django 2.1.5 on 2019-01-14 14:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_profesori'),
    ]

    operations = [
        migrations.CreateModel(
            name='klasa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emriKlasa', models.CharField(max_length=10)),
                ('paralelja', models.CharField(max_length=10)),
                ('vitiShkollor', models.DateTimeField(default=datetime.datetime.now)),
                ('idLenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profesori')),
            ],
        ),
    ]