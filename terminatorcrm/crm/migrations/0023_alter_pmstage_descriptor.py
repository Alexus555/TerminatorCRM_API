# Generated by Django 4.1.4 on 2023-02-08 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0022_pmstage_descriptor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmstage',
            name='descriptor',
            field=models.CharField(max_length=2, null=True),
        ),
    ]