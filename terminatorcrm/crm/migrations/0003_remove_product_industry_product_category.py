# Generated by Django 4.1.4 on 2023-01-03 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_impstage_pmstage_pmstep_projectreport_projectstream_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='industry',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='crm.productcategory'),
        ),
    ]
