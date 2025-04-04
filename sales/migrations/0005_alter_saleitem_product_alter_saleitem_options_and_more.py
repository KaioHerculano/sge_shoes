# Generated by Django 5.1.6 on 2025-03-29 07:19

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_stock'),
        ('sales', '0004_alter_sale_options_remove_sale_seller_sale_cashier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='Produto'),
        ),
        migrations.AlterModelOptions(
            name='saleitem',
            options={'verbose_name': 'Item da Venda', 'verbose_name_plural': 'Itens das Vendas'},
        ),
        migrations.RemoveField(
            model_name='sale',
            name='payment_method',
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='quantity',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.sale', verbose_name='Venda'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Preço Unitário'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
