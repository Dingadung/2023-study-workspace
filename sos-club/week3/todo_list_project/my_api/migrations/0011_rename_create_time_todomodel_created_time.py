# Generated by Django 4.1.5 on 2023-01-24 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0010_alter_todomodel_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='create_time',
            new_name='created_time',
        ),
    ]