# Generated by Django 4.1.4 on 2023-02-17 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0028_impstage_required_for_report_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='crm.projectstatus'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='crm.projecttype'),
            preserve_default=False,
        ),
    ]
