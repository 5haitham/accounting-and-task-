# Generated by Django 5.0.7 on 2024-07-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_system', '0002_alter_invoiceitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
