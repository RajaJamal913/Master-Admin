# Generated by Django 5.0.6 on 2024-07-24 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('spent_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('status', models.CharField(choices=[('active', 'Active'), ('suspended', 'Suspended')], max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('rates', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
