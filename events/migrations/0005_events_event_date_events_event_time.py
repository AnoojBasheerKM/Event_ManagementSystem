# Generated by Django 5.1.4 on 2024-12-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='event_time',
            field=models.TimeField(null=True),
        ),
    ]