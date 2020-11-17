# Generated by Django 2.1.5 on 2019-01-19 09:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190114_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='notaPerfundimtare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vleraNota', models.IntegerField(default=0)),
                ('dataNota', models.DateTimeField(default=datetime.datetime.now)),
                ('idLenda', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.lenda')),
                ('idNx', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.nxenesi')),
                ('idProfesori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.profesori')),
            ],
        ),
    ]