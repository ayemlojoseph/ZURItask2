# Generated by Django 3.0.6 on 2021-08-22 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('subject', models.TextField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
