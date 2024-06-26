# Generated by Django 3.1.7 on 2021-07-26 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agency', '0002_delete_agencytable'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgencyTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('division', models.CharField(max_length=10)),
                ('district', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.TextField(max_length=100)),
            ],
        ),
    ]
