# Generated by Django 3.1 on 2020-08-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flights', '0002_auto_20200814_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pasanger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='Flights.Flight')),
            ],
        ),
    ]
