# Generated by Django 2.1.5 on 2019-01-14 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190114_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='nxenesi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emriNx', models.CharField(max_length=50)),
                ('mbiemriNx', models.CharField(max_length=50)),
                ('emriPrindit', models.CharField(max_length=50)),
                ('NrTelPr', models.CharField(max_length=50)),
                ('idKlasa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.klasa')),
            ],
        ),
    ]
