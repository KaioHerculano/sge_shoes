# Generated by Django 5.1.6 on 2025-05-13 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_rename_tax_id_company_chpj_remove_company_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='chpj',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
