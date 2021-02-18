# Generated by Django 3.1.5 on 2021-01-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='reserv2',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
    ]