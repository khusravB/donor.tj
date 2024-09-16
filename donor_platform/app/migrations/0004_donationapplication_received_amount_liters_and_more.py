# Generated by Django 5.1.1 on 2024-09-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_donationapplication_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationapplication',
            name='received_amount_liters',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='donationapplication',
            name='received_amount_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
