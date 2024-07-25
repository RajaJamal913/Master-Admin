# Generated by Django 5.0.6 on 2024-07-25 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindash', '0003_api_bannedip_orderpanelconfig_activitylog_panelrate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitylog',
            name='activity',
        ),
        migrations.AddField(
            model_name='activitylog',
            name='action',
            field=models.CharField(choices=[('Login', 'Login'), ('Logout', 'Logout')], default='Login', max_length=20),
        ),
        migrations.AlterField(
            model_name='activitylog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admindash.userprofile'),
        ),
    ]
