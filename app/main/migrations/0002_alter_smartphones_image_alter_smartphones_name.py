# Generated by Django 5.0.1 on 2024-02-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphones',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='smartphones',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
