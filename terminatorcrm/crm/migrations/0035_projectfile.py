# Generated by Django 4.1.4 on 2023-03-01 06:17

import crm.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0034_cash_remove_projectpmstage_status_percent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('file', models.FileField(blank=True, null=True, upload_to=crm.models.project_file_name)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.project')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
