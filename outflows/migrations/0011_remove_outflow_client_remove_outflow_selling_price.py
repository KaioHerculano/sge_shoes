# Generated by Django 5.1.6 on 2025-03-26 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outflows', '0010_outflow_client_outflow_selling_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outflow',
            name='client',
        ),
        migrations.RemoveField(
            model_name='outflow',
            name='selling_price',
        ),
    ]
