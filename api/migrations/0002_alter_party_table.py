# Generated by Django 4.2.3 on 2023-07-25 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='party',
            table='party_master',
        ),
    ]