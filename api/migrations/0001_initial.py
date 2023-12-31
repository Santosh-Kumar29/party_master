# Generated by Django 4.2.3 on 2023-07-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('party_type', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('land_line_number', models.CharField(max_length=15)),
                ('mobile_number', models.CharField(max_length=15)),
                ('gst_no', models.CharField(max_length=20)),
                ('contact_person', models.CharField(max_length=100)),
            ],
        ),
    ]
