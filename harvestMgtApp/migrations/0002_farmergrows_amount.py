# Generated by Django 2.2.5 on 2020-03-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvestMgtApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmergrows',
            name='amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
