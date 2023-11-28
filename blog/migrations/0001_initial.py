# Generated by Django 4.2.5 on 2023-09-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='blogs')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('gender', models.CharField(choices=[('male', 'Мужчина'), ('female', 'Женщина')], max_length=6)),
                ('name', models.CharField(max_length=20)),
                ('profession', models.CharField(max_length=50)),
            ],
        ),
    ]