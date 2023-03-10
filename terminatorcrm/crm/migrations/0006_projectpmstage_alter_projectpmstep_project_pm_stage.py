# Generated by Django 4.1.4 on 2023-01-04 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_alter_project_client_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPMStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_percent', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('ts_start_date', models.DateField(null=True)),
                ('ts_end_date', models.DateField(null=True)),
                ('rm_start_date', models.DateField(null=True)),
                ('rm_end_date', models.DateField(null=True)),
                ('fact_start_date', models.DateField(null=True)),
                ('fact_end_date', models.DateField(null=True)),
                ('is_payable', models.BooleanField(default=False, null=True)),
                ('invoice_number', models.CharField(max_length=100)),
                ('share_share', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('is_invoice_issued', models.BooleanField(default=False, null=True)),
                ('is_invoice_paid', models.BooleanField(default=False, null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('pm_stage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.pmstage')),
                ('pm_step', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.pmstep')),
            ],
        ),
        migrations.AlterField(
            model_name='projectpmstep',
            name='project_pm_stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.projectpmstage'),
        ),
    ]
