# Generated by Django 4.2.6 on 2024-01-08 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0012_items_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items_comments',
            old_name='chart_of_accounts',
            new_name='Items',
        ),
    ]
