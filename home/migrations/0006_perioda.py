# Generated by Django 2.1.5 on 2019-01-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_nxenesi'),
    ]

    operations = [
        migrations.CreateModel(
            name='perioda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emriPerioda', models.CharField(max_length=10)),
            ],
        ),
    ]
