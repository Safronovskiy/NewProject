# Generated by Django 3.1.5 on 2021-01-18 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField(blank=True, max_length=2000)),
                ('is_published', models.DateTimeField(auto_now=True)),
                ('is_edited', models.DateTimeField(auto_now_add=True)),
                ('is_moderated', models.BooleanField(default=False)),
                ('is_archivated', models.BooleanField(default=False)),
                ('res', models.CharField(blank=True, max_length=100, null=True)),
                ('res1', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.blogcategory')),
            ],
        ),
    ]