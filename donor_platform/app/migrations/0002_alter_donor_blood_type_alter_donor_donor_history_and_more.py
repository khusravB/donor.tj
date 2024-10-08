# Generated by Django 5.1.1 on 2024-09-11 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('First Positive', 'O(I) Rh+'), ('First Negative', 'O(I) Rh−'), ('Second Positive', 'A(II) Rh+'), ('Second Negative', 'A(II) Rh−'), ('Third Positive', 'B(III) Rh+'), ('Third Negative', 'B(III) Rh-'), ('Fourth Positive', 'AB(IV) Rh+'), ('Fourth Negative', 'AB(IV) Rh-')], default='First Positive', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.donorhistory'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='profile_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
