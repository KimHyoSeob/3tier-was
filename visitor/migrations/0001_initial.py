# Generated by Django 5.0.4 on 2024-05-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=100)),
                ('eamil', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=30)),
            ],
        ),
    ]
