# Generated by Django 4.1.4 on 2023-02-18 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0031_alter_projectpmstep_project_pm_stage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectpmstage',
            options={'ordering': ['pm_stage']},
        ),
        migrations.AlterModelOptions(
            name='projectpmstep',
            options={'ordering': ['pm_step']},
        ),
        migrations.AddField(
            model_name='pmstep',
            name='required_for_stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.pmstage'),
        ),
    ]