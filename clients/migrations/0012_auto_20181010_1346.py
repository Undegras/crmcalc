# Generated by Django 2.1.2 on 2018-10-10 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_auto_20181010_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='client_status_creditor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Status_client_Creditor'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='client_status_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Status_client_Info'),
        ),
    ]