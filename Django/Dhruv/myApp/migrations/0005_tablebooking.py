# Generated by Django 4.0.3 on 2022-03-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_contact_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('date', models.DateField()),
                ('noofpeople', models.CharField(max_length=150)),
                ('time', models.TimeField()),
            ],
        ),
    ]
