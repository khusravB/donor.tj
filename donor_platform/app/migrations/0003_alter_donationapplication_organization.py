# Generated by Django 5.1.1 on 2024-09-11 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_donor_blood_type_alter_donor_donor_history_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationapplication',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
