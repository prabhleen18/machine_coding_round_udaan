# Generated by Django 2.0 on 2021-07-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='pinCode',
            field=models.IntegerField(),
        ),
    ]
