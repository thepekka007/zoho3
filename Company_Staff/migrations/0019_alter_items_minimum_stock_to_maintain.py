# Generated by Django 4.2.6 on 2024-01-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0018_chart_of_accounts_parent_account_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='minimum_stock_to_maintain',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]