# Generated by Django 4.1.4 on 2023-02-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0032_alter_projectpmstage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=4),
        ),
    ]
