# Generated by Django 3.0.8 on 2020-07-07 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200707_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='summary',
            new_name='about',
        ),
    ]
