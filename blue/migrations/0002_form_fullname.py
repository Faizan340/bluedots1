# Generated by Django 3.2.8 on 2022-01-12 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='fullname',
            field=models.CharField(default='fullname', max_length=1000),
        ),
    ]