# Generated by Django 2.1.2 on 2018-10-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20181010_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit_type',
            name='id',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]
