# Generated by Django 5.1 on 2024-09-05 18:21

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moncalc', '0005_alter_diagonal_gu_diag_alter_headunit_name_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='headunit',
            managers=[
                ('object_hu', django.db.models.manager.Manager()),
            ],
        ),
    ]
