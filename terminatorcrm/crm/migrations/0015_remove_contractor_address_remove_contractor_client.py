# Generated by Django 4.1.4 on 2023-02-02 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_agent_leadsource_leadstage_leadstatus_reason_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contractor',
            name='client',
        ),
    ]
