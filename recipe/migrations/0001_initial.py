# Generated by Django 4.2.3 on 2023-08-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredient', models.CharField(max_length=100)),
                ('time', models.FloatField()),
                ('process', models.TextField()),
            ],
        ),
    ]
