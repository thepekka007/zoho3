# Generated by Django 4.2.6 on 2024-01-13 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0013_rename_chart_of_accounts_items_comments_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart_of_accounts',
            name='account_description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
