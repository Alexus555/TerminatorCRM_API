# Generated by Django 4.1.4 on 2023-01-04 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_alter_projectpmstage_invoice_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectpmstage',
            name='pm_step',
        ),
    ]