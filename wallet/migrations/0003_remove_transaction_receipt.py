# Generated by Django 4.0.6 on 2022-08-19 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_account_currency_receipt_alter_customer_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='receipt',
        ),
    ]
