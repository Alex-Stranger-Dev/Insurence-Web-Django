# Generated by Django 4.1.2 on 2022-12-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client1', '0007_alter_phone_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='persone',
            name='second_name',
            field=models.CharField(default=str, max_length=35, verbose_name='Second name'),
        ),
    ]
