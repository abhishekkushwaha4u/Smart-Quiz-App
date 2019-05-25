# Generated by Django 2.2.1 on 2019-05-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('registration_number', models.CharField(blank=True, max_length=9)),
                ('phone_number', models.CharField(max_length=10)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], max_length=7)),
            ],
        ),
    ]
