# Generated by Django 4.2.6 on 2024-01-03 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0004_chart_of_accounts_delete_chart_of_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chart_of_accounts',
            name='login_details',
        ),
    ]
