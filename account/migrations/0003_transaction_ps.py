# Generated by Django 3.1.2 on 2020-11-01 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='ps',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
