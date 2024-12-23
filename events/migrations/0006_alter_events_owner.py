# Generated by Django 5.1.4 on 2024-12-22 06:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_events_event_date_events_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
