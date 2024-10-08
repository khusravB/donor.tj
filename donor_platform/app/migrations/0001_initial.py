# Generated by Django 5.1.1 on 2024-09-11 18:03

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_of_all_donations', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('donor', 'Donor'), ('organization', 'Organization')], default='organization', max_length=30)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_info', models.TextField()),
                ('blood_type', models.CharField(choices=[('First Positive', 'O(I) Rh+'), ('First Negative', 'O(I) Rh−'), ('Second Positive', 'A(II) Rh+'), ('Second Negative', 'A(II) Rh−'), ('Third Positive', 'B(III) Rh+'), ('Third Negative', 'B(III) Rh-'), ('Fourth Positive', 'AB(IV) Rh+'), ('Fourth Negative', 'AB(IV) Rh-')], default='First Positive', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('donor_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.donorhistory')),
            ],
        ),
        migrations.CreateModel(
            name='DonationApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('needing_person', models.CharField(max_length=255)),
                ('requested_amount_liters', models.DecimalField(decimal_places=2, max_digits=5)),
                ('requested_amount_quantity', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('blood_type', models.CharField(choices=[('First Positive', 'O(I) Rh+'), ('First Negative', 'O(I) Rh−'), ('Second Positive', 'A(II) Rh+'), ('Second Negative', 'A(II) Rh−'), ('Third Positive', 'B(III) Rh+'), ('Third Negative', 'B(III) Rh-'), ('Fourth Positive', 'AB(IV) Rh+'), ('Fourth Negative', 'AB(IV) Rh-')], default='First Positive', max_length=50)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('all_donors', models.ManyToManyField(blank=True, null=True, to='app.donor')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organization')),
            ],
        ),
    ]
