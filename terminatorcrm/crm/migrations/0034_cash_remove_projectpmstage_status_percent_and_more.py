# Generated by Django 4.1.4 on 2023-03-01 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0033_alter_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='projectpmstage',
            name='status_percent',
        ),
        migrations.CreateModel(
            name='ProjectPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_date', models.DateField(blank=True, null=True)),
                ('fact_date', models.DateField(blank=True, null=True)),
                ('invoice', models.CharField(blank=True, max_length=100, null=True)),
                ('plan_amount', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('fact_amount', models.DecimalField(decimal_places=2, max_digits=17, null=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('cash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.cash')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.project')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
