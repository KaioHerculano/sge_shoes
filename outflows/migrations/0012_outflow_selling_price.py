# Generated by Django 5.1.6 on 2025-03-26 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outflows', '0011_remove_outflow_client_remove_outflow_selling_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='outflow',
            name='selling_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
