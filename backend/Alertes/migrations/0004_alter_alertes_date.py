# Generated by Django 5.0.1 on 2024-05-06 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alertes', '0003_alter_alertes_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertes',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
